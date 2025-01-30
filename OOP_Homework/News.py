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

    def to_dict(self):
        # Return a dictionary representation of the object
        return {
            'title': self.title,
            'text': self.text,
            'city': self.city
        }
