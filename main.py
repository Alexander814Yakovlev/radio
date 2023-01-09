import vlc, customtkinter
from PIL import Image

root = customtkinter.CTk()
root.minsize(320, 320)
root.title("Comedy Radio")
root.iconbitmap('icon.ico')
#root.overrideredirect(1)

class WMover:
    def __init__(self,tk):
        self.tk=tk
        self.e=None
        self.tk.bind('<B1-Motion>',self.move)
    def move(self,e):
        if not self.e:self.e=e
        s,x,y=self.tk.geometry().split('+')
        x,y=int(x),int(y)
        self.tk.geometry(s+'+'+str(x+e.x-self.e.x)+'+'+str(y+e.y-self.e.y))
        self.e=e

def playback():
    global my_media
    global button_frame

    my_media = vlc.MediaPlayer("https://pub0102.101.ru:8000/stream/air/aac/64/202")
    my_media.play()
    
    button_frame.destroy()

    button_frame = customtkinter.CTkFrame(master=root, fg_color="transparent")
    button_frame.place(x=130, y=270)

    pause_button = customtkinter.CTkButton(master=button_frame, command=pause, text="⏸️", font=('Roboto', 26), height=20, width=20, fg_color='transparent', text_color='red', hover_color='white')
    pause_button.pack()

    play_button.destroy()

def pause():
    global button_frame

    my_media.stop()
    button_frame.destroy()

    button_frame = customtkinter.CTkFrame(master=root, fg_color="transparent")
    button_frame.place(x=130, y=270)

    play_button = customtkinter.CTkButton(master=button_frame, command=playback, text='⏯️', font=('Roboto', 26), height=20, width=20, fg_color='transparent', text_color='red', hover_color='white')
    play_button.pack()

cover = customtkinter.CTkImage(light_image=Image.open("comedy-radio2.jpg"),
                                  dark_image=Image.open("comedy-radio2.jpg"),
                                  size=(320, 320))


cover_frame = customtkinter.CTkLabel(master=root, image=cover, text=None)
cover_frame.pack(fill="both")

button_frame = customtkinter.CTkFrame(master=root, fg_color="transparent")
button_frame.place(x=130, y=270) 

play_button = customtkinter.CTkButton(master=button_frame, command=playback, text='⏯️', font=('Roboto', 26), height=20, width=20, fg_color='transparent', text_color='red', hover_color='white')
play_button.pack()

Ext_but = customtkinter.CTkButton(root, text="❌", command=lambda: exit(), fg_color='transparent', hover_color='white', text_color='red')
Ext_but.place(x=290, y=10, anchor="nw", width=30, height=20)

w=WMover(root)
root.mainloop()