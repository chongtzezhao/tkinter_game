from tkinter import *
import random
import time

game = Tk()
game.title("Click the Button!")
game.geometry("900x700")
timer = Tk()
timer.title('Timings')
timer.geometry("300x200")


w = game.winfo_width()
h = game.winfo_height()
print(w, h)
labels = []
prev_time = 0
prev_coord = (0, 0)
scores = []
Label(timer, text = 'Timings', anchor=CENTER, font=14).grid(padx=50)
show_score = Label(timer, text = '', font=14)

def move_button(prev_coord):
    w = game.winfo_width()
    h = game.winfo_height()
    x = random.randint(1, w-button.winfo_reqwidth())
    y = random.randint(1, h-button.winfo_reqheight())
    button.grid(pady = y, padx = x)
    if prev_coord is None:
        return None, (x, y)
    prev_x, prev_y = prev_coord
    dist = ((prev_x-x)**2+(prev_y-y)**2)**0.5
    prev_coord = (x, y)
    return dist, prev_coord

def update_time(prev_time):
    diff = time.time()-prev_time
    prev_time+=diff
    new_label = Label(timer, text = f'{diff:.3f}', anchor=CENTER, font=14)
    new_label.grid()
    return new_label, prev_time, diff

def update_record():
    global prev_time
    global prev_coord
    global labels
    global scores
    global show_score
    prev_label, prev_time, diff = update_time(prev_time)
    labels.append(prev_label)
    if len(labels)>5:
        labels[0].destroy()
        del labels[0]
    dist, prev_coord = move_button(prev_coord)
    scores.append(dist/diff)
    show_score.destroy()
    show_score = Label(timer, text = str(sum(scores)/len(scores)), font=14)
    show_score.grid()
    
    
    

def start_game():
    global prev_time
    global prev_coord
    global show_score
    prev_coord = None
    prev_time = time.time()
    start.destroy()
    move_button(None)
    show_score.grid()
        
photo = PhotoImage(file = "uwu.png")
button = Button(game, image=photo, command=update_record)

start_photo = PhotoImage(file = "start.png")
start = Button(game, image=start_photo, command=start_game, width=450, height=450)
start.grid(pady=125, padx=225)


game.mainloop()
timer.mainloop()
