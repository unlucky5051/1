from dist.Model.Camera import *
class CameraController():

    __camera__ = Camera()

    def get(self):
        return Camera.select().execute
    def get_camera_cabinet(self):
        return Camera.select().execute()

    def add(self,name,link,cabinet_id):
        __camera = Camera(name=name, link=link, cabinet_id=cabinet_id)
        validator = ModelValidator(__camera)
        if validator.validate():
            Cabinet.insert(name=name, departament=departament).execute()
        else:
            print('Ошибка', validator.errors)