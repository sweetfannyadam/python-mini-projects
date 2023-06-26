import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
html = response.text

soup = BeautifulSoup(html, "html.parser")

movie_tag = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in movie_tag]
movies = movie_titles[::-1]

with open("movies.txt", encoding="utf-8", mode="w") as file:
    for movie in movies:
        print(movie)
        file.write(f"{movie}\n")
