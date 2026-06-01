import time
import keyboard
import pyautogui
Running = True
time.sleep(3)
while (Running):
    pyautogui.typewrite("Hello world", interval=0.1)
    pyautogui.press('enter')
    time.sleep(1)

    for i in range(50):  # 50 x 0.1 = 5 seconds total
            if keyboard.is_pressed('f'):
                print("F pressed during wait - stopping!")
                Running = False
            time.sleep(0.1)
    if keyboard.is_pressed('f'):
            Running = False
   