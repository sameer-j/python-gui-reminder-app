"""
author: 'Sameer Jain'
updated by: 'Rinku Kumari'

-------------------------
Reminder App V3
-------------------------
Python GUI app using tkinter.
V2 makes use of custom message box to show the pop up message.
program needs to be run from command line/ terminal.
"""

from time import sleep
from tkinter import *
from tkinter import ttk

execution_count = 0

def action(win, more):
    global execution_count
    global root
    print('Answer', more)
    if more:
        win.destroy()
        sleep(snooze_time)
        execution_count = execution_count + 1
        ReminderWindow(title, message)
    else:
        win.destroy()
        root.destroy()

def ReminderWindow(title, message):
    global root
    print('Execution', execution_count)
    win = Toplevel()
    win.withdraw()
    win.update_idletasks()
    x = (win.winfo_screenwidth() - win.winfo_reqwidth()) / 2
    y = (win.winfo_screenheight() - win.winfo_reqheight()) / 2
    win.geometry("+%d+%d" % (x, y))
    win.deiconify()
    win.title(title)
    message1=message
    message2='Current Snooze time={0} seconds'.format(snooze_time)
    message3 = 'Do you want more reminders?'
    ttk.Label(win, text=message1).grid(column=0, row=0)
    ttk.Label(win, text=message2).grid(column=0, row=1)
    ttk.Label(win, text=message3).grid(column=0, row=2)
    yes_btn = ttk.Button(win, text='Yes', command=lambda: action(win, True))
    yes_btn.grid(column=0,row=3)
    ttk.Button(win, text='No', command=lambda: action(win, False)).grid(column=1, row=3)
    yes_btn.focus()
    win.lift()
    win.attributes('-topmost', True)

print('\n\n\n')
print('Welcome to Reminder App(beta v3)!')
print('-------------------------------------------------')
print('Once started, the app runs indefinetly till you ask it stop.')
print('It will pop up a message window every set snooze interval time to remind you to do a task periodically')
print('-------------')
snooze_time = int(input('Enter Snooze interval:'))
title = input('Enter title for reminder window: ')
message = input('Enter message for reminder window: ')
# snooze_time = 3
print('\n\nThanks! You will get your first reminder in {0} seconds'.format(snooze_time))
print('\n\n')
print('App started....')

root = Tk()
root.withdraw()
execution_count = 1
ReminderWindow(title, message)   # example title='Eye Exercise Reminder', message='Time for Eye Exercise!'
root.mainloop()
print('Exiting, bye')
