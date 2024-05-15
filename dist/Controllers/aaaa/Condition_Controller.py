from dist.Model.Condition import *

class Condition_Controller():
    def add_value(self, position):
        self.__table.insert(position=position).execute()
    def get(self):
        return Conditions.select().execute
    def show(self, position):
        return Conditions.select(Conditions.position).where(Conditions.id == id).execute()