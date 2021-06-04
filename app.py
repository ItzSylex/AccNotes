from tkinter import *


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

        self.canvas = Canvas(
            self.window, bg = "#151515", height = 480, width = 340,
            bd = 0, highlightthickness = 0, relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)

        self.copy_button = Button(
            image = self.button_img, borderwidth = 0, relief = "flat",
            highlightthickness = 0, command = self.copy_button
        )

        self.copy_button.place(
            x = 35, y = 429,
            width = 270, height = 29
        )

        self.canvas.create_text(
            170.0, 55.0,
            text = "AccNotes",
            fill = "#ffffff",
            font = 'Montserrat 38 bold')

        self.create_entry()

    def copy_button(self):
        pass

        # Loop tru self.entry_list and use the get() method

    def create_entry(self):

        entry_details = {
            "claim": [152, 27, 166.5],
            "issue": [193, 82, 235],
            "name": [387, 27, 401.5],
            "resolution": [290, 82, 332]
        }

        for i, (name, details) in enumerate(entry_details.items()):
            name = Text(
                bd = 0, bg = "#343c50", highlightthickness = 0,
                insertbackground = '#ffffff', fg = "#979797",
                font = "Montserrat 10", pady = 6
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
