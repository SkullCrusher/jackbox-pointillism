import time
import win32api
import win32con
from pynput.mouse import Button, Controller
from PIL import Image
from math import sqrt

# 8 is kinda okay
# 7 is LIT

image = "./sample7.png"  # "example2.jpg"  #
delay = 2

colors = (
    (0, 0, 0),       # black
    (243, 41, 56),   # red
    (255, 165, 0),   # orange
    (248, 230, 85),  # yellow
    (68, 213, 68),   # green
    (0, 70, 174),    # blue
    (188, 77, 248),  # purple
    (99, 74, 44),    # brown
    (255, 255, 255)  # white
)

# The color location in relationship to the top left.
color_offset_x = 305
color_offset_y = -35

# How many pixels are inbetween each color
color_space = 33

# Width is 580x580.
canvas_height_width = 595

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


def pick_color(index):
    time.sleep(0.5)
    click_x = base_x + color_offset_x + (index * color_space)
    click_y = base_y + color_offset_y
    click(click_x, click_y)
    time.sleep(0.5)


def closest_color(r, g, b):
    color_diffs = []
    for color in colors:
        cr, cg, cb = color
        color_diff = sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]


def draw_image(image):
    image.show()

    # Map each pixel.
    for i in range(0, len(colors)):
        pick_color(i)

        c_r = colors[i][0]
        c_g = colors[i][1]
        c_b = colors[i][2]

        for x in range(0, int(resize_height)):
            for y in range(0, int(resize_width)):

                # Get the color of the pixel.
                r, g, b = image.getpixel((x, y))

                # Pick from our list.
                picked = closest_color(r, g, b)

                # Only color in the color that match (to keep from changing colors constantly).
                if picked[0] != c_r or picked[1] != c_g or picked[2] != c_b:
                    continue

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
