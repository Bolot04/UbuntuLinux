import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Что вроде чего то!!)"
    page.theme_mode = ft.ThemeMode.LIGHT



    greeting_text = ft.Text(value="Hello, World")
    create_name = ft.TextField(label="Введите имя!")
    result_text = ft.Text()
    data_text = ft.Text(" ")

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

        data_text.value = f"Дата: {time_str}" 

        if not name:
            greeting_text.value = "Введите корректное имя"
            result_text.value = ""
            page.update()
            return


        greeting_text.value = f"Hello, {name}"
        result_text.value = f"Имя сохраненно: {name}"
        page.update()

    page.add(
        greeting_text,
        create_name,
        ft.ElevatedButton("Отправить", on_click=on_submit),
        result_text,
        data_text,
        theme_button
    )

ft.app(target=main, )




