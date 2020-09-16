import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    
    def setUp(self):
        self.new_articles = Articles('tom','Technology advancement','The artificial intelligence takeover','http://ww.wzxnews.com','http://xhcbjkjkc.jpeg','23/7/20')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))