from practice.hello import Calculation


class Child(Calculation):
    num2 = 500

    def __init__(self):
        Calculation.__init__(self)

    def test2(self, a, b):
        return print(a + b)


obj3 = Child()
obj3.test2(5, 10)
obj3.test5()
