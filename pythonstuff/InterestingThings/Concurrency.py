"""
Concurrency examples (intermediate):

Includes:
- thread_pool_example(): simple IO-bound concurrency (requests).
- process_pool_example(): CPU-bound concurrency (heavy CPU task).
- asyncio_example(): high-concurrency IO using aiohttp.
- producer_consumer_example(): communication between threads using queue.

Run the section(s) you want from __main__.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed, ProcessPoolExecutor
import asyncio
import time
from typing import List, Optional
from queue import Queue
from threading import Thread

# Optional external libs used below:
# pip install requests aiohttp
import requests
import aiohttp
import math


# ---------------------------
# IO-bound: ThreadPoolExecutor
# ---------------------------
def fetch_url(url: str, timeout: float = 10.0) -> Optional[str]:
    """Fetch a URL using requests (blocking). Returns text or None on error.
    Suitable for IO-bound work; safe to call from worker threads.
    """
    try:
        resp = requests.get(url, timeout=timeout)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        return f"ERROR: {e}"


def thread_pool_example(urls: List[str], max_workers: int = 5) -> None:
    """Run multiple blocking HTTP requests concurrently using a thread pool."""
    start = time.time()
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        futures = {ex.submit(fetch_url, u): u for u in urls}
        for fut in as_completed(futures):
            url = futures[fut]
            try:
                result = fut.result()
                print(f"[thread] {url}: {len(result) if isinstance(result, str) else result}")
            except Exception as e:
                print(f"[thread] {url} failed: {e}")
    print(f"[thread] elapsed: {time.time() - start:.2f}s\n")


# ---------------------------
# CPU-bound: ProcessPoolExecutor
# ---------------------------
def cpu_heavy(n: int) -> int:
    """A CPU-heavy task: compute sum of primes <= n (naive)"""
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        if x % 2 == 0 and x != 2:
            return False
        r = int(math.sqrt(x))
        for i in range(3, r + 1, 2):
            if x % i == 0:
                return False
        return True

    return sum(i for i in range(2, n + 1) if is_prime(i))


def process_pool_example(inputs: List[int], max_workers: int = 4) -> None:
    """Run CPU-heavy tasks in parallel using multiple processes."""
    start = time.time()
    with ProcessPoolExecutor(max_workers=max_workers) as ex:
        futures = {ex.submit(cpu_heavy, n): n for n in inputs}
        for fut in as_completed(futures):
            n = futures[fut]
            try:
                result = fut.result()
                print(f"[process] primes_sum({n}) = {result}")
            except Exception as e:
                print(f"[process] {n} failed: {e}")
    print(f"[process] elapsed: {time.time() - start:.2f}s\n")


# ---------------------------
# High concurrency: asyncio + aiohttp
# ---------------------------
async def async_fetch(session: aiohttp.ClientSession, url: str) -> str:
    """Asynchronous fetch using a shared aiohttp ClientSession."""
    async with session.get(url) as resp:
        resp.raise_for_status()
        return await resp.text()


async def asyncio_example(urls: List[str], concurrency: int = 20) -> None:
    """Perform many concurrent HTTP requests efficiently with asyncio + aiohttp."""
    start = time.time()
    connector = aiohttp.TCPConnector(limit_per_host=concurrency)
    timeout = aiohttp.ClientTimeout(total=30)
    async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        sem = asyncio.Semaphore(concurrency)

        async def guarded_fetch(u: str) -> str:
            async with sem:
                try:
                    return await async_fetch(session, u)
                except Exception as e:
                    return f"ERROR: {e}"

        tasks = [asyncio.create_task(guarded_fetch(u)) for u in urls]
        # gather with return_exceptions=True to avoid cancelling all on first failure
        results = await asyncio.gather(*tasks, return_exceptions=True)
        for u, r in zip(urls, results):
            if isinstance(r, Exception):
                print(f"[async] {u} failed: {r}")
            else:
                print(f"[async] {u}: {len(r)}")
    print(f"[async] elapsed: {time.time() - start:.2f}s\n")


# ---------------------------
# Producer-consumer with Queue (threads)
# ---------------------------
def producer(q: Queue, items: List[int]) -> None:
    """Producer puts items into the queue."""
    for it in items:
        print(f"[producer] producing {it}")
        q.put(it)
    # signal consumers to stop
    q.put(None)


def consumer(q: Queue) -> None:
    """Consumer processes items until it sees sentinel None."""
    while True:
        item = q.get()
        if item is None:
            # put sentinel back for other consumers then exit
            q.put(None)
            break
        # simulate processing
        print(f"[consumer] processing {item}")
        time.sleep(0.5)
    print("[consumer] exiting")


def producer_consumer_example() -> None:
    """Start one producer and two consumers demonstrating safe communication via Queue."""
    q: Queue = Queue()
    items = list(range(1, 6))
    prod = Thread(target=producer, args=(q, items))
    cons1 = Thread(target=consumer, args=(q,))
    cons2 = Thread(target=consumer, args=(q,))

    cons1.start()
    cons2.start()
    prod.start()

    prod.join()
    cons1.join()
    cons2.join()
    print("[pc] done\n")


# ---------------------------
# Main runner: choose which example to run
# ---------------------------
if __name__ == "__main__":
    # Example targets (adjust as needed)
    test_urls = [f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(1, 6)]

    print("1) ThreadPoolExecutor (IO-bound)")
    thread_pool_example(test_urls, max_workers=5)

    print("2) ProcessPoolExecutor (CPU-bound)")
    # inputs are sizes for CPU work (bigger -> heavier)
    process_pool_example([20000, 22000], max_workers=2)

    print("3) asyncio + aiohttp (many concurrent IO)")
    asyncio.run(asyncio_example(test_urls * 4, concurrency=20))

    print("4) Producer-Consumer pattern (threads + Queue)")
    producer_consumer_example()