import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def bfs_crawl(start_url, max_depth = 3):
    visited = set() #This keeps track of my visited URLs
    queue = [(start_url, 0)]

    while queue:
        url, depth = queue.pop(0)
        if depth > max_depth:
            continue
        if url in visited:
            continue
            
        visited.add(url)
        print(f"Scraping {url} at depth {depth}")
        try:
            #Fetch and parse the page
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            for a_tag in soup.find_all('a', href=True):
                link = a_tag['href']
                full_url = urljoin(url, link)

                if urlparse(full_url).netloc == urlparse(start_url).netloc:
                    if full_url not in visited:
                        queue.append((full_url, depth + 1))
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
    return visited