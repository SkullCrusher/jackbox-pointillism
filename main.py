import time
import win32api
import win32con
from pynput.mouse import Button, Controller
from PIL import Image

image = "./sample.png"
delay = 2

colors = [
    [0, 0, 0],       # black
    [243, 41, 56],   # red
    [255, 165, 0],   # orange
    [248, 230, 85],  # yellow
    [68, 213, 68],   # green
    [0, 70, 174],    # blue
    [188, 77, 248],  # purple
    [99, 74, 44],    # brown
    [255, 255, 255]  # white
]

# Width is 580x580.
canvas_height_width = 50  # 570

# DPI - how many pixels in between each.
dpi = 10

# Resize the image to fit in our resolution.
resize_width = canvas_height_width // dpi
resize_height = canvas_height_width // dpi


def load_image(path):
    tmp = Image.open(path)
    return tmp.resize((resize_width, resize_height), resample=Image.BILINEAR, box=None)


picture = load_image(image)

print("Jackbox - Pointillism bot")
print("Waiting 10 seconds before starting. Put mouse on top left of canvas.")

# Delay so get the correct window setup.
time.sleep(delay)


def get_mouse_position():
    mouse = Controller()
    current_mouse_position = mouse.position
    return current_mouse_position


# Get the mouse position to base everything off.
base_position = get_mouse_position()

# Alias out the variables.
base_x = base_position[0]
base_y = base_position[1]

print("Top left position is x={0},y={1}".format(base_x, base_y))
print("Starting to draw '{0}'.".format(image))


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


# r, g, b = rgb_im.getpixel((1, 1))

# for i in range(0, 10):
#    click(base_x + i * 25, base_y)

# click(10,10)

def draw_image(image):

    # Map each pixel.
    for color in colors:
        for x in range(0, int(resize_height)):
            for y in range(0, int(resize_width)):

                print("color", color)

                # Skip if it's not the right color.

                # Generate the position to click.
                click_x = base_x + (x * dpi)
                click_y = base_y + (y * dpi)

                # Click on the position.
                click(click_x, click_y)

                # time.sleep(0.1)

                # If the cancel key is on, exit.
                if win32api.GetAsyncKeyState(win32con.VK_CAPITAL) == 1:
                    print("Close key pressed! Force closing.")
                    quit()


draw_image(picture)
