from datetime import datetime


class PrivateAd:
    def __init__(self, title: str, text: str, expiration_date):
        self.title = title
        self.text = text
        self.publish_date = datetime.now()
        self.expiration_date = expiration_date

        converted_date = datetime.strptime(self.expiration_date, "%Y-%m-%d")

        self.day_left = (converted_date - self.publish_date).days

    def __str__(self):
        return f"""
            _________________________________
                    {self.title}
                    
                    {self.text}
                    
                    Day left:  {self.day_left}
            _________________________________        
                    """
