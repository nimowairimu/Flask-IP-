import unittest
from models import movie
Movie = movie.Movie

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_sources = Sources(1234,'Undercover','A thrilling new Drug Trafficking season','https://Undercover/DrugLords','Reality','English','USA')

 self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources,Sources))


class ArticlesTest(unittest.TestCase)

 '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = Articles('John BLacc','New world architecture',"Article for the new architechture you'll expect to see in the next 20 years"','https://Undercover/new-world-architecture','https://www.google.com/url?sa=i&url= img.jpeg',20/15/17)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))

if __name__ == '__main__':
    unittest.main()