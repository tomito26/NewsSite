class Articles:
    '''
    function class to define  article objects
    '''
    def __init__(self,author,title,description,url,urlToImage,publishedAt):
        self.authtor = author
        self.title = title
        self.description = description
        self.url  = url
        self.urlToImage= urlToImage
        self.publishAt = publishedAt
        