""" 
By Jessica Angela Campisi
Date: 11/1/2019
Purpose: Create and display a story
"""

class Story:
    title = ""
    story = ""
    author = ""

    def __init__(self):
        self.title = self.setTitle()
        self.story = self.setStory()
        self.author = self.setAuthor()
    
    def setTitle(self):
        return "A Soldier's Surprise"
        
        # input("What is the title to the story: ")
    
    def setStory(self):
        return "It is spring of 1943 during World War II. Standing among hundreds of new soldiers at Camp Grant, in Illinois, my father, Sam, just 18 years old, waits as a truck slowly drives by. A full field pack is randomly tossed to each soldier. \"How strange,\" my father thinks, as he sees his last name, Litrenti, marked on each item in his pack. \"How did they know it was me when they tossed the pack?\" He was impressed! Beating all odds, my father was tossed a field pack from World War I—his own father’s."
        
        # input("\nPlease write me a story: ")
    
    def setAuthor(self):
        return "Gail Litrenti-Benedetto"
    
    def returnStory(self):
        return "<h1>{0}</h1><i>{2}</i><br><p>{1}</p>".format(self.title, self.story, self.author)
