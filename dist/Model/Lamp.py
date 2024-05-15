from peewee import PrimaryKeyField

from dist.Model.Base import *
from dist.Model.Section import *
from dist.Model.Cabinet import *

class Lamp(Base):
    id = PrimaryKeyField(unique=True)
    state = BooleanField(null=False,default = 0)
    section_id = ForeignKeyField(Section)
    cabinet_id = ForeignKeyField(Cabinet)

    class Meta:
        db_table = 'Lamps'