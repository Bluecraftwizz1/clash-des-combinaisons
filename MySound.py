from winsound import *
import pygame

class MySound:

    def __init__(self, music=True, sound_effects=True, rules=False):
        self.music = music
        self.sound_effects = sound_effects
        #self.rules = rules

        pygame.init()
        pygame.mixer.music.load('images and sounds\\hamza.mp3')
        pygame.mixer.music.play(-1)

        #pygame.init()
        #pygame.mixer.music.load('rules.mp3')
        #pygame.mixer.music.play(-1)

    def play_rules(self):
        PlaySound('images and sounds\\rules.wav', SND_ASYNC)

    def com(self, num):
        if self.sound_effects:
            if num == 1:
                PlaySound('images and sounds\\1_pos.wav', SND_ASYNC)
            if num == 2:
                PlaySound('images and sounds\\2_pos.wav', SND_ASYNC)
            if num == 3:
                PlaySound('images and sounds\\3_pos.wav', SND_ASYNC)
            if num == 4:
                PlaySound('images and sounds\\4_pos.wav', SND_ASYNC)
            if num == 5:
                PlaySound('images and sounds\\5_pos.wav', SND_ASYNC)
            if num == 0:
                PlaySound('images and sounds\\no_pos.wav', SND_ASYNC)

    def you_won(self):
        if self.sound_effects:
            PlaySound('images and sounds\\you_1.wav', SND_FILENAME)

    def you_lose(self):
        if self.sound_effects:
            PlaySound('images and sounds\\you_lose.wav', SND_FILENAME)

    def victoire(self):
        if self.sound_effects:
            PlaySound('images and sounds\\victoire.wav', SND_ASYNC)

    def start(self):
        PlaySound('images and sounds\\start.wav', SND_ASYNC)

    def pause_music(self):
        print("images and sounds\\pausing music")
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()

    def play_sound_rules(self):
        PlaySound('images and sounds\\select.wav', SND_ASYNC)

    def unplay_sound_rules(self):
        PlaySound('images and sounds\\rules.wav', SND_ASYNC)

    def effects_off(self):
        PlaySound('images and sounds\\effects_off.wav', SND_ASYNC)

    def effects_on(self):
        PlaySound('images and sounds\\effects_on.wav', SND_ASYNC)

    def play_sound_select(self):
        if self.sound_effects:
            PlaySound('images and sounds\\select.wav', SND_ASYNC)

    def play_move(self):
        if self.sound_effects:
            PlaySound('images and sounds\\move.wav', SND_ASYNC)

    def play_not_your_turn(self):
        if self.sound_effects:
            PlaySound('images and sounds\\not_your_turn.wav', SND_ASYNC)

    def play_push(self):
        if self.sound_effects:
            PlaySound('images and sounds\\YEET.wav', SND_ASYNC)

    def play_player_red_generate(self):
        if self.sound_effects:
            PlaySound('images and sounds\\player_red_generate.wav', SND_ASYNC)

    def play_player_blue_generate(self):
        if self.sound_effects:
            PlaySound('images and sounds\\player_blue_generate.wav', SND_ASYNC)

    def play_player_red_won(self):
        if self.sound_effects:
            PlaySound('images and sounds\\player_red_won.wav', SND_FILENAME)

    def play_player_blue_won(self):
        if self.sound_effects:
            PlaySound('images and sounds\\player_blue_won.wav', SND_FILENAME)

    def play_blue_orient(self):
        if self.sound_effects:
            PlaySound('images and sounds\\blue_orient.wav', SND_ASYNC)

    def play_red_orient(self):
        if self.sound_effects:
            PlaySound('images and sounds\\red_orient.wav', SND_ASYNC)

    def play_blue_first(self):
        if self.sound_effects:
            PlaySound('images and sounds\\player_blue_first.wav', SND_ASYNC)

    def play_red_first(self):
        if self.sound_effects:
            PlaySound('images and sounds\\player_red_first.wav', SND_ASYNC)