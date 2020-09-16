import unittest
from app.models import News



class NewsTest(unittest.TestCase):
    '''
    Test class to test the behavior of the News class
    '''
    
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_news = News('abc-news','ABC News','Autralia most trusted source')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))



