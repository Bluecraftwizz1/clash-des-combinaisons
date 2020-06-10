from tkinter import *
from PIL import ImageTk,Image
from functools import partial
from WindowGenerateCard import WindowGenerateCard
from WindowGenerateCardAI import WindowGenerateCardAI
from MySound import MySound
import pygame

class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master, sound):

        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        self.sound = sound

        # reference to the master widget, which is the tk window
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit, font="Times 20")

        # added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Menu", font="Times 20", command=self.Menu_open)

        # added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)


    def client_exit(self):
        exit()

    def Menu_open(self):
        x = WindowMenu(self.sound)
        x.mainloop()

# root window created. Here, that would be the only window, but
# you can later have windows within windows.

# creation of an instance

class WindowMenu(Tk):

    def __init__(self, sound):
        super(WindowMenu, self).__init__()

        self.sound = sound

        self.sound.start()

        self.geometry("1575x640")

        # add the frame
        frame = Window(self, sound)

        #self.Menu_img=ImageTk.PhotoImage(Image.open("Gameexample.png"),master=self)
        self.img_Music_on_off=ImageTk.PhotoImage(Image.open("images and sounds\\Music_logo.jpg"),master=self)
        self.img_Sound_on_off=ImageTk.PhotoImage(Image.open("images and sounds\\Sound_logo.jpg"),master=self)
        self.img_background = ImageTk.PhotoImage(Image.open("images and sounds\\background_grid.png"),master=self)
        self.img_list = ImageTk.PhotoImage(Image.open("images and sounds\\list.jpg"), master=self)

        self.label = Label(self, width="1579", height="732", image = self.img_background)
        self.label.image=self.img_background
        self.label.pack()

        self.button_play_2 = Button(self ,text="Multi-Player", height="1", width="15", bg="red", font="Times 20",command=self.clicked_play)
        self.button_play_1 = Button(self, text="Single-Player", height="1", width="15", bg="red", font="Times 20", command=self.clicked_playAI)
        self.Music_on_off = Button(self, height="81", width="86", image=self.img_Music_on_off, command = self.clicked_music)
        self.Sound_on_off = Button(self, height="81", width="86", image=self.img_Sound_on_off, command = self.clicked_sound)
        self.list = Button(self, height="81", width="86", image=self.img_list, text="Rules", command = self.clicked_rules)

        self.button_play_2.place(relx=0.42,rely=0.64)
        self.button_play_1.place(relx=0.42, rely=0.55)
        self.Music_on_off.place(relx=0.94,rely=0.01)
        self.Sound_on_off.place(relx=0.94,rely=0.15)
        #self.list.place(relx=0.94, rely=0.29)

        self.windows = []

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        sys.exit()

    def clicked_play(self):
        self.sound.play_sound_select()
        window_card = WindowGenerateCard(self.sound)
        window_card.mainloop()

    def clicked_playAI(self):
        self.sound.play_sound_select()
        self.windows.append(WindowGenerateCardAI(self.sound))
        print(self.windows)
        self.windows[-1].mainloop()


    def clicked_rules(self):
        self.sound.play_rules()

    def clicked_sound(self):
        if self.sound.sound_effects:
            self.sound.play_sound_select()
            self.sound.sound_effects = False
            self.sound.effects_off()
            print("sound effects off !")
        else:
            self.sound.sound_effects = True
            self.sound.play_sound_select()
            print("sound effects on !")
            self.sound.effects_on()

    def clicked_music(self):
        if self.sound.music:
            self.sound.music = False
            self.sound.pause_music()
        else:
            self.sound.music = True
            self.sound.unpause_music()
