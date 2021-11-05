class Course:
    def __init__(self, name, maxgrade, cost, lessons):
        self.name = name
        self.maxgrade = maxgrade
        self.cost = cost # cost +ve, cost = cost + (.14)Cost


    # make sure that the maxgrade should be more than 100
    # customize property in calculation
    @property
    def passgrade(self):
        return self.maxgrade*.6

    # property limit setting and getting
    @property
    def cost(self):
        return self.__a + (self.__a*.14)

    @cost.setter
    def cost(self, cost):
        cost = abs(cost)
        self.__a = cost



c = Course("python", 100, -1000)
print(c.cost)
print("test")
