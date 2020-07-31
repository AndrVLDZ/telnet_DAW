import subprocess
# (library) source: https://github.com/boppreh/keyboard
# pip install keyboard
import keyboard

def start_DAW():
    """Documentation"""
    DAW_PATH = 'C:\Program Files\PreSonus\Studio One 4\\Studio One.exe'
    # Open my music editor
    subprocess.Popen([DAW_PATH])
    # Trigger keyboard on machine. Make all keypress
    # aka `SPACEBARR.press()`
    keyboard.send('space', do_press=True, do_release=True)

if __name__ == "__main__":
    start_DAW()