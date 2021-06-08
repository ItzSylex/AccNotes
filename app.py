from tkinter import *
from tkinter.font import Font
import pyperclip


class AccNotes():

    def __init__(self):
        self.window = Tk()
        self.window.geometry("340x480")
        self.window.title("")
        self.window.resizable(False, False)

        self.click = True
        self.entry_list = []

        self.button_img = PhotoImage(file = f"imgs/copy_button.png")
        self.small_entry_img = PhotoImage(file = f"imgs/small_entry.png")
        self.big_entry_img = PhotoImage(file = f"imgs/big_entry.png")
        self.font = Font(
            family = "Arial Rounded MT Bold",
            size = 38,
            weight = "bold",
        )

        self.canvas = Canvas(
            self.window, bg = "white", height = 480, width = 340,
            bd = 0, highlightthickness = 0, relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)

        self.copy_button = Button(
            image = self.button_img, borderwidth = 0, relief = "flat",
            highlightthickness = 0, command = self.copy_button
        )

        self.copy_button.place(
            x = 35, y = 384,
            width = 270, height = 52
        )

        self.canvas.create_text(
            170.0, 60.0,
            text = "AccNotes",
            fill = "#262626",
            font = self.font)

        self.create_text()

    def copy_button(self):
        note = ""

        for i, entry in enumerate(self.entry_list):
            content = entry.get(1.0, END)

            if i == 0:
                note = note + f"Claim: {content.strip()} \n"
                entry.delete(1.0, END)

            elif i == 1:
                note = note + f"Resolution/issue: {content.strip()} \n"
                entry.delete(1.0, END)

            else:
                note = note + f"By: {content.strip()}"

        pyperclip.copy(note)

    def create_text(self):

        entry_details = {
            "claim": [107, 27, 121.5],
            "issue": [148, 182, 240],
            "name": [342, 27, 356.5]
        }

        for i, (name, details) in enumerate(entry_details.items()):
            name = Text(
                bd = 0, bg = "#5E3E71", highlightthickness = 0,
                insertbackground = 'white', fg = "#E8E8E8",
                font = "Montserrat 10", pady = 6, selectbackground = "#4C335B",
            )

            name.place(
                x = 45.0, y = details[0],
                width = 250.0,
                height = details[1]
            )

            self.entry_list.append(name)

            if i % 2 == 0:
                canvas_bg = self.canvas.create_image(
                    170.0, details[2], image = self.small_entry_img
                )
            else:
                canvas_bg = self.canvas.create_image(
                    170.0, details[2], image = self.big_entry_img
                )


app = AccNotes()
app.window.mainloop()
