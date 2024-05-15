from dist.Model.Cabinet import *

cabinet = Cabinet
class Cabinet_Controller():
    def __init__(self):
        self.__table = Cabinet()

    def add_value(self , name , departament):
        self.__table.insert(name = name, departament = departament).execute()

    def get(self):
        return Cabinet.select().execute()

    def show(self, name):
        return Cabinet.select(Cabinet.name, Cabinet.departament).where(Cabinet.name == name).execute()

    def update_name(self, new_name, id):
        Cabinet.update({Cabinet.name:new_name}).where(Cabinet.id == id).execute()

    def delete_field(self, id):
        Cabinet.delete().where(Cabinet.id == id).execute()