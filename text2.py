import sys, json
import keyboard

# https://github.com/boppreh/keyboard

keys = []

for line in sys.stdin:
    # print(line[:-1])
    # print(json.load(line))
    keys = json.loads(line)

for key in keys:
  print(key[1])
  keyboard.add_hotkey(key[0], print, args=(key[1]), suppress=True)

print('ready')

# keyboard.add_hotkey('1', lambda: print('1'), suppress=True)
# keyboard.add_hotkey('2', lambda: print('2'), suppress=True)
# keyboard.add_hotkey('3', lambda: print('3'), suppress=True)
# keyboard.add_hotkey('4', lambda: print('4'), suppress=True)
# keyboard.add_hotkey('5', lambda: print('5'), suppress=True)
# keyboard.add_hotkey('6', lambda: print('6'), suppress=True)
# keyboard.add_hotkey('7', lambda: print('7'), suppress=True)
# keyboard.add_hotkey('8', lambda: print('8'), suppress=True)
# keyboard.add_hotkey('9', lambda: print('9'), suppress=True)
# keyboard.add_hotkey('0', lambda: print('0'), suppress=True)
# keyboard.add_hotkey('enter', lambda: print('enter'), suppress=True)

# Blocks until you press esc.
keyboard.wait('esc')


