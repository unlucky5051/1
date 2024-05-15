from dist.Models.Condition import *
from dist.Controllers.Cabinet_Controller import *

class ConditionController():
    def add(self,position):
        con=Condition(position=position)
        validator = ModelValidator(con)
        if validator.validate():
            Condition.insert(position=position).execute()
        else:
            print("Ошибка: вы ввели имеющиеся данные")
    def get(self):
        return Condition.select().execute()
    def show_position(self,id):
        return Condition.get(Condition.id == id).position


if __name__ == "__main__":
    cond = ConditionController()
    # for number in range(10):
    #     cond.add(number)

    for row in range(1,11):
        print(cond.show_position(row))
