import win32com.client

names = ["Rahul", "Nishant", "Harry"]

speaker = win32com.client.Dispatch("SAPI.SpVoice")

for name in names:
    speaker.Speak(f"Shoutout to {name}")
