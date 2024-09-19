class Person:
    def __init__(self):
        self.A="john"
        self._B="John Bond"
    def PrintName(self):
        print(self.A)
        print(self._B)
p=Person()
p.A
p._B
p.PrintName()