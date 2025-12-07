import flet as ft
from datetime import datetime
import sqlite3

def create_db():
    conn = sqlite3.connect("user_register_time.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        timestamp TEXT                      
                   )
    """)
    conn.commit()
    conn.close()


def save_to_db(name: str, timestamp: str):
    conn = sqlite3.connect("user_register_time.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, timestamp) VALUES (?, ?)", (name, timestamp))
    conn.commit()
    conn.close()


def main(page: ft.Page):
    page.title = "Что вроде чего то!!)"
    page.theme_mode = ft.ThemeMode.LIGHT



    greeting_text = ft.Text(value="Hello, World")
    create_name = ft.TextField(label="Введите имя!")
    result_text = ft.Text()

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
        # time_str = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")
        # save_to_db(name, time_str)
        # result_text.value = f"Имя: {name}"

        if not name:
            greeting_text.value = "Введите корректное имя"
            result_text.value = ""
            page.update()
            return

        time_str = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")
        save_to_db(name, time_str)


        greeting_text.value = f"Hello, {name}"
        result_text.value = f"Имя сохраненно: {name}"
        page.update()

    page.add(
        greeting_text,
        create_name,
        ft.ElevatedButton("Отправить", on_click=on_submit),
        result_text,
        theme_button
    )

create_db()

ft.app(target=main, )




