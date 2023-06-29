import datetime
import time

def digital_clock():
    while True:
        # Get the current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        # Clear the screen (for better display in some terminals)
        print("\033c", end="")
        # Print the current time
        print(current_time, end="", flush=True)
        # Wait for one second
        time.sleep(1)

# Start the digital clock
digital_clock()
