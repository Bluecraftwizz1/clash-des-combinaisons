from tkinter import*
from PIL import ImageTk, Image
from functools import partial
import random
from Game import Game
from MySound import MySound
from WindowGame import WindowGame
from tkinter import messagebox

class WindowGenerateCard(Tk):

    def __init__(self, sound, card1=None, card2=None):
        super(WindowGenerateCard, self).__init__()
        self.sound = sound
        self.card1 = card1
        self.card2 = card2
        self.reset_labels()
        self.title("Pick Card")
        self.buttons = []
        self.pos = None
        self.player_number = 1
        self.generate_card()

    def reset_labels(self):
        labels = []
        for r in range(5):
            row = []
            for i in range(5):
                if (r + i) % 2 == 0:
                    color = 'white'
                else:
                    color = 'black'
                entry = Label(self, width="20", height="9", bg=color)
                entry.grid(row=r, column=i)
                row.append(entry)
            labels.append(row)
        self.labels = labels

    def generate_card(self):
        self.reset_labels()
        self.remove_buttons()

        text = "Player "+ str(self.player_number) + ", \n generate your card \n " + "Player " + str(3 - self.player_number) + ", \ndon't look !"
        button = Button(self, width="18", height="7", bg="yellow", text=text, command=self.pick_direction)
        button.grid(row=2, column=2)
        self.buttons.append(button)
        if self.player_number == 1:
            self.sound.play_player_blue_generate()
        else:
            self.sound.play_player_red_generate()


    def remove_buttons(self):
        for button in self.buttons:
            button.destroy()
        self.buttons = []

    def pick_direction(self):
        self.sound.play_sound_select()
        if self.player_number == 1:
            self.sound.play_blue_orient()
        else:
            self.sound.play_red_orient()
        self.remove_buttons()
        text = "player "+str(self.player_number)+" pick card"

        button = Button(self, width="18", height="7", bg="yellow", text=text, command=self.pick_direction)
        button.grid(row=2, column=1)
        self.buttons.append(button)

        button_val = Button(self, width="15", height="5", bg="yellow", text="validate \n(WRITE IT DOWN)", command=self.validate_card)
        button_val.grid(row=2, column=3)
        self.buttons.append(button_val)

        self.pos = generate_pos()
        self.update_card()

    def update_card(self):
        self.reset_labels()
        for i in range(len(self.labels)):
            if self.player_number== 1:
                color = "dodger blue"
            else:
                color="red"
            self.labels[i] = Label(self, width="20", height="9", bg=color)
            self.labels[i].grid(row=4 - (self.pos)[i][0], column=(self.pos)[i][1])
        button_val = Button(self, width="15", height="5", bg="yellow", text="validate \n(WRITE IT DOWN)",command=self.validate_card)
        button_val.grid(row=2, column=3)
        self.buttons.append(button_val)

        button_rotate = Button(self, width="15", height="5", bg="yellow", text="rotate",command=self.rotate)
        button_rotate.grid(row=2, column=1)
        self.buttons.append(button_rotate)

    def rotate(self):
        self.sound.play_sound_select()
        for i in range(len(self.pos)):
            center_before_rotation = [self.pos[i][0]-2,self.pos[i][1]-2]
            rotate_around_center = [center_before_rotation[1],-center_before_rotation[0]]
            new_point = [rotate_around_center[0]+2, rotate_around_center[1]+2]
            self.pos[i] = new_point
        self.update_card()

    def validate_card(self):
        self.sound.play_sound_select()
        if self.player_number == 1:
            self.card1 = self.pos
            print("player " + str(self.player_number))
            print(self.pos)
            self.player_number = 2
            self.generate_card()
        elif self.player_number == 2:
            self.card2 = self.pos
            print("player " + str(self.player_number) + " card validated")
            print(self.pos)
            self.destroy()
            window_game = WindowGame(self.sound, self.card1, self.card2)
            window_game.mainloop()

def generate_pos():
    pos = [[2,2]]
    boo = True
    for i in range(4):
        boo = True
        while (boo):
            m = int(random.random() * 25)
            x = m % 5
            y = int((m - x) / 5)
            new_pos = [x, y]
            if new_pos not in pos and new_pos != [2, 2]:
                boo = False
                pos.append(new_pos)
    return pos