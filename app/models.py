class News :
    '''
    News class to define news objects
    '''
    
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

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
        self.publishedAt = publishedAt
        