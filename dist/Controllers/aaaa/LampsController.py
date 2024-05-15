from dist.Model.Lamps import *

lamps = Lamps
class Lamps_Controller():
    def __init__(self):
        self.__table = Lamps()

    def add_value(self, state, section_id, cabinet_id):
        self.__table.insert(state = state, section_id = section_id, cabinet_id = cabinet_id).execute()

    def get(self):
        return Lamps.select().execute()

    def show(self, id):
        return Lamps.select(Lamps.id, Lamps.section_id, Lamps.cabinet_id, Lamps.state).where(Lamps.id == id).execute()

    def update_state(self, new_state, id):
        Lamps.update({Lamps.state:new_state}).where(Lamps.id == id).execute()

    def delete_field(self, id):
        Lamps.delete().where(Lamps.id == id).execute()