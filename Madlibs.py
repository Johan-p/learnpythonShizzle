"""
In this project, we'll use Python to write a Mad Libs word game! Mad Libs have short stories with blank spaces that a player can fill in. The result is usually funny (or strange).

Mad Libs require:

A short story with blank spaces (asking for different types of words).
Words from the player to fill in those blanks.
"""

# The template for the story

print "starting Mad Libs"

Name = raw_input("Enter a name: ")
Adjective_1 = raw_input("Adjective One: ")
Adjective_2 = raw_input("Adjective Two: ")
Adjective_3 = raw_input("Adjective Three: ")
Verb = raw_input("verb: ")
Nouns_1 = raw_input("nouns One: ")
Nouns_2 = raw_input("nouns Two: ")
Animal = raw_input("input an animal: ")
Food = raw_input("input a food: ")
Fruit = raw_input("input a fruit: ")
Superhero = raw_input("input a superhero: ")
Country = raw_input("input a country: ")
Dessert = raw_input("input a dessert: ")
Year = raw_input("input a Year: ")

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world." % (Name, Adjective_1, Adjective_2, Animal, Food, Verb, Nouns_1, Fruit, Adjective_3, Name, Superhero, Name, Country, Name, Dessert, Name, Year, Nouns_2)

print STORY



















