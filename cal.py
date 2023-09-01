#!/usr/bin/env python3
#Yearly Calendar

import tkinter as tk
import calendar

#show calendar of selected year
def show_cal(event=None):
    gui = tk.Tk()
    gui.title("Calendar")
    year = int(entry_box.get())
    gui_content = calendar.calendar(year)
    cal_year = tk.Label(gui, text=gui_content, font="Cousine 10 bold", justify='left')
    cal_year.grid(column=0, row=0, padx=0, pady=0)
    #print (gui_content)
    gui.mainloop()


#labels/buttons 
if __name__ == "__main__":
    new = tk.Tk()
    new.title("Calendar")
    new.geometry("300x140")
    cal_label = tk.Label(new, text="Calendar", font=("Arial 14 bold"))
    entry_label = tk.Label(new, text="Enter Year: ", anchor='w')
    entry_box = tk.Entry(new)
    show_btn = tk.Button(new, text='Show', width=4, command=show_cal)
    exit_btn = tk.Button(new, text='Exit', width=4, command=new.destroy)
    
    #grid layout
    cal_label.grid(column=0, row=0, padx=4, pady=6)
    entry_label.grid(column=0, row=1, padx=4, pady=4)
    entry_box.grid(column=1, row=1, padx=4, pady=4)
    show_btn.grid(column=1, row=2, padx=4, pady=(16,2), sticky='w')
    exit_btn.grid(column=1, row=2, padx=4, pady=(16,2), sticky='e')


    #set focus/bind
    entry_box.focus_set()
    entry_box.bind('<Return>', show_cal)

    new.mainloop()
