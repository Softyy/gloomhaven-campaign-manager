class GlobalAchievement():

    def __init__(self, id, title="test", banner="https://placeimg.com/200/480/any"):
        self.id = id
        self.title = title
        self.banner = banner

    def __repr__(self):
        return f'{self.id}-{self.title}'
