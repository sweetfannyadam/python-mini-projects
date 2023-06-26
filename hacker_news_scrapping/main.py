from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
html_data = response.text
soup = BeautifulSoup(html_data, "html.parser")

article_titleline = soup.find_all(name="span", class_="titleline")
article_text = [tag.getText() for tag in article_titleline]
article_link = [tag.find(name="a").get("href") for tag in article_titleline]

article_subline = soup.find_all(name="span", class_="score")
article_upvote = [int(tag.getText().split(' ')[0]) for tag in article_subline]

data_dict = {
    article_upvote[i]:[
        article_text[i],
        article_link[i]
    ] for i in range(len(article_upvote))
}

for score in sorted(article_upvote):
    print(f"{score}\n{data_dict[score][0]}\n{data_dict[score][1]}")





























# import lxml
# with open(file="website.html", mode="r") as data:
#     content = data.read()
#
# soup = BeautifulSoup(content, "html.parser")

