from pynput import keyboard, mouse

# Initialize mouse controller
mouse_controller = mouse.Controller()


# Movement step in pixels
STEP = 10

def on_press(key):
    try:
        x, y = mouse_controller.position

        if key == keyboard.Key.up:
            mouse_controller.position = (x, y - STEP)
        elif key == keyboard.Key.down:
            mouse_controller.position = (x, y + STEP)
        elif key == keyboard.Key.left:

            mouse_controller.position = (x - STEP, y)
        elif key == keyboard.Key.right:
            mouse_controller.position = (x + STEP, y)
        elif key == keyboard.Key.enter:
            mouse_controller.click(mouse.Button.left)

    except AttributeError:
        pass


    if key == keyboard.Key.esc:
        print("Exiting...")

        return False

print("Use arrow keys to move the mouse cursor.")

print("Press ENTER to left-click.")
print("Press ESC to quit.")



# Start listening to keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()






