import tkinter as tk
import datetime
import winsound

def set_alarm():
    alarm_time = alarm_entry.get()
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            play_alarm_sound()
            break

def play_alarm_sound():
    frequency = 2500  # Set frequency (range: 37 to 32767 Hz)
    duration = 2000  # Set duration in milliseconds (2000ms = 2 seconds)
    winsound.Beep(frequency, duration)

# Create the main window
window = tk.Tk()
window.title("Alarm Clock")

# Create a label and an entry for the alarm time
alarm_label = tk.Label(window, text="Set Alarm (HH:MM:SS):")
alarm_label.pack(pady=10)
alarm_entry = tk.Entry(window)
alarm_entry.pack()

# Create a button to set the alarm
set_alarm_button = tk.Button(window, text="Set Alarm", command=set_alarm)
set_alarm_button.pack(pady=10)

# Run the main event loop
window.mainloop()
