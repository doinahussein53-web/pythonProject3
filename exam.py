import abc
from ipaddress import ip_interface


class DOCUMENT:
    def __init__(self,title="public",author="protected",doc_type="PDE,DOCX"):
        self.title=title
        self.author=author
        self.doc_type=doc_type
    def __str__(self):
        return f"{self.title} {self.author}"

    def __add__(self, other):
        return self.doc_type + other.doc.type

class child (DOCUMENT):
   super().__init__(title="public",author="protected",doc_type="PDF,DOCX")
   def __init__(self):
       self.__state=state


   def set_state(self,state):
       if state in ["property to set state either rejected or accepted"]:
           self.__state=state
       else:
           print("error")


doc1=DOCUMENT("python","property rejected","PDF")
doc2=DOCUMENT("book","property accepted","DOCX")
print(doc1)
print(doc2)
print(doc1+doc2)



#####

from abc import ABC ,abstractmethod

class Book:

class interface(ABC):
    @abstractmethod
    def get_pages(self):
        pass
    @abstractmethod
    def property_title(self):
        pass
class book(Book):
    def __init__(self,title,author,type,num_pages):
        self.title=title
        self.author=author
        self.type=type
        self.num_pages=num_pages
    def __str__(self):
        return f"{self.title}{self.author}{self.type}{self.num_pages}"
    def number_pages(self):
        return self.num_pages<=100
    def __gt__(self, other):
        return self.num_pages>other.num_pages
    def set_title(self, title):
        if title in ["opp","data mining"]:
            self.title=title
        else:
            print("error")


b1=Book("OPP",)












