import time
timestamp = int(time.strftime('%H'))
def greeting(timestamp):
    if 8 <= timestamp < 12:
        print (f"Good Morning Sir")
    elif 12 <= timestamp < 20:
        print(f"Good evening Sir")
    else:
        print(f"Good Night Sir")

if __name__ == "__main__":
    greeting(timestamp)