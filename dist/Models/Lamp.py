from dist.Models.Base import *
from dist.Models.Cabinet import Cabinet
from dist.Models.Section import Section


class Lamp(Base):
    id = PrimaryKeyField(unique=True)
    state = BooleanField(null=False,default = 0)
    seсtion_id = ForeignKeyField(Section)
    cabinet_id = ForeignKeyField(Cabinet)

    class Meta:
        db_table = 'Lamps'