import json
import urllib.request
from bs4 import BeautifulSoup
from django.shortcuts import render

def index_view(request):
    # Fetch contributors from GitHub
    contributors_url = "https://github.com/UIU-Developers-Hub/Sir-Kothay/contributors_list?count=100&current_repository=Sir-Kothay&items_to_show=100"
    contributors = []
    try:
        with urllib.request.urlopen(contributors_url) as response:
            html = response.read().decode('utf-8')
            soup = BeautifulSoup(html, 'html.parser')
            lis = soup.find_all('li', class_='mb-2 d-flex')
            for li in lis:
                a_img = li.find('a', class_='mr-2')
                if a_img:
                    img = a_img.find('img')
                    profile_url = a_img['href']
                    image_url = img['src'] if img else ''
                    contributors.append({
                        'profileUrl': profile_url,
                        'imageUrl': image_url
                    })
    except:
        contributors = []

    return render(request, 'index.html', {'contributors': contributors})