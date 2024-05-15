from dist.Controllers.Controller import Controller
from dist.Models.Cabinet import *
from dist.Validators.BaseValidator import BaseValidator


# from peewee_validates import *

# котроллер для таблицы Cabinets, в которой будут созданы запросы в виде функций

class Cabinet_Controller(BaseValidator):



#     фунцции и методы описывающие действия над записями таблицы (запросы)
#     def __int__(self):
#         self.__table = Cabinet
#

    # Добавить запись
    def add_value(self,name,departament):
        cabinet = Cabinet(name = name, department = departament)
        validator = ModelValidator(cabinet)
        if validator.validate():
            Cabinet.insert(name=name, department=departament).execute()
        else:
            print('Ошибка',validator.errors)
        #

    def get(self):
        return Cabinet.select().execute()
    def show(self, name):
        return Cabinet.select(Cabinet.name, Cabinet.department).where(Cabinet.name == name).execute()

    def show_id(self,name):
        return Cabinet.get(Cabinet.name == name)
        # return Cabinet.select(Cabinet.id).where(Cabinet.name==name).execute()
    #Вывод кабинета по его ид
    def show_name(self,id):
        return Cabinet.get(Cabinet.id == id)
    # ОБНОВЛЕНИЯ ИМЕНИ по id
    def update_name(self,new_name, id):
        Cabinet.update({Cabinet.name:new_name}).where(Cabinet.id == id).execute()
    # удаление
    def delete_field(self,id):
        Cabinet.delete().where(Cabinet.id == id).execute()
    class Meta:

        messages = {
            'name.required': 'Введите имя',
            'required': 'Введите значение',
            'unique': 'Значение должно быть уникальным',

        }

if __name__ == "__main__":
    cab = Cabinet_Controller()
    # print(cab.show_id('207Т'))
    # print(cab.get())
    print(cab.show_name(18).name, cab.show_name(18).department)
