import random
import tkinter as tk
Rock=0
Paper=1
Scissor=2
Win=1
Lose=-1
Draw=0
Outcomes={
    (0,1):Lose, (0,2):Win, (0,0):Draw,
    (1,0):Win, (1,2):Lose, (1,1):Draw,
    (2,0):Lose, (2,1):Win, (2,2):Draw}
def game(user,com):
    return Outcomes[(user,com)]
def playgame(userchoice):
    comp=random.randint(0,2)
    outcomes=game(userchoice,comp)
    result="you won!" if outcomes==Win else "You Lost!" if outcomes==Lose else "draw"
    label.config(text=f"Computer chose {['Rock', 'Paper', 'Scissors'][comp]} \n{result}")
root=tk.Tk()
root.geometry("300x300")
root.maxsize(600,600)
root.title("Rock,Paper and scissor")
label=tk.Label(root, text="select an option")
label.pack()
rockbutton=tk.Button(root, text="Rock", width=40, height=3, command=lambda: playgame(0))
rockbutton.pack()
paperbutton=tk.Button(root, text="Paper", width=40, height=3, command=lambda: playgame(1))
paperbutton.pack()
scissorbutton=tk.Button(root, text="Scissor", width=40, height=3, command=lambda: playgame(2))
scissorbutton.pack()
label=tk.Button(root, text=" ")
label.pack()
root.mainloop()

