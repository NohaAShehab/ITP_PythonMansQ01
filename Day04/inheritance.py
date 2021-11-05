class Person:
    Alive = True

    def __init__(self, name="", dataofbirth="", nationality="", income=0):
        # public instance variables
        self.name = name
        self.dataofbirth = dataofbirth
        self._nationality = nationality  # protected
        self.__income = income

    def speak(self):
        print(f"I am {self.name}")

    # def setIncome(self, income):
    #     if income.isalpha():
    #         income = 0
    #     self.__income = income
    #
    # def getIncome(self):
    #     return abs(self.__income)
    # private member ---> setter , getter

    @classmethod
    def createperson(cls):
        return cls("Adam", 1990)

    @staticmethod
    def calage(year):
        return 2021 - year
