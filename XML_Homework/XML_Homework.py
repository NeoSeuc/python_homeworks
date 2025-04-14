from OOP_Homework.News import News
import os
import xml.etree.ElementTree as ET

class XMLNewsProvider:
    def __init__(self, file_path=None):
        self.default_folder = "data"
        self.file_path = file_path or os.path.join(self.default_folder, "news.xml")

    def load_news(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")

        tree = ET.parse(self.file_path)
        root = tree.getroot()

        news_list = []
        for item in root.findall("record"):
            title = item.findtext("title", default="No title")
            text = item.findtext("text", default="No text")
            city = item.findtext("city", default="Unknown city")
            news = News(title, text, city)
            news_list.append(news)

        return news_list

    def cleanup(self):
        os.remove(self.file_path)
        print(f"File {self.file_path} was removed after successful processing.")


def main(file_path=None):
    provider = XMLNewsProvider(file_path)

    try:
        news_items = provider.load_news()
        for news in news_items:
            print(news)

        provider.cleanup()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()