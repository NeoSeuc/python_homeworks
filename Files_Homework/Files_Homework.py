from OOP_Homework.News import News
from OOP_Homework.PrivatAd import PrivateAd
import os

file = open("articles.txt", mode="a")


news1 = News("News Title", "News Text", "Kiev")

file.write(str(news1))

privatead1 = PrivateAd("Private AD Title", "Private AD text", "2025-05-01")
file.write(str(privatead1))
