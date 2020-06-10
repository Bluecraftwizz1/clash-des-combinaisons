from tkinter import*
from Game import Game
from PIL import ImageTk, Image
from functools import partial
import random
from winsound import *


sound_select = lambda: PlaySound(r'C:\Users\kael chiche the bada\PycharmProjects\Game_with_Val\game extra\sounds\select', SND_ASYNC)
sound_move = lambda: PlaySound(r'C:\Users\kael chiche the bada\PycharmProjects\Game_with_Val\game extra\sounds\move', SND_ASYNC)
sound_not_your_turn = lambda: PlaySound(r'C:\Users\kael chiche the bada\PycharmProjects\Game_with_Val\game extra\sounds\not_your_turn',SND_ASYNC)

card1 = None
card2 = None
labels = [None, None, None, None]

def generate_card(player_number):
    button = Button(card_Window, width="15", height="5", bg="yellow", text="rotate", command=partial(rotate,player_number))
    button.grid(row=2, column=1)

    global labels
    if labels[0] != None:
        for x in labels:
            x.destroy()
    print("player "+str(player_number)+" pick card")
    button = Button(card_Window, width="15", height="5", bg="yellow", text="validate", command=partial(validate_card, player_number))
    button.grid(row=2, column=3)
    global pos
    pos = generate_pos()

    update_card(player_number)


def update_card(player_num):
    if labels[0] != None:
        for x in labels:
            x.destroy()
    for i in range(len(labels)):
        labels[i] = Label(card_Window, width="20", height="9", bg="gray50")
        labels[i].grid(row=4 - pos[i][0], column=pos[i][1])
    button = Button(card_Window, width="15", height="5", bg="yellow", text="validate",command=partial(validate_card,player_num))
    button.grid(row=2, column=3)

def generate_pos():
    pos = []
    boo = True
    for i in range(4):
        boo = True
        while (boo):
            m = int(random.random() * 25)
            x = m % 5
            y = int((m - x) / 5)
            new_pos = [x, y]
            if new_pos not in pos and new_pos != [2,2]:
                boo = False
                pos.append(new_pos)
    return pos

def rotate(player_num):
    for i in range(len(pos)):
        center_before_rotation = [pos[i][0]-2,pos[i][1]-2]
        rotate_around_center = [center_before_rotation[1],-center_before_rotation[0]]
        new_point = [rotate_around_center[0]+2, rotate_around_center[1]+2]
        pos[i] = new_point
    update_card(player_num)

def validate_card(player_number):
    global pos
    if player_number == 1:
        global card1
        card1 = pos
        print("player " + str(player_number) + " card validated")
        generate_card(2)
    elif player_number == 2:
        global card2
        card2 = pos
        print("player " + str(player_number) + " card validated")
        card_Window.destroy()

card_Window = Tk()


c40= Label(card_Window,width="20",height="9",bg="white")
c41= Label(card_Window,width="20",height="9",bg="black")
c42= Label(card_Window,width="20",height="9",bg="white")
c43= Label(card_Window,width="20",height="9",bg="black")
c44= Label(card_Window,width="20",height="9",bg="white")
c34= Label(card_Window,width="20",height="9",bg="black")
c33= Label(card_Window,width="20",height="9",bg="white")
c32= Label(card_Window,width="20",height="9",bg="black")
c31= Label(card_Window,width="20",height="9",bg="white")
c30= Label(card_Window,width="20",height="9",bg="black")
c20= Label(card_Window,width="20",height="9",bg="white")
c21= Label(card_Window,width="20",height="9",bg="black")
c22= Label(card_Window,width="20",height="9",bg="gray50")
c23= Label(card_Window,width="20",height="9",bg="black")
c24= Label(card_Window,width="20",height="9",bg="white")
c14= Label(card_Window,width="20",height="9",bg="black")
c13= Label(card_Window,width="20",height="9",bg="white")
c12= Label(card_Window,width="20",height="9",bg="black")
c11= Label(card_Window,width="20",height="9",bg="white")
c10= Label(card_Window,width="20",height="9",bg="black")
c00= Label(card_Window,width="20",height="9",bg="white")
c01= Label(card_Window,width="20",height="9",bg="black")
c02= Label(card_Window,width="20",height="9",bg="white")
c03= Label(card_Window,width="20",height="9",bg="black")
c04= Label(card_Window,width="20",height="9",bg="white")

c40.grid(row=0,column=0)
c41.grid(row=0,column=1)
c42.grid(row=0,column=2)
c43.grid(row=0,column=3)
c44.grid(row=0,column=4)
c34.grid(row=1,column=4)
c33.grid(row=1,column=3)
c32.grid(row=1,column=2)
c31.grid(row=1,column=1)
c30.grid(row=1,column=0)
c20.grid(row=2,column=0)
c21.grid(row=2,column=1)
c22.grid(row=2,column=2)
c23.grid(row=2,column=3)
c24.grid(row=2,column=4)
c14.grid(row=3,column=4)
c13.grid(row=3,column=3)
c12.grid(row=3,column=2)
c11.grid(row=3,column=1)
c10.grid(row=3,column=0)
c00.grid(row=4,column=0)
c01.grid(row=4,column=1)
c02.grid(row=4,column=2)
c03.grid(row=4,column=3)
c04.grid(row=4,column=4)

generate_card(1)

card_Window.mainloop()

my_Window = Tk()

print("here")

if card1 ==None or card2 == None:
    exit()

card1.append([2,2])
card2.append([2,2])

game = Game()
game.player1.goal = card1
game.player2.goal = card2

print("player1.goal = " +str(game.player1.goal))
print("player2.goal = " +str(game.player2.goal))


c40= Label(my_Window,width="20",height="9",bg="white")
c41= Label(my_Window,width="20",height="9",bg="black")
c42= Label(my_Window,width="20",height="9",bg="white")
c43= Label(my_Window,width="20",height="9",bg="black")
c44= Label(my_Window,width="20",height="9",bg="white")

c34= Label(my_Window,width="20",height="9",bg="black")
c33= Label(my_Window,width="20",height="9",bg="white")
c32= Label(my_Window,width="20",height="9",bg="black")
c31= Label(my_Window,width="20",height="9",bg="white")
c30= Label(my_Window,width="20",height="9",bg="black")

c20= Label(my_Window,width="20",height="9",bg="white")
c21= Label(my_Window,width="20",height="9",bg="black")
c22= Label(my_Window,width="20",height="9",bg="white")
c23= Label(my_Window,width="20",height="9",bg="black")
c24= Label(my_Window,width="20",height="9",bg="white")

c14= Label(my_Window,width="20",height="9",bg="black")
c13= Label(my_Window,width="20",height="9",bg="white")
c12= Label(my_Window,width="20",height="9",bg="black")
c11= Label(my_Window,width="20",height="9",bg="white")
c10= Label(my_Window,width="20",height="9",bg="black")

c00= Label(my_Window,width="20",height="9",bg="white")
c01= Label(my_Window,width="20",height="9",bg="black")
c02= Label(my_Window,width="20",height="9",bg="white")
c03= Label(my_Window,width="20",height="9",bg="black")
c04= Label(my_Window,width="20",height="9",bg="white")


c40.grid(row=0,column=0)
c41.grid(row=0,column=1)
c42.grid(row=0,column=2)
c43.grid(row=0,column=3)
c44.grid(row=0,column=4)

c34.grid(row=1,column=4)
c33.grid(row=1,column=3)
c32.grid(row=1,column=2)
c31.grid(row=1,column=1)
c30.grid(row=1,column=0)

c20.grid(row=2,column=0)
c21.grid(row=2,column=1)
c22.grid(row=2,column=2)
c23.grid(row=2,column=3)
c24.grid(row=2,column=4)

c14.grid(row=3,column=4)
c13.grid(row=3,column=3)
c12.grid(row=3,column=2)
c11.grid(row=3,column=1)
c10.grid(row=3,column=0)

c00.grid(row=4,column=0)
c01.grid(row=4,column=1)
c02.grid(row=4,column=2)
c03.grid(row=4,column=3)
c04.grid(row=4,column=4)

possible_clicks=[]


def remove_previous_clicks():
    for button in possible_clicks:
        button.destroy()

def clicking_player1_captain():
    sound_select()
    remove_previous_clicks()
    possible_clicks.clear()
    possible_moves = game.player1.captain.generate_possible_moves(game.get_occupied())
    for x in possible_moves:
        if x in game.get_occupied():
            pion = game.who_there(x)
            if pion == game.player1.captain:
                new_button = Button(my_Window, width="144", height="139", bg="yellow", text="player1_capitain", command=partial(move_player1_captain_GUI, [x[0], x[1]]), image=img_player1_captain)
            if pion == game.player1.pyramid1 or pion == game.player1.pyramid2:
                new_button = Button(my_Window, width="144", height="139", bg="yellow", text="player1_pyramid", command=partial(move_player1_captain_GUI, [x[0], x[1]]), image=img_player1_pyramid1)
            if pion == game.player1.pilot1 or pion == game.player1.pilot2:
                new_button = Button(my_Window, width="144", height="139", bg="yellow", text="player1_capitain", command=partial(move_player1_captain_GUI, [x[0], x[1]]), image=img_player1_pilote1)
            if pion == game.player2.captain:
                new_button = Button(my_Window, width="144", height="139", bg="yellow", text="player2_capitain", command=partial(move_player1_captain_GUI, [x[0], x[1]]), image=img_player2_captain)
            if pion == game.player2.pyramid1 or pion == game.player2.pyramid2:
                new_button = Button(my_Window, width="144", height="139", bg="yellow", text="player2_pyramid", command=partial(move_player1_captain_GUI, [x[0], x[1]]), image=img_player2_pyramid1)
            if pion == game.player2.pilot1 or pion == game.player2.pilot2:
                new_button = Button(my_Window, width="144", height="139", bg="yellow", text="player2_capitain", command=partial(move_player1_captain_GUI, [x[0], x[1]]), image=img_player2_pilot1)
        else:
            new_button = Button(my_Window, width="20", height="9", bg="yellow", command=partial(move_player1_captain_GUI,[x[0],x[1]]))
        new_button.grid(row=4-x[0],column=x[1])
        possible_clicks.append(new_button)

def clicking_player1_pyramid1():
    sound_select()
    remove_previous_clicks()
    possible_clicks.clear()
    possible_moves = game.player1.pyramid1.generate_possible_moves(game.get_occupied())
    for x in possible_moves:
        new_button = Button(my_Window, width="20", height="9", bg="yellow",command=partial(move_player1_pyramid1_GUI,[x[0],x[1]]))
        new_button.grid(row=4-x[0],column=x[1])
        possible_clicks.append(new_button)

def clicking_player1_pyramid2():
    sound_select()
    remove_previous_clicks()
    possible_clicks.clear()
    possible_moves = game.player1.pyramid2.generate_possible_moves(game.get_occupied())
    for x in possible_moves:
        new_button = Button(my_Window, width="20", height="9", bg="yellow",command=partial(move_player1_pyramid2_GUI,[x[0],x[1]]))
        new_button.grid(row=4-x[0],column=x[1])
        possible_clicks.append(new_button)

def clicking_player1_pilot1():
    sound_select()
    remove_previous_clicks()
    possible_clicks.clear()
    possible_moves = game.player1.pilot1.generate_possible_moves(game.get_occupied())
    for x in possible_moves:
        new_button = Button(my_Window, width="20", height="9", bg="yellow",command=partial(move_player1_pilot1_GUI,[x[0],x[1]]))
        new_button.grid(row=4-x[0],column=x[1])
        possible_clicks.append(new_button)

def clicking_player1_pilot2():
    sound_select()
    remove_previous_clicks()
    possible_clicks.clear()
    possible_moves = game.player1.pilot2.generate_possible_moves(game.get_occupied())
    for x in possible_moves:
        new_button = Button(my_Window, width="20", height="9", bg="yellow",command=partial(move_player1_pilot2_GUI,[x[0],x[1]]))
        new_button.grid(row=4-x[0],column=x[1])
        possible_clicks.append(new_button)


def clicking_player2_pyramid2():
    sound_select()
    remove_previous_clicks()
    possible_clicks.clear()
    possible_moves = game.player2.pyramid2.generate_possible_moves(game.get_occupied())
    for x in possible_moves:
        new_button = Button(my_Window, width="20", height="9", bg="yellow",command=partial(move_player2_pyramid2_GUI,[x[0],x[1]]))
        new_button.grid(row=4-x[0],column=x[1])
        possible_clicks.append(new_button)

def clicking_player2_pyramid1():
    sound_select()
    remove_previous_clicks()
    possible_clicks.clear()
    possible_moves = game.player2.pyramid1.generate_possible_moves(game.get_occupied())
    for x in possible_moves:
        new_button = Button(my_Window, width="20", height="9", bg="yellow",command=partial(move_player2_pyramid1_GUI,[x[0],x[1]]))
        new_button.grid(row=4-x[0],column=x[1])
        possible_clicks.append(new_button)

def clicking_player2_captain():
    sound_select()
    remove_previous_clicks()
    possible_clicks.clear()
    possible_moves = game.player2.captain.generate_possible_moves(game.get_occupied())
    for x in possible_moves:
        if x in game.get_occupied():
            pion = game.who_there(x)
            if pion == game.player1.captain:
                new_button = Button(my_Window, width="144", height="139", bg="yellow", text="player1_capitain",
                                    command=partial(move_player2_captain_GUI, [x[0], x[1]]), image=img_player1_captain)
            if pion == game.player1.pyramid1 or pion == game.player1.pyramid2:
                new_button = Button(my_Window, width="144", height="139", bg="yellow", text="player1_pyramid",
                                    command=partial(move_player2_captain_GUI, [x[0], x[1]]), image=img_player1_pyramid1)
            if pion == game.player1.pilot1 or pion == game.player1.pilot2:
                new_button = Button(my_Window, width="144", height="139", bg="yellow", text="player1_capitain",
                                    command=partial(move_player2_captain_GUI, [x[0], x[1]]), image=img_player1_pilote1)
            if pion == game.player2.captain:
                new_button = Button(my_Window, width="144", height="139", bg="yellow", text="player2_capitain",
                                    command=partial(move_player2_captain_GUI, [x[0], x[1]]), image=img_player2_captain)
            if pion == game.player2.pyramid1 or pion == game.player2.pyramid2:
                new_button = Button(my_Window, width="144", height="139", bg="yellow", text="player2_pyramid",
                                    command=partial(move_player2_captain_GUI, [x[0], x[1]]), image=img_player2_pyramid1)
            if pion == game.player2.pilot1 or pion == game.player2.pilot2:
                new_button = Button(my_Window, width="144", height="139", bg="yellow", text="player2_capitain",
                                    command=partial(move_player2_captain_GUI, [x[0], x[1]]), image=img_player2_pilot1)
        else:
            new_button = Button(my_Window, width="20", height="9", bg="yellow",
                                command=partial(move_player2_captain_GUI, [x[0], x[1]]))
        new_button.grid(row=4-x[0],column=x[1])
        possible_clicks.append(new_button)

def clicking_player2_pilot1():
    sound_select()
    remove_previous_clicks()
    possible_clicks.clear()
    possible_moves = game.player2.pilot1.generate_possible_moves(game.get_occupied())
    for x in possible_moves:
        new_button = Button(my_Window, width="20", height="9", bg="yellow", command=partial(move_player2_pilot1_GUI,[x[0],x[1]]))
        new_button.grid(row=4-x[0],column=x[1])
        possible_clicks.append(new_button)

def clicking_player2_pilot2():
    sound_select()
    remove_previous_clicks()
    possible_clicks.clear()
    possible_moves = game.player2.pilot2.generate_possible_moves(game.get_occupied())
    for x in possible_moves:
        new_button = Button(my_Window, width="20", height="9", bg="yellow", command=partial(move_player2_pilot2_GUI,[x[0],x[1]]))
        new_button.grid(row=4-x[0],column=x[1])
        possible_clicks.append(new_button)

def move_player1_captain_GUI(x):
    if game.turn == 1:
        sound_move()
    else:
        sound_not_your_turn()
    game.move(game.player1.captain, x)
    d = game.to_GUI()
    remove_previous_clicks()
    possible_clicks.clear()
    update_GUI(d)
    winner = game.winner()
    game_over(winner)

def move_player1_pyramid1_GUI(x):
    if game.turn == 1:
        sound_move()
    else:
        sound_not_your_turn()
    game.move(game.player1.pyramid1, x)
    d = game.to_GUI()
    remove_previous_clicks()
    possible_clicks.clear()
    update_GUI(d)
    winner = game.winner()
    game_over(winner)

def move_player1_pyramid2_GUI(x):
    if game.turn == 1:
        sound_move()
    else:
        sound_not_your_turn()
    game.move(game.player1.pyramid2, x)
    d = game.to_GUI()
    remove_previous_clicks()
    possible_clicks.clear()
    update_GUI(d)
    winner = game.winner()
    game_over(winner)

def move_player1_pilot1_GUI(x):
    if game.turn == 1:
        sound_move()
    else:
        sound_not_your_turn()
    game.move(game.player1.pilot1, x)
    d = game.to_GUI()
    remove_previous_clicks()
    possible_clicks.clear()
    update_GUI(d)
    winner = game.winner()
    game_over(winner)

def move_player1_pilot2_GUI(x):
    if game.turn == 1:
        sound_move()
    else:
        sound_not_your_turn()
    game.move(game.player1.pilot2, x)
    d = game.to_GUI()
    remove_previous_clicks()
    possible_clicks.clear()
    update_GUI(d)
    winner = game.winner()
    game_over(winner)

def move_player2_pyramid2_GUI(x):
    if game.turn == 2:
        sound_move()
    else:
        sound_not_your_turn()
    game.move(game.player2.pyramid2, x)
    d = game.to_GUI()
    remove_previous_clicks()
    possible_clicks.clear()
    update_GUI(d)
    winner = game.winner()
    game_over(winner)

def move_player2_pyramid1_GUI(x):
    if game.turn == 2:
        sound_move()
    else:
        sound_not_your_turn()
    game.move(game.player2.pyramid1, x)
    d = game.to_GUI()
    remove_previous_clicks()
    possible_clicks.clear()
    update_GUI(d)
    winner = game.winner()
    game_over(winner)

def move_player2_captain_GUI(x):
    if game.turn == 2:
        sound_move()
    else:
        sound_not_your_turn()
    game.move(game.player2.captain, x)
    d = game.to_GUI()
    remove_previous_clicks()
    possible_clicks.clear()
    update_GUI(d)
    winner = game.winner()
    game_over(winner)

def move_player2_pilot1_GUI(x):
    if game.turn == 2:
        sound_move()
    else:
        sound_not_your_turn()
    game.move(game.player2.pilot1, x)
    d = game.to_GUI()
    remove_previous_clicks()
    possible_clicks.clear()
    update_GUI(d)
    winner = game.winner()
    game_over(winner)

def move_player2_pilot2_GUI(x):
    if game.turn == 2:
        sound_move()
    else:
        sound_not_your_turn()
    game.move(game.player2.pilot2, x)
    d = game.to_GUI()
    remove_previous_clicks()
    possible_clicks.clear()
    update_GUI(d)
    winner = game.winner()
    game_over(winner)

def game_over(winner):
    if winner == 1:
        print("player 1 won !")
    if winner == 2:
        print("player 2 won !")
    if winner == 0:
        print("both players won !")

def get_color(pion):
    x = pion.coord[0] + pion.coord[1]
    x = x%2
    if x == 0:
        return "white"
    else:
        return "black"


# image button test

img_player1_captain = ImageTk.PhotoImage(Image.open('C:\\Users\\kael chiche the bada\\PycharmProjects\\Game_with_Val\\game extra\\pieces\\image1.png'))  # PIL solution
img_player1_pilote1 = ImageTk.PhotoImage(Image.open('C:\\Users\\kael chiche the bada\\PycharmProjects\\Game_with_Val\\game extra\\pieces\\image2.png'))  # PIL solution
img_player1_pyramid1 = ImageTk.PhotoImage(Image.open('C:\\Users\\kael chiche the bada\\PycharmProjects\\Game_with_Val\\game extra\\pieces\\image0.png'))  # PIL solution
img_player2_pyramid1 = ImageTk.PhotoImage(Image.open('C:\\Users\\kael chiche the bada\\PycharmProjects\\Game_with_Val\\game extra\\pieces\\image3.png'))  # PIL solution
img_player2_pilot1 = ImageTk.PhotoImage(Image.open('C:\\Users\\kael chiche the bada\\PycharmProjects\\Game_with_Val\\game extra\\pieces\\image4.png'))  # PIL solution
img_player2_captain = ImageTk.PhotoImage(Image.open('C:\\Users\\kael chiche the bada\\PycharmProjects\\Game_with_Val\\game extra\\pieces\\image5.png'))  # PIL solution


player1_captain = Button(my_Window, width="144", height="139", bg=get_color(game.player1.captain), text="player1_capitain", command=clicking_player1_captain, image=img_player1_captain)
player1_pyramid1= Button(my_Window,width="144",height="139",bg=get_color(game.player1.captain), text="player1_pyramid1", command=clicking_player1_pyramid1, image=img_player1_pyramid1)
player1_pyramid2= Button(my_Window,width="144",height="139",bg=get_color(game.player1.captain), text="player1_pyramid2", command=clicking_player1_pyramid2, image=img_player1_pyramid1)
player1_pilot1= Button(my_Window,width="144",height="139",bg=get_color(game.player1.captain), text="player1_pilot1", command=clicking_player1_pilot1, image=img_player1_pilote1)
player1_pilot2= Button(my_Window,width="144",height="139",bg=get_color(game.player1.captain), text="player1_pilot2", command=clicking_player1_pilot2, image=img_player1_pilote1)

player2_captain = Button(my_Window,width="144",height="139",bg=get_color(game.player1.captain), text="player2_capitain", command=clicking_player2_captain, image=img_player2_captain)
player2_pyramid1= Button(my_Window,width="144",height="139",bg=get_color(game.player1.captain), text="player2_pyramid1", command=clicking_player2_pyramid1, image=img_player2_pyramid1)
player2_pyramid2= Button(my_Window,width="144",height="139",bg=get_color(game.player1.captain), text="player2_pyramid2", command=clicking_player2_pyramid2, image=img_player2_pyramid1)
player2_pilot1= Button(my_Window,width="144",height="139",bg=get_color(game.player1.captain), text="player2_pilot1", command=clicking_player2_pilot1, image=img_player2_pilot1)
player2_pilot2= Button(my_Window,width="144",height="139",bg=get_color(game.player1.captain), text="player2_pilot2", command=clicking_player2_pilot2, image=img_player2_pilot1)

player1_pions=[player1_captain, player1_pyramid1,player1_pyramid2,player1_pilot2,player1_pilot1]
player2_pions=[player2_captain, player2_pyramid1,player2_pyramid2,player2_pilot2,player2_pilot1]

def move_player1_captain(x,y):
    xx= 4-x
    player1_captain.grid(row=xx, column=y)
    player1_captain['bg']=get_color(game.player1.captain)

def move_player1_pyramid1(x,y):
    xx= 4-x
    player1_pyramid1.grid(row=xx, column=y)
    player1_pyramid1['bg'] = get_color(game.player1.pyramid1)

def move_player1_pyramid2(x,y):
    xx= 4-x
    player1_pyramid2.grid(row=xx, column=y)
    player1_pyramid2['bg'] = get_color(game.player1.pyramid2)

def move_player1_pilot1(x,y):
    xx= 4-x
    player1_pilot1.grid(row=xx, column=y)
    player1_pilot1['bg'] = get_color(game.player1.pilot1)

def move_player1_pilot2(x,y):
    xx= 4-x
    player1_pilot2.grid(row=xx, column=y)
    player1_pilot2['bg'] = get_color(game.player1.pilot2)

def move_player2_captain(x,y):
    xx= 4-x
    player2_captain.grid(row=xx, column=y)
    player2_captain['bg'] = get_color(game.player2.captain)

def move_player2_pyramid1(x,y):
    xx= 4-x
    player2_pyramid1.grid(row=xx, column=y)
    player2_pyramid1['bg'] = get_color(game.player2.pyramid1)

def move_player2_pyramid2(x,y):
    xx= 4-x
    player2_pyramid2.grid(row=xx, column=y)
    player2_pyramid2['bg'] = get_color(game.player2.pyramid2)

def move_player2_pilot1(x,y):
    xx= 4-x
    player2_pilot1.grid(row=xx, column=y)
    player2_pilot1['bg'] = get_color(game.player2.pilot1)

def move_player2_pilot2(x,y):
    xx= 4-x
    player2_pilot2.grid(row=xx, column=y)
    player2_pilot2['bg'] = get_color(game.player2.pilot2)

def update_GUI(d):

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

    move_player1_captain( d[key][0], d[key][1])
    move_player1_pyramid1( d[key1][0], d[key1][1])
    move_player1_pyramid2( d[key2][0], d[key2][1])
    move_player1_pilot1( d[key3][0], d[key3][1])
    move_player1_pilot2( d[key4][0], d[key4][1])
    move_player2_captain(d[key5][0], d[key5][1])
    move_player2_pyramid1(d[key6][0], d[key6][1])
    move_player2_pyramid2(d[key7][0], d[key7][1])
    move_player2_pilot1(d[key8][0], d[key8][1])
    move_player2_pilot2(d[key9][0], d[key9][1])



d = game.to_GUI()


update_GUI(d)

my_Window.title("clash des combinaison GAME")
my_Window.mainloop()

exit()


