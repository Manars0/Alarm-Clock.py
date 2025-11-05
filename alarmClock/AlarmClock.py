import tkinter as tk
import time
import winsound

def set_alarm():
    alarm_time = entry.get()
    label.config(text='Alarm Time: '+ alarm_time)

    root.after(1000, check_alarm, alarm_time)

def check_alarm (alarm_time):
    current_time = time.strftime('%H:%M:%S')

    if current_time == alarm_time:
        label.config(text='Alarm Time: '+ alarm_time + '\n WAKE UP')
        winsound.Beep(1000,2000)
    else:
        root.after(1000, check_alarm, alarm_time) 

root = tk.Tk()
root.title('ALARM CLOCK')

label= tk.Label(root, text='Enter alarm tima (HH:MM:SS)')
label.pack()
entry= tk.Entry(root)
entry.pack()

button = tk.Button(root, text='SET ALARM', command=set_alarm)
button.pack()

root.mainloop()