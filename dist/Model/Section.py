from dist.Model.Base import *

class Section(Base):


    id = PrimaryKeyField(unique=True)
    name = CharField(unique=True, max_length=20, null=False)
    class Meta:
        db_table = 'Sections'

