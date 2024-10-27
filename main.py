import docxtpl as docx
import tkinter as tk
import sqlite3
import os
from tkinter import ttk
from tkinter import scrolledtext

class database:
    def __init__(self) -> None:
        self.con = sqlite3.connect("database.db")
        self.cur = self.con.cursor()

    def create_table(self):
        self.cur.execute("CREATE TABLE movie(title, year, score)")
    
    def retrieve_names(self):
        res = self.cur.execute("SELECT name FROM sqlite_master")
        files = res.fetchall()
        return files
    
    def retrieve_text(self, name):
        res = self.cur.execute(f"SELECT text FROM sqlite_master WHERE name='{name}'")
        res.fetchone()


def read_docx():
    pass

def write_docx(first_name, second_name, text):
    doc = docx.DocxTemplate("my_word_template.docx")
    context = { 'first_name' : f"{first_name}", 'second_name' : f"{second_name}", 'text' : f"{text}" }
    doc.render(context)
    doc.save("generated_doc.docx")


class UI:
    def __init__(self) -> None:
        self.r = tk.Tk()
        self.r.title('Text to docx')
        self.label = tk.Label(self.r, text="Edit this text to change the output file")
        self.label.pack()
        self.text_input = scrolledtext.ScrolledText(self.r)
        self.text_input.pack()
        self.button = tk.Button(self.r, text='Get text', width=25, command=self.get_text)
        self.button.pack()
        self.button = tk.Button(self.r, text='Stop', width=25, command=self.r.destroy)
        self.button.pack()
    
    def get_text(self):
        text = self.text_input.get("1.0", tk.END)
        print(text)

    def change_text(self, new_text):
        self.text_input.config(text=new_text)


if __name__ == "__main__":
    ui = UI()
    db = database()
    ui.r.mainloop()