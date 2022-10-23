from tkinter import *
import random

def next_turn():
    print("next turn function")

def print_textturn(pl):
    text_turn = "Ход "
    if pl == "x":
        text_turn = text_turn + "крестиков"
    else:
        text_turn = text_turn + "ноликов"
    return text_turn

def new_game():
    global player
    player = random.choice(players)
    label.config(text=print_textturn(player))

    for row in range(3):
        for column in range(3):
            buttons[row, column].config(text="", bg="#F0F0F0")


# Код визуала и игры

window = Tk()
window.title("Крестики нолики")

players = ["x", "o"]
player = random.choice(players)

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=print_textturn(player), font=('calibri', 40))
label.pack(side="top")

reset_button = Button(text="рестарт", font=('calibri', 40), bg="#f8f8f8", command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(
            frame,
            text="",
            font=('calibri', 40),
            width=5, height=3,
            command= lambda row=row, column=column: next_turn(row, column)
        )
        buttons[row][column].grid(row=row, column=column)

window.mainloop()


