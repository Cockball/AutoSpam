import pyautogui
import time
import random

words = [
"Hello",
"FYI This is a SPAM message",
"Not sponsored",
"Sorry I got bored and codded a spam bot",
";-;"
]

def sleep():
time.sleep(8)

word = random.choice(words)

def handler():

for i in range(1):
for word in words:
pyautogui.typewriter(word)
pyautogui.press("enter")

def main():
sleep():
handler():

if __name__ = '__main__':
main()
