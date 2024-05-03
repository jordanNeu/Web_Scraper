from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name = "span", class_="titleline")


article_texts = []
article_links = []

for article_tag in articles:
    a_tag = article_tag.find("a")
    if a_tag:
        text = a_tag.getText()
        article_texts.append(text)

        link = a_tag.get('href')
        article_links.append(link)

# article_upvotes = soup.find_all(name = "span", class_="score")
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name = "span", class_="score")]
print(article_texts)
print(article_links)
print(article_upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])






























# # import lxml
# # HOW TO USE BEAUTIFUL SOUP
# with open("website.html") as file:
#     contents = file.read()
# # IF HTML.PARSER ISNT WORKING
# # soup = BeautifulSoup(contents, "lxml")
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.prettify())
# # print(soup.title)
# # print(soup.title.name)
#
# all_anchors = soup.find_all(name="a")
# print(all_anchors)
#
# # LOOPED
# for tag in all_anchors:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# # section_heading.getText() | section_heading.name
#
# anchors_in_lists = soup.select("li a")
#
# # form_tag = soup.find("input")
# # max_length = form_tag.get("maxlength")