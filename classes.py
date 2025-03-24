class MyClass:
    x = 10



my_first_class = MyClass()

print(my_first_class.x)



class HelloWorld:
    def __init__(self,name):
        self.name = name


helloWorld = HelloWorld("siva")
print(helloWorld.name)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


person = Person("siva",30)

print(person.name)
print(person.age)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}({self.age})"
    
person = Person("Jhon",30)

print(person)


class Person:
    def __init__(self,name):
        self.name = name
    
    def myFunction(self):
        print(f"Hello {self.name}")
        

person = Person("siva")
person.myFunction()

"""
You can use any word instead of self for example see down below
"""

class SelfChangingToOtherWords:
    def __init__(my_fucking_word_insted_of_self,name,age):
        my_fucking_word_insted_of_self.name = name
        my_fucking_word_insted_of_self.age = age
    
    def my_fucking_function(abc):
        print("This is my Fucking function calling " + abc.name)


self_changing_to_other_words = SelfChangingToOtherWords("siva",30)
self_changing_to_other_words.my_fucking_function()




