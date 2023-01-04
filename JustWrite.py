#For most writers, a big problem is writing block. 
# Where you can't think of what to write and you can't write anything.

#One of the most interesting solutions to this is 
# a web app called The Most Dangerous Writing App, 
# an online text editor where if you stop writing, 
# all your progress will be lost.

#A timer will count down and when the website 
# detects the user has not written anything 
# in the last 5/10 seconds, it will delete all 
# the text they've written so far.

#Try it out here:

#https://www.squibler.io/dangerous-writing-prompt-app

#You are going to build a desktop app that has 
# similar functionality. The design is up to you, 
# but it should allow a user to type and if they stop 
# for more than 5 seconds, it should delete everything 
# they've written so far.

import random
import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedTk
import sv_ttk
import math
from promptcleaning import data
from time import sleep

DARKEST = "#222222"
LIGHT = "#434242"
OFFWHITE = "#F3EFE0"
LIGHTBLUE = "#22A39F"
FONT = ("Roboto", 16)

previous_text = ""


window = tk.Tk()
window.tk_setPalette('SystemButtonFace')
window.title("JustWrite")

window.geometry("1000x724")

window.resizable(True, True)

sv_ttk.set_theme("dark")


canvas = tk.Canvas(width=50, height=50, bg= LIGHT, highlightthickness=0)
timer_text = canvas.create_text(25, 25, text="00:00", fill="white", font=(FONT, 15))
canvas.pack(side=tk.TOP, anchor="w")


def start_writing():
    global text_area
    prompt.config(text=random.choice(data))
    text_area = tk.Text(Frame,width=50,foreground=OFFWHITE, borderwidth=0, 
                    background=LIGHT,font=FONT)

        # Set the text area's state to 'normal' to allow user input
    text_area.config(state='normal')

    window.after(5000, check_text_area)

    # Pack the text area widget and make it visible
    text_area.pack(side=tk.BOTTOM,padx=10, pady=10)
    count_down(5)
    
def start_writing_noprompt():
    global text_area
    prompt.destroy()
    text_area = tk.Text(Frame,width=50,foreground=OFFWHITE, borderwidth=0, 
                    background=LIGHT,font=FONT)

        # Set the text area's state to 'normal' to allow user input
    text_area.config(state='normal')

    window.after(5000, check_text_area)

    # Pack the text area widget and make it visible
    text_area.pack(side=tk.BOTTOM,padx=10, pady=10)
    count_down(5)



def count_down(count):
    global canvas
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
        
    current_text = text_area.get("1.0", tk.END)
    
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    
    if not current_text.strip() and previous_text.strip():
        timer = window.after(1000, count_down, count - 1)
    elif current_text.strip() == previous_text.strip():
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        reset_timer()
    else:
        count = 5
       # previous_text = current_text
        timer = window.after(1000, count_down, count - 1)
        
        
# The "raw CPM" is the actual number of characters you type per minute, 
# including all the mistakes. "Corrected" scores count only correctly typed words. 
# "WPM" is just the corrected CPM divided by 5.
        
        
def reset_timer():
    global current_text
    with open("results.txt", 'a', encoding="utf-8") as file:
        file.write(f"\n{prompt.cget('text')},{current_text}")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    #Need to make this update the above list aswell
    #Did it in the start function
    #Need to reset the word label on timer start too



def check_text_area():
    global previous_text
    global text_area
    global current_text
    
    # Get the current text in the text area
    current_text = text_area.get("1.0", tk.END)
    
    # If the text area is empty and it was not empty the last time the function was called, destroy it
    if not current_text.strip() and previous_text.strip():
        text_area.destroy()
        reset_timer()
    elif current_text.strip() == previous_text.strip():
        text_area.destroy()
        reset_timer()
    else:
        # If the text area is not empty, 
        # or if it was not empty the last time the 
        # function was called, reschedule the function to be called again after 15 seconds
        window.after(5000, check_text_area)
        previous_text = current_text





title_label = tk.Label(text="Just Write", fg=LIGHTBLUE, font=(FONT, 50))
title_label.pack(side=tk.TOP,anchor='n', padx=15)



Frame = tk.Frame(window, background="#1b1b1b", height=20,pady=20)
Frame.pack(side=tk.TOP, fill=tk.X)


prompt = tk.Label(Frame, text="Welcome to ultimate writing tool. If you don't write for 5 seconds your text dissappears.", justify=tk.CENTER, foreground=OFFWHITE,
                  font=("Roboto", 20), borderwidth=5, background=DARKEST, activebackground="#1b1b1b",fg="white",
                  state="normal")
prompt.config(wraplength=500)
prompt.pack(side=tk.TOP,pady=10)


buttons = tk.Frame(window, background="#1b1b1b", height=20,pady=20)
buttons.pack(side=tk.TOP, fill=tk.X)
start_button = ttk.Button(buttons,text="Start", command=start_writing)
start_button.pack(side=tk.LEFT, anchor="n")


nopromptbtn = ttk.Button(buttons, text="Start Without a prompt", command=start_writing_noprompt)
nopromptbtn.pack(side=tk.RIGHT, anchor="n")








window.mainloop()
#TO DO
#Add the timer DONE
#add a button to change the prompt
#Button to start without a prompt DONE
#Save the texts written together with the prompt in a text file when it gets deleted