from OOP_Homework.News import News
import json

news1 = News("News Title", "News Text", "Kiev")

with open('news_data.json', 'w') as json_file:
    json.dump(news1.to_dict(), json_file, indent=4)