import tkinter as tk
import random
print(' Sinh viên: Lê Quang Trung')
print('Mã sv: 23572-21610012')
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 120

def startGame(event):
    if timeleft == 120:
        countdown()
        nextColour()

def nextColour():
    global score
    global timeleft

    if timeleft > 0:
        e.focus_set()

        if e.get().lower() == colours[0].lower():
            score += 2
        elif e.get() != "":  
            score -= 1

        e.delete(0, tk.END)

        random.shuffle(colours)
        label.config(fg=colours[0], text=colours[1])

        scoreLabel.config(text="Score: " + str(score))

def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1

        timeLabel.config(text="Time left: " + str(timeleft))

        timeLabel.after(1000, countdown)

root = tk.Tk()
root.title("COLOR GAME")
root.geometry("500x350")
root.configure(bg="#FAF9F6") 

instructions = tk.Label(root, text="Type in the color of the words, not the word itself!",
                        font=('Helvetica', 14), bg="#FAF9F6")
instructions.pack(pady=10)


scoreLabel = tk.Label(root, text="Press enter to start", font=('Helvetica', 16), bg="#FAF9F6")
scoreLabel.pack()


timeLabel = tk.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 16), bg="#FAF9F6")
timeLabel.pack()

label = tk.Label(root, font=('Helvetica', 60), bg="#FAF9F6")
label.pack(pady=20)

e = tk.Entry(root, font=('Helvetica', 14), width=20, justify='center')
e.pack(pady=10)

root.bind('<Return>', startGame)

e.focus_set()

root.mainloop()
