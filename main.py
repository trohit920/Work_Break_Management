from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer_status = None
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer_status)
    canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    work_time = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    checkbutton.config(text="")

    reps += 1
    if reps % 8 == 0:
        count_down(long_break_sec)
        my_label.config(text="Long Break ", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        my_label.config(text="Short Break ", fg=PINK)
    else:
        count_down(work_time)
        my_label.config(text="Work Time", fg=GREEN )


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0 or count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_status
        timer_status = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✓"
        checkbutton.config(text=mark, font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(101, 112, image=image)
timer_text = canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

my_label= Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
my_label.grid(column=1, row=0)

checkbutton = Label(text="", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
checkbutton.grid(column=1, row=3)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
