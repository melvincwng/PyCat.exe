'''
    This is a Python script that will display a pet cat on your desktop that will move around your screen. It will act as a:
        1. Desktop companion
        2. Eye-straining prevention tool
    We are using tkinter library which is a GUI library for Python.
'''

import tkinter as tk
import time
import random

class PyCat():
    def __init__(self):
        # Create a Tkinter window by instantantiating a tk.Tk() object, which we will then be inserting under the window attribute
        self.window = tk.Tk()
        
        # Make window frameless
        self.window.overrideredirect(True)

        # Make window appear on top of others (similar concept to z-index: 999/some very high value in CSS --> to determine stack order of elements)
        self.window.attributes('-topmost', True)

        # Create a Label widget as a container that can be used to store our image (it can also store text)
        # 'bd' refers to the border width or size belonging to the Label widget (in px)
        self.label = tk.Label(self.window, bd=0, bg='white')

        # Turn 'white' background color into transparent color instead
        self.window.wm_attributes('-transparentcolor', 'white')

        # Pass in the gif file (which is a collection of different frames/images). 
        # We then use a list comprehension to generate an array of PhotoImage widgets of our pet cat (each PhotoImage contains a particular frame/image), and
        # Then set the frame index to 0 initially & also set the current_image attribute to the initial frame index
        self.alive_animation = [tk.PhotoImage(file='alive.gif',format = 'gif -index %i' %(i)) for i in range(114)]
        self.frame_index = 0
        self.current_image = self.alive_animation[self.frame_index]

        # We need a previous timestamp to check whether can we advance to the next frame/image for our cat.gif
        # time.time() returns the current time in seconds since the Epoch)\
        self.previous_timestamp = time.time()

        # Generate random X,Y coordinates for your pet cat to spawn at (X: 0 to 1280 - random, Y: 608 - fixed)
        SCREEN_WIDTH = self.window.winfo_screenwidth()
        SCREEN_HEIGHT = self.window.winfo_screenheight()
        X_AXIS_LEFT_LIMIT = 0
        X_AXIS_RIGHT_LIMIT = 1280
        RANDOM_X_AXIS_START_POINT = random.randint(X_AXIS_LEFT_LIMIT, X_AXIS_RIGHT_LIMIT)
        FIXED_Y_AXIS_START_POINT = SCREEN_HEIGHT - 112
        print("Your screen dimensions: ", SCREEN_WIDTH, SCREEN_HEIGHT)
        print("Random X, Y starting points: ", RANDOM_X_AXIS_START_POINT, FIXED_Y_AXIS_START_POINT)

        # Save your randomly generated X,Y coordinates to the x_position and y_position attributes
        self.x_position = int(RANDOM_X_AXIS_START_POINT)
        self.y_position = int(FIXED_Y_AXIS_START_POINT)

        # Set your tkinter window of size 64x64 pixels to be spawned at the X,Y coordinates of (0 to 1280, 608) - random for X, fixed for Y
        self.window.geometry(f"64x64+{RANDOM_X_AXIS_START_POINT}+{FIXED_Y_AXIS_START_POINT}")

        # # Add the image to our Label widget. Now out tkinter window will have the image of our pet cat.
        self.label.configure(image=self.current_image)

        # The .pack() method is used to help display the widget in the window.
        self.label.pack()

        # Execute tkinter
        self.window.mainloop()
  
        # Move to the right by one px
        self.x_position += 1

        # Advance to the next frame/image if 125ms have passed
        current_timestamp = time.time()
        if current_timestamp > self.previous_timestamp + 0.125:
            self.previous_timestamp = time.time()
            # advance the frame by one, wrap back to 0 at the end
            self.frame_index = (self.frame_index + 1) % 114
            self.current_image = self.alive_animation[self.frame_index]

        # Create the window
        self.window.geometry(f"64x64+{self.x_position}+{self.y_position}")
        # Add the image to our label
        self.label.configure(image=self.current_image)
        # Give window to geometry manager (so it will appear)
        self.label.pack()

        # Call updateFrame() again after 150ms
        self.window.after(125, self.updateFrame)
if __name__ == '__main__':
    PyCat()