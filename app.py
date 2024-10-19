import requests
import streamlit as st

def fetch_media_urls(base_url, max_pages=None, extensions=None):
    page = 1
    media_urls = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    while True:
        url = f"{base_url}/wp-json/wp/v2/media/?page={page}&per_page=100"
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            st.error(f"Failed to fetch data: {response.status_code}")
            break

        data = response.json()
        
        if not data:
            # No more data to fetch
            break

        for item in data:
            if 'guid' in item and 'rendered' in item['guid']:
                media_url = item['guid']['rendered']
                if extensions:
                    if any(media_url.endswith(ext) for ext in extensions):
                        media_urls.append(media_url)
                else:
                    media_urls.append(media_url)

        page += 1

        if max_pages and page > max_pages:
            break

    return media_urls

def main():
    st.title("WP Media URL Sniffer")

    # Input fields
    base_url = st.text_input("Enter the WordPress site URL:")
    max_pages = st.number_input("Number of pages to scrape:", min_value=1, step=1, value=1)
    extensions_input = st.text_input("Filter by file extensions (comma-separated, e.g., zip,pdf):")

    # Convert extensions input to a list
    extensions = [ext.strip() for ext in extensions_input.split(',')] if extensions_input else None

    if st.button("Fetch Media URLs"):
        if base_url:
            media_urls = fetch_media_urls(base_url.strip(), max_pages, extensions)
            if media_urls:
                st.success(f"Found {len(media_urls)} media URLs:")
                for url in media_urls:
                    st.write(url)
            else:
                st.warning("No media URLs found.")
        else:
            st.error("Please enter a valid WordPress site URL.")

    st.divider()

    st.write('An experiment by [Francesco Carlucci](https://francescocarlucci.com)')

if __name__ == "__main__":
    main()
