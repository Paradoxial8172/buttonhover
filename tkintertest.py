from tkinter import *
from PIL import Image, ImageTk
import pygame.mixer as mixer

mixer.init()

mixer.music.load("explode.mp3")

root = Tk()

def sound():
    mixer.music.play()

play_img_open = Image.open("play.png")
play_img = ImageTk.PhotoImage(play_img_open)
stop_img_open = Image.open("stop.png")
stop_img = ImageTk.PhotoImage(stop_img_open)

lighter_play_open_img = play_img_open.point(lambda p: p * 0.7)  
lighter_play_img = ImageTk.PhotoImage(lighter_play_open_img)
lighter_stop_open_img = stop_img_open.point(lambda p: p * 0.7)
lighter_stop_img = ImageTk.PhotoImage(lighter_stop_open_img)

def lighten_img(button: Button, img):
    button.configure(image=img)

def restore_image(button: Button, img):
    button.configure(image=img)

# Create the button with the original image
button = Button(root, image=play_img, relief=FLAT)
button2 = Button(root, image=stop_img, relief=FLAT, command=sound)
button.pack()
button2.pack()

button.bind("<Enter>", func=lambda e: lighten_img(button, lighter_play_img))
button.bind("<Leave>", func=lambda e: restore_image(button, play_img))

button2.bind("<Enter>", func=lambda e: lighten_img(button2, lighter_stop_img))
button2.bind("<Leave>", func=lambda e: restore_image(button2, stop_img))

root.mainloop()