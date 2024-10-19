# WP Media URL Sniffer

This Python application is a reconnaissance tool designed to fetch media URLs from a WordPress site using the REST API.

It leverages the fact that many WordPress plugins overlook the public nature of the media folder, which should not be used to store sensitive attachments.

## Features

- **URL Input**: Enter the WordPress site URL to start fetching media URLs.
- **Page Limit**: Specify the number of pages to scrape for media URLs.
- **File Extension Filter**: Optionally filter results based on file extensions (e.g., `zip`, `pdf`).
- **User-Friendly Interface**: Built with Streamlit for an easy-to-use web interface.

## Installation

```
git clone https://github.com/yourusername/wordpress-media-url-sniffer.git
cd wordpress-media-url-sniffer
pip install -r requirements.txt
streamlit run app.py
```

### Disclaimer

This piece of software is not intended to be used for malicious purposes.

It's just a draft, if you like the concept feel free to fork it and extend it!

Created by: [Francesco Carlucci]([https://frenxi.com](https://francescocarlucci.com/))
