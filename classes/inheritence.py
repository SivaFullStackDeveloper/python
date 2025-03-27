class GrandParent:
    def generationGrandParent(self):
        print("this is grand parent generation")
    
    def ageGrandParent(self):
        print("Im a old person")


class Parent(GrandParent):
    def generationParent(self):
        print("this is parent generation")
    
    def ageParent(self):
        print("Im a mid age person")

class Child(Parent):
    def generationChild(self):
        print("this is Child generation")
    
    def ageChild(self):
        print("Im a young age person")


child = Child()

child.generationChild()
child.ageChild()
child.ageParent()
child.generationParent()
child.generationGrandParent()
child.ageGrandParent()


class A:
    def feauture1(self):
        print("this is feature 1")

    def feauture2(self):
        print("this is feature 1")

class B:
    def feauture3(self):
        print("this is feature 3")
        
    def feauture4(self):
        print("this is feature 4")

class C(A,B):
    def feauture5(self):
        print("this is feature 3")
        
    def feauture6(self):
        print("this is feature 4")