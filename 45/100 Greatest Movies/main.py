from bs4 import BeautifulSoup as bs
from requests import get

website_data = get('https://www.filmsite.org/empireuk100-2.html')

soup = bs(website_data.text, 'html.parser')

movies = soup.select(selector='table tr li font a')

print()

with open('movies.txt', 'w') as file:
    for index, movie in enumerate(movies):
        file.write(f"{index + 1}. {' '.join(movie.text.split())}\n")
