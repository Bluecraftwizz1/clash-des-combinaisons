from tkinter import*
import pygame

def clicked_play():
    update = 10
    if update == 10:
        print("play")
        my_Window.destroy()  # Do we have to destroy it? ,,,,,YES!!!!!!!!!!!
        import GUI
        


score_audio = 1

def audio_on_off():
    global score_audio
    score_audio = score_audio +1
    if score_audio %2==0:
        print("song on")
        pygame.mixer.music.unpause()
    else:
        print("song off")
        pygame.mixer.music.pause()

score_audio1 = 1
def audio1_on_off():
    global score_audio1
    score_audio1 = score_audio1 +1
    if score_audio1 %2==0:
        print("sound_effects on")
        sound_effects = True
    else:
        print("sound_effects off")
        sound_effects = False

my_Window = Tk()
update =0

sound_select = lambda: PlaySound(r'C:\Users\kael chiche the bada\PycharmProjects\Game_with_Val\game extra\sounds\select', SND_ASYNC)
sound_move = lambda: PlaySound(r'C:\Users\kael chiche the bada\PycharmProjects\Game_with_Val\game extra\sounds\move', SND_ASYNC)
sound_not_your_turn = lambda: PlaySound(r'C:\Users\kael chiche the bada\PycharmProjects\Game_with_Val\game extra\sounds\not_your_turn',SND_ASYNC)

#playsound.playsound(r'C:\Users\kael chiche the bada\Desktop\game extra\sounds\music.wav'),False)
pygame.init()
pygame.mixer.music.load(r'C:\Users\kael chiche the bada\PycharmProjects\Game_with_Val\game extra\sounds\music_mp3.mp3')
pygame.mixer.music.play(-1)

sound_effects = True

button = Button(my_Window, text="PLAY",command=clicked_play, height="6", width="30", bg="red", font="Times 20")
audio = Button(my_Window, text="background Song ON\OFF",command=audio_on_off, height="6", width="30", bg="blue", font="Times 20")
audio1 = Button(my_Window, text="sound effects ON\OFF",command=audio1_on_off, height="6", width="30", bg="blue", font="Times 20")
my_Window.title("Home Menu")
audio.pack(side=LEFT)
audio1.pack(side=RIGHT)
button.pack()


my_Window.mainloop()
