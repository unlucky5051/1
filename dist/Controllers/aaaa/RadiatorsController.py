from dist.Model.Radiators import *

radiators = Radiators

class Radiators_Controller():
    def __init__(self):
        self.__table = Radiators()

    def add_value(self, name, temperature_id, condition_id, cabinet_id):
        self.__table.insert(name = name, temperature_id = temperature_id, condition_id = condition_id, cabinet_id = cabinet_id).execute()

    def get(self):
        return Radiators.select().execute()

    def show(self, id):
        return Radiators.select(Radiators.id, Radiators.name, Radiators.temperature_id, Radiators.condition_id, Radiators.cabinet_id).where(Radiators.id == id).execute()

    def update_state(self, new_name, new_temperature_id, id):
        (Radiators.update({Radiators.name:new_name}).where(Radiators.id == id).execute(),
         Radiators.update({Radiators.temperature_id:new_temperature_id}).where(Radiators.id == id).execute())

    def delete_field(self, id):
        Radiators.delete().where(Radiators.id == id).execute()