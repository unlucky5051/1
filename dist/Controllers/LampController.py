from dist.Models.Lamp import Lamp
from dist.Models.Cabinet import Cabinet
from dist.Models.Section import Section

class LampController():

    def get(self):
        return Lamp.select()

    def print_get(self):
        for fields in self.get():
            print(fields.state, fields.seсtion_id.name,fields.cabinet_id.name,fields.cabinet_id.department)

    # вывод одной записи (строки) из таблицы

    def show(self, arg_id):
        query = Lamp.get(Lamp.id == arg_id)
        print('Состояние лампы',query.state,'Имя секции',query.seсtion_id.name,'Кабинет:', query.cabinet_id.name)

    # метод вывода состояния секций по cabinet_id
    def show_lamps(self,cabinet_id):
        return Lamp.select().where(Lamp.cabinet_id == cabinet_id)



    def show_setion(self,seсtion_id, cabinet_id):

        return Lamp.select().where(Lamp.cabinet_id == cabinet_id and Lamp.seсtion_id == seсtion_id).execute()

    # Добавить по id Кабинета и Секции
    def add(self,section,cabinet):
        Lamp.create(seсtion_id = section, cabinet_id = cabinet)

    # Добавить по name Кабинета и Секции

    def add_2(self,section, cabinet):
        section_id = Section.get(Section.name == section).id
        cabinet_id = Cabinet.get(Cabinet.name == cabinet).id

        Lamp.create(seсtion_id=section_id,cabinet_id=cabinet_id)
        print('Лампа добавлена')

    # Добавить несколько записей
    def add_many(self,data):
        Lamp.insert_many(data).execute()

    # Обновление пособ №1 save()
    # def update_One(self,arg_id, arg_state):
    #     lamp = Lamp.get(Lamp.id==arg_id) #создание из выбранной записи по id объекта
    #     lamp.state = arg_state #изменяем у выбранного объекта занчение состояния
    #     lamp.save() # c помощью функции save() обновляем запись

    def update_one(self,id,new_state):
        Lamp.update({Lamp.state:new_state}).where(Lamp.id == id).execute()

    # Обновление пособ №2 update()

    def update_Two(self,arg_id,arg_state):
        Lamp.update(state = arg_state).where(Lamp.id == arg_id).execute()

    def power_off_all(self,cabinet_id,arg_state):

        Lamp.update(state = arg_state).where(Lamp.cabinet_id == cabinet_id).execute()

    # метод который меняет состояние ламп опредёллённой секции определённого кабинета
    def power_off_section(self,cabinet_id,arg_state,seсtion_id):

        Lamp.update(state=arg_state).where(Lamp.cabinet_id == cabinet_id and Lamp.seсtion_id == seсtion_id).execute()

    # Если включена хотя бы одна лампа кабинета выводит True
    def state_of_lamps(self, cabinet_id):
        state = False
        #  в цикле использую метод show_lamps(), который выводит информацию о лампе нужного кабинета
        for row in self.show_lamps(cabinet_id):
            if row.state:#row.state == True
                state=True
        return state
    # метод который определяет есть ли включённая лампа в секции
    def state_of_lamps_section(self,cabinet_id, section_id):
        state = False
        for row in self.show_setion(section_id,cabinet_id):
            if row.state:
                state = True
        return state
    # метод вывода secton_id в виде списка
    def list_section(self,cabinet_id):
        list = []
        query = Lamp.select(Lamp.seсtion_id).distinct().where(Lamp.cabinet_id == cabinet_id).execute()
        for row in query:
            list.append(row.seсtion_id.id)
        return list


    def list_section_id(self,cabinet_id):
        list = []
        query = Lamp.select(Lamp.seсtion_id).distinct().where(Lamp.cabinet_id == cabinet_id).execute()
        for section in query:

            list.append(section.seсtion_id.id)
        return list



if __name__ == "__main__":

    lamp = LampController()
    print(lamp.state_of_lamps(1))
    lamp.power_off_all(1,1)
    print(lamp.state_of_lamps(1))
    # lamp.power_off_section(18,True,4)
    # print(lamp.state_of_lamps_section(18,4))

    # lamp.list_section_id(18)
    # print(lamp.list_section_id(1)[0])
    # print(lamp.list_section_id(1)[1])
    # print(lamp.list_section(1))
    # print(lamp.list_section(1))
    # print(lamp.list_section(15))
