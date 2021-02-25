import pyautogui, time
time.sleep(2) #time after executing when brute force starts
f = open(text, 'r') #your wordlist here need to put a wordlist to the same folder
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press(enter)
