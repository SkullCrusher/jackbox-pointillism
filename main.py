import time
import win32api
import win32con
from pynput.mouse import Button, Controller

print("Jackbox - Pointillism bot")
print("Waiting 10 seconds before starting. Put mouse on top left of canvas.")

# Delay so get the correct window setup.
time.sleep(10)


def getMousePosition():
    mouse = Controller()
    current_mouse_position = mouse.position
    return current_mouse_position


# Get the mouse position to base everything off.
base_position = getMousePosition()

# Alias out the variables.
base_x = base_position[0]
base_y = base_position[1]

print("Top left position is x={0},y={1}".format(base_x, base_y))
print("Starting to draw '{0}'.".format("sample.png"))


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


for i in range(0, 10):
    click(base_x + i * 25, base_y)



# click(10,10)

