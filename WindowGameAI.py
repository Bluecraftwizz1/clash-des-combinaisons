from tkinter import*
from PIL import ImageTk, Image
from functools import partial
from random import random
from Game import Game
from MySound import MySound
import time
from SimpleAI import SimpleAI
from Player import Player
from tkinter import messagebox

def generate_pos():
    pos = []
    boo = True
    for i in range(5):
        boo = True
        while (boo):
            m = int(random.random() * 25)
            x = m % 5
            y = int((m - x) / 5)
            new_pos = [x, y]
            if new_pos not in pos:
                boo = False
                pos.append(new_pos)
    return pos

class WindowGameAI(Tk):

    def __init__(self,sound,generate_window, card1=None, card2=None):
        self.sound = sound

        self.game = Game(self.sound)

        self.game.player1 = Player(None, [0,2], [0,0], [0,4], [0,1], [0,3])
        self.game.player2 = Player(None, [4,2], [4,0], [4,4], [4,1], [4,3])

        self.sound = sound
        self.score = 0

        self.generate_window = generate_window

        self.game.player1.goal = card1
        self.game.player2.goal = card2

        #self.game.player1.goal = generate_pos()
        #self.game.player2.goal = generate_pos()

        print("player1.goal = " +str(self.game.player1.goal))
        print("player2.goal = " +str(self.game.player2.goal))

        print(self.game.to_GUI())

        com_num = self.game.same_cards()
        # ("Number of common cards", "You have " + str(com_num) + " cards in common")
        if [2, 2] in self.game.player1.goal:
            color = 'dodger blue'
        else:
            color = 'white'
        entry = Label(self.generate_window, width="20", height="9",
                      text="You have " + str(com_num) + "\n positions in common", bg=color)
        entry.grid(row=2, column=2)
        self.generate_window.update()

        self.sound.com(com_num)
        time.sleep(2)

        self.generate_window.geometry("+0+100")

        super(WindowGameAI, self).__init__()
        self.geometry("+800+100")

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

        self.possible_clicks=[]

        self.img_player1_captain = ImageTk.PhotoImage(image=Image.open('images and sounds\\image1.png'),master=self)  # PIL solution
        self.img_player1_pilote1 = ImageTk.PhotoImage(image=Image.open('images and sounds\\image2.png'),master=self)  # PIL solution
        self.img_player1_pyramid1 = ImageTk.PhotoImage(image=Image.open('images and sounds\\image0.png'),master=self)  # PIL solution
        self.img_player2_pyramid1 = ImageTk.PhotoImage(image=Image.open('images and sounds\\image3.png'),master=self)  # PIL solution
        self.img_player2_pilot1 = ImageTk.PhotoImage(image=Image.open('images and sounds\\image4.png'),master=self)  # PIL solution
        self.img_player2_captain = ImageTk.PhotoImage(image=Image.open('images and sounds\\image5.png'),master=self)  # PIL solution


        self.player1_captain = Button(self, width="144", height="139", bg="dodger blue", text="player1_capitain",
                                 command=self.clicking_player1_captain, image=self.img_player1_captain)
        self.player1_captain.image=self.img_player1_captain


        self.player1_pyramid1 = Button(self, width="144", height="139", bg="dodger blue", text="player1_pyramid1",
                                  command=self.clicking_player1_pyramid1, image=self.img_player1_pyramid1)
        self.player1_pyramid1.image=self.img_player1_pyramid1


        self.player1_pyramid2 = Button(self, width="144", height="139", bg="dodger blue", text="player1_pyramid2",
                                  command=self.clicking_player1_pyramid2, image=self.img_player1_pyramid1)
        self.player1_pyramid2.image = self.img_player1_pyramid1


        self.player1_pilot1 = Button(self, width="144", height="139", bg="dodger blue", text="player1_pilot1",
                                command=self.clicking_player1_pilot1, image=self.img_player1_pilote1)
        self.player1_pilot1.image = self.img_player1_pilote1


        self.player1_pilot2 = Button(self, width="144", height="139", bg="dodger blue", text="player1_pilot2",
                                command=self.clicking_player1_pilot2, image=self.img_player1_pilote1)
        self.player1_pilot2.image = self.img_player1_pilote1


        self.player2_captain = Button(self, width="144", height="139", bg="red", text="player2_capitain",
                                 command=self.clicking_player2_captain, image=self.img_player2_captain)
        self.player2_captain.image = self.img_player2_captain


        self.player2_pyramid1 = Button(self, width="144", height="139", bg="red", text="player2_pyramid1",
                                  command=self.clicking_player2_pyramid1, image=self.img_player2_pyramid1)
        self.player2_pyramid1.image = self.img_player2_pyramid1


        self.player2_pyramid2 = Button(self, width="144", height="139", bg="red", text="player2_pyramid2",
                                  command=self.clicking_player2_pyramid2, image=self.img_player2_pyramid1)
        self.player2_pyramid2.image = self.img_player2_pyramid1


        self.player2_pilot1 = Button(self, width="144", height="139", bg="red", text="player2_pilot1",
                                command=self.clicking_player2_pilot1, image=self.img_player2_pilot1)
        self.player2_pilot1.image = self.img_player2_pilot1


        self.player2_pilot2 = Button(self, width="144", height="139", bg="red", text="player2_pilot2",
                                command=self.clicking_player2_pilot2, image=self.img_player2_pilot1)
        self.player2_pilot2.image = self.img_player2_pilot1


        self.player1_pions = [self.player1_captain, self.player1_pyramid1, self.player1_pyramid2, self.player1_pilot2, self.player1_pilot1]
        self.player2_pions = [self.player2_captain, self.player2_pyramid1, self.player2_pyramid2, self.player2_pilot2, self.player2_pilot1]

        self.update_GUI()

        self.AI = SimpleAI(self.game)

        if self.game.turn == 1:
            self.sound.play_blue_first()
        else:
            self.sound.play_red_first()
            self.AI.make_a_move()
            self.update_GUI()

        self.protocol("WM_DELETE_WINDOW", self.on_closing_game)

    def on_closing(self):
        self.sound.play_sound_select()
        del(self.game)
        self.destroy()

    def remove_previous_clicks(self):
        for button in self.possible_clicks:
            button.destroy()
        self.possible_clicks = []

    def clicking_player1_captain(self):
        self.sound.play_sound_select()
        self.remove_previous_clicks()
        self.possible_moves = self.game.player1.captain.generate_possible_moves(self.game.get_occupied())
        for x in self.possible_moves:
            if x in self.game.get_occupied():
                pion = self.game.who_there(x)
                if pion == self.game.player1.captain:
                    new_button = Button(self, width="144", height="139", bg="yellow", text="player1_capitain",
                                        command=partial(self.move_player1_captain_GUI, [x[0], x[1]]),
                                        image=self.img_player1_captain)
                if pion == self.game.player1.pyramid1 or pion == self.game.player1.pyramid2:
                    new_button = Button(self, width="144", height="139", bg="yellow", text="player1_pyramid",
                                        command=partial(self.move_player1_captain_GUI, [x[0], x[1]]),
                                        image=self.img_player1_pyramid1)
                if pion == self.game.player1.pilot1 or pion == self.game.player1.pilot2:
                    new_button = Button(self, width="144", height="139", bg="yellow", text="player1_capitain",
                                        command=partial(self.move_player1_captain_GUI, [x[0], x[1]]),
                                        image=self.img_player1_pilote1)
                if pion == self.game.player2.captain:
                    new_button = Button(self, width="144", height="139", bg="yellow", text="player2_capitain",
                                        command=partial(self.move_player1_captain_GUI, [x[0], x[1]]),
                                        image=self.img_player2_captain)
                if pion == self.game.player2.pyramid1 or pion == self.game.player2.pyramid2:
                    new_button = Button(self, width="144", height="139", bg="yellow", text="player2_pyramid",
                                        command=partial(self.move_player1_captain_GUI, [x[0], x[1]]),
                                        image=self.img_player2_pyramid1)
                if pion == self.game.player2.pilot1 or pion == self.game.player2.pilot2:
                    new_button = Button(self, width="144", height="139", bg="yellow", text="player2_capitain",
                                        command=partial(self.move_player1_captain_GUI, [x[0], x[1]]),
                                        image=self.img_player2_pilot1)
            else:
                new_button = Button(self, width="20", height="9", bg="yellow",
                                    command=partial(self.move_player1_captain_GUI, [x[0], x[1]]))
            new_button.grid(row=4 - x[0], column=x[1])
            self.possible_clicks.append(new_button)


    def clicking_player1_pyramid1(self):
        self.sound.play_sound_select()
        self.remove_previous_clicks()
        self.possible_moves = self.game.player1.pyramid1.generate_possible_moves(self.game.get_occupied())
        for x in self.possible_moves:
            new_button = Button(self, width="20", height="9", bg="yellow",command=partial(self.move_player1_pyramid1_GUI,[x[0],x[1]]))
            new_button.grid(row=4-x[0],column=x[1])
            self.possible_clicks.append(new_button)

    def clicking_player1_pyramid2(self):
        self.sound.play_sound_select()
        self.remove_previous_clicks()
        self.possible_moves = self.game.player1.pyramid2.generate_possible_moves(self.game.get_occupied())
        for x in self.possible_moves:
            new_button = Button(self, width="20", height="9", bg="yellow",command=partial(self.move_player1_pyramid2_GUI,[x[0],x[1]]))
            new_button.grid(row=4-x[0],column=x[1])
            self.possible_clicks.append(new_button)

    def clicking_player1_pilot1(self):
        self.sound.play_sound_select()
        self.remove_previous_clicks()
        self.possible_clicks.clear()
        self.possible_moves = self.game.player1.pilot1.generate_possible_moves(self.game.get_occupied())
        for x in self.possible_moves:
            new_button = Button(self, width="20", height="9", bg="yellow",command=partial(self.move_player1_pilot1_GUI,[x[0],x[1]]))
            new_button.grid(row=4-x[0],column=x[1])
            self.possible_clicks.append(new_button)

    def clicking_player1_pilot2(self):
        self.sound.play_sound_select()
        self.remove_previous_clicks()
        self.possible_moves = self.game.player1.pilot2.generate_possible_moves(self.game.get_occupied())
        for x in self.possible_moves:
            new_button = Button(self, width="20", height="9", bg="yellow",command=partial(self.move_player1_pilot2_GUI,[x[0],x[1]]))
            new_button.grid(row=4-x[0],column=x[1])
            self.possible_clicks.append(new_button)


    def clicking_player2_pyramid2(self):
        self.sound.play_sound_select()
        self.remove_previous_clicks()
        self.possible_moves = self.game.player2.pyramid2.generate_possible_moves(self.game.get_occupied())
        for x in self.possible_moves:
            new_button = Button(self, width="20", height="9", bg="yellow",command=partial(self.move_player2_pyramid2_GUI,[x[0],x[1]]))
            new_button.grid(row=4-x[0],column=x[1])
            self.possible_clicks.append(new_button)

    def clicking_player2_pyramid1(self):
        self.sound.play_sound_select()
        self.remove_previous_clicks()
        self.possible_moves = self.game.player2.pyramid1.generate_possible_moves(self.game.get_occupied())
        for x in self.possible_moves:
            new_button = Button(self, width="20", height="9", bg="yellow",command=partial(self.move_player2_pyramid1_GUI,[x[0],x[1]]))
            new_button.grid(row=4-x[0],column=x[1])
            self.possible_clicks.append(new_button)

    def clicking_player2_captain(self):
        self.sound.play_sound_select()
        self.remove_previous_clicks()
        self.possible_moves = self.game.player2.captain.generate_possible_moves(self.game.get_occupied())
        for x in self.possible_moves:
            if x in self.game.get_occupied():
                pion = self.game.who_there(x)
                if pion == self.game.player1.captain:
                    new_button = Button(self, width="144", height="139", bg="yellow", text="player1_capitain",
                                        command=partial(self.move_player2_captain_GUI, [x[0], x[1]]),
                                        image=self.img_player1_captain)
                if pion == self.game.player1.pyramid1 or pion == self.game.player1.pyramid2:
                    new_button = Button(self, width="144", height="139", bg="yellow", text="player1_pyramid",
                                        command=partial(self.move_player2_captain_GUI, [x[0], x[1]]),
                                        image=self.img_player1_pyramid1)
                if pion == self.game.player1.pilot1 or pion == self.game.player1.pilot2:
                    new_button = Button(self, width="144", height="139", bg="yellow", text="player1_capitain",
                                        command=partial(self.move_player2_captain_GUI, [x[0], x[1]]),
                                        image=self.img_player1_pilote1)
                if pion == self.game.player2.captain:
                    new_button = Button(self, width="144", height="139", bg="yellow", text="player2_capitain",
                                        command=partial(self.move_player2_captain_GUI, [x[0], x[1]]),
                                        image=self.img_player2_captain)
                if pion == self.game.player2.pyramid1 or pion == self.game.player2.pyramid2:
                    new_button = Button(self, width="144", height="139", bg="yellow", text="player2_pyramid",
                                        command=partial(self.move_player2_captain_GUI, [x[0], x[1]]),
                                        image=self.img_player2_pyramid1)
                if pion == self.game.player2.pilot1 or pion == self.game.player2.pilot2:
                    new_button = Button(self, width="144", height="139", bg="yellow", text="player2_capitain",
                                        command=partial(self.move_player2_captain_GUI, [x[0], x[1]]),
                                        image=self.img_player2_pilot1)
            else:
                new_button = Button(self, width="20", height="9", bg="yellow",
                                    command=partial(self.move_player2_captain_GUI, [x[0], x[1]]))
            new_button.grid(row=4 - x[0], column=x[1])
            self.possible_clicks.append(new_button)

    def clicking_player2_pilot1(self):
        self.sound.play_sound_select()
        self.remove_previous_clicks()
        self.possible_moves = self.game.player2.pilot1.generate_possible_moves(self.game.get_occupied())
        for x in self.possible_moves:
            new_button = Button(self, width="20", height="9", bg="yellow",  command=partial(self.move_player2_pilot1_GUI,[x[0],x[1]]))
            new_button.grid(row=4-x[0],column=x[1])
            self.possible_clicks.append(new_button)

    def clicking_player2_pilot2(self):
        self.sound.play_sound_select()
        self.remove_previous_clicks()
        self.possible_moves = self.game.player2.pilot2.generate_possible_moves(self.game.get_occupied())
        for x in self.possible_moves:
            new_button = Button(self, width="20", height="9", bg="yellow", command=partial(self.move_player2_pilot2_GUI,[x[0],x[1]]))
            new_button.grid(row=4-x[0],column=x[1])
            self.possible_clicks.append(new_button)

    def update_GUI(self):
        d = self.game.to_GUI()

        key = 'player1_captain'
        key1 = 'player1_pyramid1'
        key2 = 'player1_pyramid2'
        key3 = 'player1_pilot1'
        key4 = 'player1_pilot2'
        key5 = 'player2_captain'
        key6 = 'player2_pyramid1'
        key7 = 'player2_pyramid2'
        key8 = 'player2_pilot1'
        key9 = 'player2_pilot2'

        self.move_player1_captain(d[key][0], d[key][1])
        self.move_player1_pyramid1(d[key1][0], d[key1][1])
        self.move_player1_pyramid2(d[key2][0], d[key2][1])
        self.move_player1_pilot1(d[key3][0], d[key3][1])
        self.move_player1_pilot2(d[key4][0], d[key4][1])
        self.move_player2_captain(d[key5][0], d[key5][1])
        self.move_player2_pyramid1(d[key6][0], d[key6][1])
        self.move_player2_pyramid2(d[key7][0], d[key7][1])
        self.move_player2_pilot1(d[key8][0], d[key8][1])
        self.move_player2_pilot2(d[key9][0], d[key9][1])

        self.update()

        winner = self.game.winner()
        self.game_over(winner)

    def get_color(self,pion):
        x = pion.coord[0] + pion.coord[1]
        x = x % 2
        if x == 0:
            return "white"
        else:
            return "black"

    def move_player1_captain(self, x, y):
        xx = 4 - x
        self.player1_captain.grid(row=xx, column=y)
        self.player1_captain['bg'] = self.get_color(self.game.player1.captain)

    def move_player1_pyramid1(self, x, y):
        xx = 4 - x
        self.player1_pyramid1.grid(row=xx, column=y)
        self.player1_pyramid1['bg'] = self.get_color(self.game.player1.pyramid1)

    def move_player1_pyramid2(self, x, y):
        xx = 4 - x
        self.player1_pyramid2.grid(row=xx, column=y)
        self.player1_pyramid2['bg'] = self.get_color(self.game.player1.pyramid2)

    def move_player1_pilot1(self, x, y):
        xx = 4 - x
        self.player1_pilot1.grid(row=xx, column=y)
        self.player1_pilot1['bg'] = self.get_color(self.game.player1.pilot1)

    def move_player1_pilot2(self, x, y):
        xx = 4 - x
        self.player1_pilot2.grid(row=xx, column=y)
        self.player1_pilot2['bg'] = self.get_color(self.game.player1.pilot2)

    def move_player2_captain(self, x, y):
        xx = 4 - x
        self.player2_captain.grid(row=xx, column=y)
        self.player2_captain['bg'] = self.get_color(self.game.player2.captain)

    def move_player2_pyramid1(self, x, y):
        xx = 4 - x
        self.player2_pyramid1.grid(row=xx, column=y)
        self.player2_pyramid1['bg'] = self.get_color(self.game.player2.pyramid1)

    def move_player2_pyramid2(self, x, y):
        xx = 4 - x
        self.player2_pyramid2.grid(row=xx, column=y)
        self.player2_pyramid2['bg'] = self.get_color(self.game.player2.pyramid2)

    def move_player2_pilot1(self, x, y):
        xx = 4 - x
        self.player2_pilot1.grid(row=xx, column=y)
        self.player2_pilot1['bg'] = self.get_color(self.game.player2.pilot1)

    def move_player2_pilot2(self, x, y):
        xx = 4 - x
        self.player2_pilot2.grid(row=xx, column=y)
        self.player2_pilot2['bg'] = self.get_color(self.game.player2.pilot2)


    def move_player1_captain_GUI(self,x):
        if self.game.turn == 1:
            self.sound.play_move()
        else:
            self.sound.play_not_your_turn()
        self.game.move(self.game.player1.captain, x)
        self.remove_previous_clicks()
        self.update_GUI()
        self.update()
        winner = self.game.winner()
        self.game_over(winner)
        self.AI.make_a_move()
        self.update_GUI()

    def move_player1_pyramid1_GUI(self,x):
        if self.game.turn == 1:
            self.sound.play_move()
        else:
            self.sound.play_not_your_turn()
        self.game.move(self.game.player1.pyramid1, x)
        self.remove_previous_clicks()
        self.update_GUI()
        self.update()
        winner = self.game.winner()
        self.game_over(winner)
        self.AI.make_a_move()
        self.update_GUI()

    def move_player1_pyramid2_GUI(self,x):
        if self.game.turn == 1:
            self.sound.play_move()
        else:
            self.sound.play_not_your_turn()
        self.game.move(self.game.player1.pyramid2, x)
        self.remove_previous_clicks()
        self.update_GUI()
        self.update()
        winner = self.game.winner()
        self.game_over(winner)
        self.AI.make_a_move()
        self.update_GUI()

    def move_player1_pilot1_GUI(self,x):
        if self.game.turn == 1:
            self.sound.play_move()
        else:
            self.sound.play_not_your_turn()
        self.game.move(self.game.player1.pilot1, x)
        self.remove_previous_clicks()
        self.update_GUI()
        self.update()
        winner = self.game.winner()
        self.game_over(winner)
        self.AI.make_a_move()
        self.update_GUI()

    def move_player1_pilot2_GUI(self,x):
        if self.game.turn == 1:
            self.sound.play_move()
        else:
            self.sound.play_not_your_turn()
        self.game.move(self.game.player1.pilot2, x)
        self.remove_previous_clicks()
        self.update_GUI()
        self.update()
        winner = self.game.winner()
        self.game_over(winner)
        self.AI.make_a_move()
        self.update_GUI()

    def move_player2_pyramid2_GUI(self,x):
        if self.game.turn == 2:
            self.sound.play_move()
        else:
            self.sound.play_not_your_turn()
        self.game.move(self.game.player2.pyramid2, x)
        self.remove_previous_clicks()
        self.update_GUI()
        winner = self.game.winner()
        self.game_over(winner)


    def move_player2_pyramid1_GUI(self,x):
        if self.game.turn == 2:
            self.sound.play_move()
        else:
            self.sound.play_not_your_turn()
        self.game.move(self.game.player2.pyramid1, x)
        self.remove_previous_clicks()
        self.update_GUI()
        winner = self.game.winner()
        self.game_over(winner)

    def move_player2_captain_GUI(self,x):
        if self.game.turn == 2:
            self.sound.play_move()
        else:
            self.sound.play_not_your_turn()
        self.game.move(self.game.player2.captain, x)
        self.remove_previous_clicks()
        self.update_GUI()
        winner = self.game.winner()
        self.game_over(winner)

    def move_player2_pilot1_GUI(self,x):
        if self.game.turn == 2:
            self.sound.play_move()
        else:
            self.sound.play_not_your_turn()
        self.game.move(self.game.player2.pilot1, x)
        self.remove_previous_clicks()
        self.update_GUI()
        winner = self.game.winner()
        self.game_over(winner)

    def move_player2_pilot2_GUI(self,x):
        if self.game.turn == 2:
            self.sound.play_move()
        else:
            self.sound.play_not_your_turn()
        self.game.move(self.game.player2.pilot2, x)
        self.remove_previous_clicks()
        self.update_GUI()
        winner = self.game.winner()
        self.game_over(winner)


    def on_closing_game(self):
        self.generate_window.destroy()
        self.destroy()

    def game_over(self,winner):
        if winner != None:
            if winner == 1:
                print("You won")
                time.sleep(1)
                color = 'dodger blue'
                self.sound.you_won()
            if winner == 2:
                print("You lose")
                time.sleep(1)
                color = 'red'
                self.sound.you_lose()
            if winner == 0:
                print("both players won !")
                color = 'purple'
                self.sound.you_won()

            self.remove_previous_clicks()
            self.update()

            time.sleep(.2)
            #if winner == 1 or winner == 0:
            if self.sound.sound_effects:
                self.sound.victoire()


            labels = []
            for r in range(5):
                row = []
                for i in range(5):
                    entry = Label(self, width="21", height="10", bg=color)
                    if r % 2 == 0:
                        entry.grid(row=r, column=i)
                    else:
                        entry.grid(row=r, column=4 - i)
                    row.append(entry)
                    time.sleep(0.05)
                    self.update()
                labels.append(row)

            time.sleep(0.6)

            self.generate_window.destroy()
            self.destroy()
