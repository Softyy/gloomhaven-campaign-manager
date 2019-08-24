from datetime import datetime as dt


class GlobalAchievement():

    def __init__(self, id, title="test", banner="https://placeimg.com/200/480/any", acquired_date=dt.today()):
        self.id = id
        self.title = title
        self.acquired_date = acquired_date
        self.banner = banner

    def __repr__(self):
        return f'{self.id}-{self.title}'
