import keyboard

x = True

if (not x):
    keyboard.press_and_release('shift+s')
if x:
    keyboard.press_and_release('alt+tab', do_release=False)


