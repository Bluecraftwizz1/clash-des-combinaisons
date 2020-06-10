from WindowMenu import WindowMenu
from tkinter import*
from Game import Game
from PIL import ImageTk, Image
from functools import partial
import random
from winsound import *
from MySound import MySound
import pygame
import Menu_Window

sound = MySound()

x = Menu_Window.WindowMenu(sound)
x.mainloop()