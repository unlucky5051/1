from dist.Models.Electrical_line import *

class Electrical_line_Controller():

    def add(self,state,cabinet):
        # переменной cabinet_id передаётся результат запроса в класс Cabinet? который выводит id




        cabinet_id = Cabinet.select(Cabinet.id).where(Cabinet.name == cabinet).limit(1).execute()



        # __el = Electrical_line(state, cabinet_id)
        # validator = ModelValidator(__el)
        # validator.validate()
        print(cabinet_id)
        # print(validator.validate())
        # print(validator.errors)
        # Electrical_line.insert(state = state, cabinet_id = cabinet_id).execute()
    def get(self):
        return Electrical_line.select().execute()