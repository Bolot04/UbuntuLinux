import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Что вроде чего то!!)"
    page.theme_mode = ft.ThemeMode.LIGHT



    greeting_text = ft.Text(value="Hello, World")
    create_name = ft.TextField(label="Введите имя!")
    result_text = ft.Text()
    data_text = ft.Text(" ")

    greeting_history = []
    history_text = ft.Text("История приветсвий: ")


    #----- Переключатель темы от чегото на чтото!!) -----
    def toggle_theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            


        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        page.update()

    theme_button = ft.IconButton(
        icon=ft.Icons.BRIGHTNESS_7,
        tooltip="Сменить тему",
        on_click=toggle_theme
    )


    def on_submit(_):
        name = create_name.value
        time_str = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")
        # time_str = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")
        # save_to_db(name, time_str)
        # result_text.value = f"Имя: {name}"        

        if not name:
            greeting_text.value = "Введите корректное имя"
            result_text.value = ""
            page.update()
            return
        

        greeting_history.append(name)    

        create_name.value = ""
        print(greeting_history)

        data_text.value = f"Дата: {time_str}" 
        greeting_text.value = f"Hello, {name}"
        result_text.value = f"Имя сохраненно: {name}"
        page.update()



    def delet_history(_):
        if greeting_history:
            greeting_history.pop()
            result_text.value = "Deleted!!"
        else:
            result_text.value = "История не найдена!!!"
        page.update()


    delet_button = ft.ElevatedButton("Deleted", on_click=delet_history)

    page.add(
        greeting_text,
        ft.Row([
            create_name,
            ft.ElevatedButton("Send", on_click=on_submit),
            result_text,
            theme_button,
            delet_button
        ])
    )

ft.app(target=main, )




