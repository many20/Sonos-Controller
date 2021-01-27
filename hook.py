import keyboard

# keyboard.press_and_release('shift+s, space')

# keyboard.write('The quick brown fox jumps over the lazy dog.')

# keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))

# # Press PAGE UP then PAGE DOWN to type "foobar".
# keyboard.add_hotkey('4', lambda: keyboard.write('#4'))

# # Blocks until you press esc.
# keyboard.wait('esc')

# # Record events until 'esc' is pressed.
# recorded = keyboard.record(until='esc')
# # Then replay back at three times the speed.
# keyboard.play(recorded, speed_factor=3)

# # Type @@ then press space to replace with abbreviation.
# keyboard.add_abbreviation('@@', 'my.long.email@example.com')

# # Block forever, like `while True`.
# keyboard.wait()

keyboard.add_hotkey('1', lambda: print('#1'))
keyboard.add_hotkey('2', lambda: print('#2'))
keyboard.add_hotkey('3', lambda: print('#3'))
keyboard.add_hotkey('4', lambda: print('#4'))

# # Blocks until you press esc.
keyboard.wait('esc')

print('start')
