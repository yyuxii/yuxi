# scrapy-news

pulls the latest headlines from a few tech RSS feeds and prints them in the terminal. no external libraries needed.

## usage

```bash
python scraper.py
```

## output

```
── headlines 2024-03-12 11:05 ──

[ hacker news ]
  • Ask HN: What are you working on?
    https://news.ycombinator.com/item?id=...
  • Show HN: I built a static site generator in 200 lines of Go
    https://news.ycombinator.com/item?id=...

[ the verge ]
  • Apple's new chip is faster but runs hotter
    https://www.theverge.com/...
  ...
```

## add your own feeds

edit the `FEEDS` dict in `scraper.py`:

```python
FEEDS = {
    "my source": "https://example.com/rss",
    ...
}
```

works with both RSS 2.0 and Atom feeds.
