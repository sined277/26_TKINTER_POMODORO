import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
# Define some constant values
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    """Reset the timer and all labels and counters"""
    # Cancel any ongoing timer
    window.after_cancel(timer)
    # Reset the timer label
    label_timer.config(text="Timer", fg=GREEN, bg='#212A3E', font=(FONT_NAME, 50, 'bold'))
    # Reset the canvas timer text
    canvas.itemconfig(timer_text, text='00:00')
    # Reset the session mark label
    label_gal.config(text='')
    # Reset the reps counter
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    """Start the timer based on the current session type"""
    global reps
    reps += 1

    # Calculate the duration of the current session
    work_sec = WORK_MIN * 60
    shoth_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Check the type of session and update the timer and label accordingly
    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text='Long Break', fg=RED)
    elif reps % 2 == 0:
        count_down(shoth_break_sec)
        label_timer.config(text='Short Break', fg=PINK)
    else:
        count_down(work_sec)
        label_timer.config(text='Working')

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    """Countdown mechanism for the timer"""
    # Calculate minutes and seconds from the count
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    # Update the canvas timer text
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    # Call this function again after 1 second until the count is 0
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # If the current session has ended, start the next session
        start_timer()
        # Update the session mark label with a checkmark
        mark = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += '✔'
        label_gal.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

# Create a tkinter window
window = tkinter.Tk()
window.title('POMODORO')
window.config(padx=100, pady=50, bg='#212A3E')

# Labels
# Create the timer label
label_timer = tkinter.Label(text="Timer", fg=GREEN, bg='#212A3E', font=(FONT_NAME, 50, 'bold'))
label_timer.grid(column=1, row=0)
# Create the session mark label
label_gal = tkinter.Label(bg='#212A3E', fg=GREEN, font=(FONT_NAME, 35, 'bold'))
label_gal.grid(column=1, row=4)

# Buttons

# Creating two buttons and placing them on the grid
button_start = tkinter.Button(text="Start", command=start_timer, highlightthickness=0)
button_start.grid(column=0, row=4)

button_reset = tkinter.Button(text="Reset", command=reset_timer, highlightthickness=0)
button_reset.grid(column=2, row=4)

# Creating a canvas and displaying an image and text on it, then placing it on the grid
canvas = tkinter.Canvas(width=200, height=224, bg='#212A3E', highlightthickness=0)
tomato_img = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Starting the main loop for the tkinter window
window.mainloop()

