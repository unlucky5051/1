from dist.Models.Air_conditioners import *
from dist.Controllers.Cabinet_Controller import *
class Air_conditioners_Controller():



    # Добавить запись
    def add_value(self,name,cabinet):
        # присваивает cabinet_id - id кабинета, который введён в аргумент cabinet
        # например 218Т - присвоит cabinet_id id =18
        cabinet = Cabinet_Controller().show_id(cabinet)
        # создать экземпялр класса, который будет использоваться для валидации
        condit = Air_conditioners(name = name,state = False,cabinet_id = cabinet)
        validator = ModelValidator(condit)
        if validator.validate():
            # cabinet_id = Cabinet.select(Cabinet.id).where(Cabinet.name == cabinet)
            Air_conditioners.insert(name = name,  cabinet_id = cabinet).execute()
        else:
            print('Ошибка валидации', validator.errors)



    def get(self):
        return Air_conditioners.select().execute()

    # Вывод id по имени КОНДИЦИОНЕРА
    def show_id(self, name):
        # return Air_conditioners.select(Air_conditioners.name, Air_conditioners.department).where(Air_conditioners.name == name).execute()
    #     через метод peewee.get()
        try:
            return Air_conditioners.get(Air_conditioners.name == name).id
        except:
            print('Ошибка: Нет такого кондиционера')

    def show_cabinet_id(self,id):
        try:
            return Air_conditioners.get(Air_conditioners.id == id).cabinet_id
        except:
            print('Ошибка: Нет такого кондиционера')
    def show_state(self,name):
        return Air_conditioners.get(Air_conditioners.name == name).state
    # ОБНОВЛЕНИЯ ИМЕНИ по id

    def update_name(self,new_name, id):
        cabinet_id = Air_conditioners_Controller().show_cabinet_id(id)
        condit = Air_conditioners(name = new_name,state = False,id = id,cabinet_id = cabinet_id)
        validator = ModelValidator(condit)
        if validator.validate():
            Air_conditioners.update({Air_conditioners.name:new_name}).where(Air_conditioners.id == id).execute()
        else:
            print('Ошибка валидации',validator.errors)

    def update(self,old_name,new_name):

        id = Air_conditioners_Controller().show_id(old_name)
        cabinet_id = Air_conditioners_Controller().show_cabinet_id(id)
        condit = Air_conditioners(name = new_name, state = False, cabinet_id = cabinet_id)
        valid = ModelValidator(condit)
        if valid.validate():
            Air_conditioners.update({Air_conditioners.name:new_name}).where(Air_conditioners.id == id).execute()
        else:
            print('Ошибка валидации', valid.errors)

    # удаление
    def delete_field(self,id):
        Air_conditioners.delete().where(Air_conditioners.id == id).execute()

    def delete(self,name):
        id = Air_conditioners_Controller().show_id(name)
        cabinet_id = Air_conditioners_Controller().show_cabinet_id(id)
        condit = Air_conditioners(name = name, state = False, cabinet_id = cabinet_id)
        vaildator = ModelValidator(condit)
        if vaildator.validate() != True :
            Air_conditioners_Controller().delete_field(id)
        else:
            print('Ошибка валидации', vaildator.errors)

    def edit_state(self,name,state):

        Air_conditioners.update({Air_conditioners.state:state}).where(Air_conditioners.name == name).execute()



if __name__ == "__main__":
    print("Это файл Air_conditioners_Controller")
    conditioner = Air_conditioners_Controller()
    for el in conditioner.get():
        print(el.id, el.name,el.state,el.cabinet_id.name)

    print(conditioner.show_state('218Т-4'))
    conditioner.edit_state('218Т-4',True)
    print(conditioner.show_state('218Т-4'))

    print(Air_conditioners.window_name)
