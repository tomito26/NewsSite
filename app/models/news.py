class News :
    '''
    Movie class to define movie objects
    '''
    
    def __init__(self, author, headline, description,urltoimage,publishAt,content):
        self.author = author
        self.headline = headline
        self.description = description
        self.urltoimage = urltoimage
        self.publishAt = publishAt
        self.content = content
       