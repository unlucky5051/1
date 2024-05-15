from dist.Model.Motion_Sensors import *

motion = MotionSensor
class Motion_SensorsController():
    def __init__(self):
        self.__table = MotionSensor()

    def add_value(self, name, position, cabinet_id):
        self.__table.insert(name = name, position = position, cabinet_id = cabinet_id).execute()

    def get(self):
        return MotionSensor.select().execute()

    def show(self, id):
        return MotionSensor.select(MotionSensor.id, MotionSensor.name, MotionSensor.position, MotionSensor.cabinet_id).where(MotionSensor.id == id).execute()

    def update_state(self, new_position, id):
        MotionSensor.update({MotionSensor.position:new_position}).where(MotionSensor.id == id).execute()

    def delete_field(self, id):
        MotionSensor.delete().where(MotionSensor.id == id).execute()