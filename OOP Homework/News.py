import datetime
class News:
    def __init__(self, title: str, text: str, city: str):
        self.title = title
        self.text = text
        self.city = city
        self.publish_date = datetime.datetime.now()

    def __str__(self):
        return f"""
        _________________________________
                {self.title}
                
                {self.text}
                
                {self.city}  {self.publish_date}
        _________________________________        
                """
