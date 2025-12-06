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
    create_name = ft.TextField(label="Введите имя!")
    result_text = ft.Text()


    def on_submit(_):
        name = create_name.value
        time_str = datetime.now().strftime("%Y:%m:%d - %H:%M:%S")
        save_to_db(name, time_str)
        result_text.value = f"Имя: {name}"
        page.update()

    page.add(
        create_name,
        ft.ElevatedButton("Отправить", on_click=on_submit),
        result_text
    )

create_db()

ft.app(target=main)




