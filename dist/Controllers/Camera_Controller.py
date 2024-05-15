from dist.Models.Camera import Camera
from dist.Models.Cabinet import *
from dist.Controllers.Cabinet_Controller import *
class Camera_Controller():

    # вывод всех записей
    def get(self):
        return Camera.select().execute()

    # добавить запись
    def add(self,name,link,cabinet):

        # запрос на id введённого кабинета
        # cabinet_id = Cabinet.select(Cabinet.id).where(Cabinet.name == cabinet)
        cabinet_id = Cabinet_Controller().show_id(cabinet)
        # __cabinet = Cabinet(id=cabinet_id)
        camera = Camera(name=name, link=link, cabinet_id=cabinet_id)
        validator_camera = ModelValidator(camera)
        # validator_cabinet = ModelValidator(__cabinet)
        if validator_camera.validate():
            Camera.insert(name=name, link=link, cabinet_id=cabinet_id).execute()
            print(f"Камера {name} добавлена в кабинет {cabinet}")
        else:
            print('Ошибка валидации',validator_camera.errors,)

    #   вывод отдельных полей
    def show_id(self,name):
        try:
            return Camera.get(Camera.name==name).id
        except:
            print('Ошибка: Нет камеры с таким именем')
    def show_link(self,name):
        try:
            return Camera.get(Camera.name == name).link
        except:
            print('Ошибка: Нет камеры с таким именем')
    def show_cabinet_id(self,name):
        try:
            return Camera.get(Camera.name == name).cabinet_id.id
        except:
            print('Ошибка: Нет камеры с таким именем')

#     обновление
    def update_name(self,old_name,new_name):
        cabinet_id = self.show_cabinet_id(old_name)

        camera = Camera(name=new_name,link='test',cabinet_id=cabinet_id)
        validator = ModelValidator(camera)
        if validator.validate():
            Camera.update({Camera.name:new_name}).where(Camera.name==old_name).execute()
        else:
            print('Ошибка валидации',validator.errors)
    def update_link(self,name,new_link):
        cabinet_id = self.show_cabinet_id(name)
        link = self.show_link(name)
        camera = Camera(name = name, link = link, cabinet_id = cabinet_id)
        validator = ModelValidator(camera)
        if validator.validate() != True:
            Camera.update({Camera.link:new_link}).where(Camera.name == name).execute()
        else:
            print('Ошибка валидации',validator.errors)

    def delete(self, name):
        cabinet_id = self.show_cabinet_id(name)
        link = self.show_link(name)
        camera = Camera(name=name,link = link, cabinet_id = cabinet_id)
        validator =ModelValidator(camera)
        if validator.validate():
            print('''''')
        else:
            Camera.delete().where(Camera.name == name).execute()


if __name__ == '__main__':
    camera = Camera_Controller()
    def print_table():
        for row in camera.get():
            print(row.name, row.link,row.cabinet_id.name)
    print_table()
    # camera.update_name('cam1','cam1-1')
    # camera.update_link('cam1-1--','mail.ru')
    camera.delete('№4')
    print('-----------------------------')
    print_table()


