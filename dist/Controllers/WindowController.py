from dist.Models.Window import Window

class WindowController():

    # Вывод всех записей
    def get(self):
        return Window.select().execute()

#     вывод окон кабинета
    def show_of_cabinet(self,cabinet_id):

        # return Window.get(Window.cabinet_id == cabinet_id)
        return Window.select().where(Window.cabinet_id == cabinet_id).execute()

#     функция проверки окрытия окна
#     словарь
    def window_state(self,cabinet_id):
        windows = []

        for row in self.show_of_cabinet(cabinet_id):
            # print(row.open_close, row.id, row.condition_id.position)
            windows.append({'id' : row.id ,
                       'open_close': row.open_close,
                       'position' : row.condition_id.position
                       })
        return windows



if __name__ == "__main__":
    win = WindowController()
    # for row in win.get():
    #     print(row. id, row.open_close, row.cabinet_id.name, row.condition_id.position)

    for row in win.window_state(1):
        print(row)