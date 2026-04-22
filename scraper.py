#!/usr/bin/env python3
"""
scrapy-news — pull headlines from RSS feeds
"""

import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime

FEEDS = {
    "hacker news": "https://news.ycombinator.com/rss",
    "the verge":   "https://www.theverge.com/rss/index.xml",
    "ars technica": "https://feeds.arstechnica.com/arstechnica/index",
}


def fetch_feed(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=5) as r:
            return r.read()
    except Exception as e:
        print(f"  error fetching {url}: {e}")
        return None


def parse_feed(data):
    headlines = []
    try:
        root = ET.fromstring(data)
        ns = ""
        # handle atom feeds
        if "feed" in root.tag:
            ns = root.tag.split("}")[0] + "}"
            for entry in root.findall(f"{ns}entry")[:5]:
                title = entry.find(f"{ns}title")
                link = entry.find(f"{ns}link")
                if title is not None:
                    href = link.get("href", "") if link is not None else ""
                    headlines.append((title.text.strip(), href))
        else:
            for item in root.findall(".//item")[:5]:
                title = item.find("title")
                link = item.find("link")
                if title is not None:
                    headlines.append((
                        title.text.strip(),
                        link.text.strip() if link is not None else ""
                    ))
    except Exception as e:
        print(f"  parse error: {e}")
    return headlines


def run():
    print(f"\n── headlines {datetime.now().strftime('%Y-%m-%d %H:%M')} ──\n")
    for source, url in FEEDS.items():
        print(f"[ {source} ]")
        data = fetch_feed(url)
        if data:
            items = parse_feed(data)
            for title, link in items:
                print(f"  • {title}")
                if link:
                    print(f"    {link}")
        print()


if __name__ == "__main__":
    run()
