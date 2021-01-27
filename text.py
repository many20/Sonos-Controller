import sys, json
import keyboard

# https://github.com/boppreh/keyboard

for line in sys.stdin:
    print(line[:-1])

keyboard.on_press_key('1', lambda e: print('1'), suppress=True)
keyboard.on_press_key('2', lambda e: print('2'), suppress=True)
keyboard.on_press_key('3', lambda e: print('3'), suppress=True)
keyboard.on_press_key('4', lambda e: print('4'), suppress=True)
keyboard.on_press_key('5', lambda e: print('5'), suppress=True)
keyboard.on_press_key('6', lambda e: print('6'), suppress=True)
keyboard.on_press_key('7', lambda e: print('7'), suppress=True)
keyboard.on_press_key('8', lambda e: print('8'), suppress=True)
keyboard.on_press_key('9', lambda e: print('9'), suppress=True)
keyboard.on_press_key('0', lambda e: print('0'), suppress=True)
keyboard.on_press_key('enter', lambda e: print('enter'), suppress=True)

# Blocks until you press esc.
keyboard.wait('esc')


