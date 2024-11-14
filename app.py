import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    url = 'https://www.python.org'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href = True)]
    return {"links": links}

if __name__ == "__main__":
    app.run(debug=True)