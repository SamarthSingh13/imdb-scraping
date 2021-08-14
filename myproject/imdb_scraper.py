from bs4 import BeautifulSoup
import requests
import re
import sqlite3

'''Scraping given URL to create list of dictionary of required attributes'''

url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

movies = soup.select('td.titleColumn')
ratings = [x.attrs.get('data-value') for x in soup.select('td.posterColumn span[name=ir]')]
thumbnails = [x.attrs.get('src') for x in soup.select('td.posterColumn img')]
imdb = []

for index in range(0, len(movies)):
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    title = movie[len(str(index))+1:-7].lstrip()
    year = re.search('\((.*?)\)', movie_string).group(1)
    data = {"title": title,
            "year": year,
            "rating": ratings[index],
            "thumbnail_url": thumbnails[index]
            }
    imdb.append(data)

'''Inserting scraped data into db'''

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()
cursor.execute("DELETE FROM scraper_movie")
for item in imdb:
    cursor.execute("INSERT INTO scraper_movie(title,year,rating,thumbnail_url) VALUES (?,?,?,?)",
    (item['title'],int(item['year']),round(float(item['rating']),1),item['thumbnail_url']))

conn.commit()

conn.close()
    