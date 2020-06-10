from tkinter import*
from functools import partial
from WindowGenerateCard import WindowGenerateCard

class WindowMenu(Tk):

    def __init__(self, sound, music=True, sound_effect=True):
        super(WindowMenu, self).__init__()
        self.sound = sound
        self.music = music

        self.button_play = Button(self, text="PLAY", command=self.clicked_play, height="6", width="30", bg="red", font="Times 20")
        self.button_music = Button(self, text="Music ON\OFF", command=self.clicked_music, height="6", width="30", bg="blue",font="Times 20")
        self.button_sound_effects = Button(self, text="Sound Effects ON\OFF", command= self.clicked_sound, height="6", width="30", bg="blue",font="Times 20")
        self.title("Home Menu")
        self.button_music.pack(side=LEFT)
        self.button_sound_effects.pack(side=RIGHT)
        self.button_play.pack()

        self.player_number = 1

    def clicked_play(self):
        self.sound.play_sound_select()
        window_card = WindowGenerateCard(self.sound)
        window_card.mainloop()

    def clicked_music(self):
        self.sound.play_sound_select()
        if self.sound.music:
            self.sound.music = False
            self.sound.pause_music()
        else:
            self.sound.music = True
            self.sound.unpause_music()

    def clicked_sound(self):
        print("here")
        if self.sound.sound_effects:
            self.sound.play_sound_select()
            self.sound.sound_effects = False
        else:
            self.sound.sound_effects = True
            self.sound.play_sound_select()
            print("sound effects on !")