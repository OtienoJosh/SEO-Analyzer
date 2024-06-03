from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

def analyze_seo(url):
    # Fetch the URL content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Analyze basic SEO factors
    title = soup.title.string if soup.title else 'No title found'
    meta = soup.find('meta', attrs={'name': 'description'})
    meta_description = meta['content'] if meta else 'No meta description found'
    meta_keywords = soup.find('meta', attrs={'name': 'keywords'})
    meta_keywords = meta_keywords['content'] if meta_keywords else 'No meta keywords found'

    # Title length
    title_length = len(title) if title else 0

    # Alt text for images
    images = soup.find_all('img')
    images_with_alt = sum(1 for img in images if img.get('alt'))
    total_images = len(images)

    # Internal and external links
    internal_links = []
    external_links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith('/'):
            internal_links.append(href)
        elif href.startswith('http') and not url.startswith(href):
            external_links.append(href)

    # Word count
    word_count = len(soup.get_text().split())

    # Keyword density (example keyword: "flask")
    keyword = "flask"
    keyword_count = len(re.findall(r'\b' + re.escape(keyword) + r'\b', soup.get_text(), re.IGNORECASE))
    keyword_density = (keyword_count / word_count) * 100 if word_count else 0

    seo_data = {
        'title': title,
        'title_length': title_length,
        'meta_description': meta_description,
        'meta_keywords': meta_keywords,
        'h1_tags': [h1.text for h1 in soup.find_all('h1')],
        'word_count': word_count,
        'images_with_alt': images_with_alt,
        'total_images': total_images,
        'internal_links': internal_links,
        'external_links': external_links,
        'keyword_density': keyword_density
    }

    return seo_data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    url = request.form.get('url')
    if not url.startswith('http'):
        url = 'http://' + url
    seo_data = analyze_seo(url)
    return render_template('results.html', seo_data=seo_data, url=url)

if __name__ == '__main__':
    app.run(debug=True)
