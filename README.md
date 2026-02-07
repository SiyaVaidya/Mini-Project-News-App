# News API Project

A Python script that fetches news articles based on a user query using the NewsAPI.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Install required dependencies:
```bash
pip install requests
```

2. Get a free API key from [NewsAPI.org](https://newsapi.org/)

## Setup

1. Open `main.py`
2. Replace the empty `api` variable with your NewsAPI key:
```python
api="your_api_key_here"
```

## Usage

Run the script:
```bash
python main.py
```

The script will prompt you to enter the type of news you're interested in. It will then fetch and display:
- Article titles
- Article URLs
- A separator between articles

## Features

- Fetches news from today's date dynamically
- Displays articles with titles and URLs
- Sorts articles by publication date
- User-friendly interface with clear prompts

## Example

```
What type of News are you interested in today ?
technology
1. Latest AI Breakthrough Announced
https://example.com/article1

**************************************

2. New Tech Gadget Released
https://example.com/article2

**************************************
```

## License

Free to use for personal projects.
