import win32com.client
import time

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while True:
    curr_time = time.strftime("%H:%M:%S")
    print(curr_time)
    speaker.speak(f"The current time is {curr_time}, It's time to drink water")
    

    time.sleep(7200)
