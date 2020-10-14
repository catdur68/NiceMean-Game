from abc import ABC, abstractmethod

class Dictionary(ABC):
    def ThisWord(self, word):
        print("{} has a variety of synonyms.".format(word))

    @abstractmethod
    def Synonym(self, x):
        pass
    def Other (self, y):
        pass

verbs = ['appropriate', 'arrogate', 'commandeer', 'convert', 'expropriate', 'pirate']
class Thesaurus_X(Dictionary):
    def Synonym(self, x):
        self.x = x
        count = 0
        while count < len(verbs):
            count = count + 1
        print("{} is one of these synonyms, but this word \nhas at least {} more synonyms you can use like: ".format(self.x, count))
            
    def Other(self, y):
        print("To see all definitions or synonyms, refer to https://merriam-webster.com/thesaurus/usurp")

vocabulary = Thesaurus_X()
vocabulary.ThisWord("'usurp'")
vocabulary.Synonym("'seize'")
for word in verbs:
        print("\t",word)
vocabulary.Other('usurp')

