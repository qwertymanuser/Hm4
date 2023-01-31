class A:
    def __init__(self,name) -> None:
        self.name = name
class B:
    def __init__(self,age) -> None:
        self.age = age
class C:
    def a():
        pass
class D:
    def b():
        pass
class Mar(A,B,C,D):
    def __init__(self, name,age) -> None:
        A.__init__(self,name)
        B.__init__(self,age)
    def __str__(self) -> str:
        return f"{self.name}, {self.age}"
marl = Mar("marlen",15)
print(marl)