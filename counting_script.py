import time
import os

# COUNT_FILE = "./count.txt"
COUNT_FILE = "/app/count.txt"


def read_count():
    try:
        with open(COUNT_FILE, "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 1


def write_count(count):
    with open(COUNT_FILE, "w") as file:
        file.write(str(count))

count = read_count()

while True:
    print(f"Count: {count}")
    count += 1
    write_count(count)
    time.sleep(1)

