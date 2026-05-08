# Detailed Python Concurrency Examples

This ZIP contains 45 practical examples:

- 15 examples for threading
- 15 examples for multiprocessing
- 15 examples for asyncio

## Install Dependencies

```bash
pip install -r requirements.txt
```

## When to Use

| Technique | Best For | Example Use Cases |
|---|---|---|
| Threading | I/O-bound work | requests.get, file reading, web scraping, downloading |
| Multiprocessing | CPU-bound work | heavy calculations, parallel data processing |
| Asyncio | High-concurrency I/O | async APIs, async scraping, queues, pipelines |

## Important Teaching Point

Concurrency means managing multiple tasks at the same time logically.
Threading, multiprocessing, and asyncio are different ways to achieve concurrency.