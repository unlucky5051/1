from dist.Model.Electrical_lines import *

class Electrical_lines_Controller():
    def add(self, cabinet):
        cabinet_id = Cabinet.select(Cabinet.id).where(Cabinet.name == cabinet)
        Electrical_lines.insert(cabinet_id = cabinet_id).execute()
