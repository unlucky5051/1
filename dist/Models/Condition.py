from dist.Models.Base import *

class Condition(Base):

    id = PrimaryKeyField(unique=True)
    position = IntegerField(unique=True)

    class Meta:
        db_table = 'Conditions'