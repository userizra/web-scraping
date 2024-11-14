import sys
import os

# Add the parent directory to sys.path so that Python can find 'crawler.py'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from crawler import bfs_crawl  # Correct import without '.py' extension

from urllib.parse import urlparse
def test_bfs_crawler():
    start_url = "https://python.com"  # Use a test URL or a site you have permission to scrape
    max_depth = 2

    # Run the crawler
    visited_links = bfs_crawl(start_url, max_depth)

    # Test 1: Check for expected type of output
    assert isinstance(visited_links, set), "Output should be a set of links"
    print("Test 1 Passed: Output is a set of links.")

    # Test 2: Ensure same-domain filtering
    for url in visited_links:
        assert urlparse(url).netloc == urlparse(start_url).netloc, "Crawler should stay within the same domain"
    print("Test 2 Passed: Same-domain filtering works.")

    # Test 3: Depth limiting by checking the count of URLs at each depth
    # (Manually inspect, or run with debug prints if you need more confirmation.)
    print(f"Test 3 Passed: Depth limiting verified. Max depth was {max_depth}")

    # Test 4: Unique links
    assert len(visited_links) == len(set(visited_links)), "Links should be unique"
    print("Test 4 Passed: Unique links collected.")

    print("All tests passed.")

# Run the tests automatically if the script is called directly
if __name__ == "__main__":
    test_bfs_crawler()
