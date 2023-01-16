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
        self.startAliveAnimation()
    
    def startAliveAnimation(self):
        # Mark pet as alive
        self.isDeceased = False
        
        # Create a Tkinter window by instantantiating a tk.Toplevel() object, which we will then be inserting under the window attribute
        self.window = tk.Toplevel()
        
        # Make window frameless
        self.window.overrideredirect(True)

        # Make window appear on top of others (similar concept to z-index: 999/some very high value in CSS --> to determine stack order of elements)
        self.window.attributes("-topmost", True)

        # Create a Label widget as a container that can be used to store our image (it can also store text)
        # 'bd' refers to the border width or size belonging to the Label widget (in px)
        self.label = tk.Label(self.window, bd=0, bg="white")

        # KIV till further notice - Adding text to Entry widget (Not fully working atm)
        # entry = tk.Entry(self.window)
        # entry.pack()
        # entry.insert("end", "Hello world!")
        # entry.configure({"background": "white", "foreground": "red","font": ("Helvetica", 8)})

        # Turn 'white' background color into transparent color instead
        self.window.wm_attributes("-transparentcolor", "white")

        # Pass in the gif file (which is a collection of different frames/images). 
        # We then use a list comprehension to generate an array of PhotoImage widgets of our pet cat (each PhotoImage contains a particular frame/image), and
        # Then set the frame index to 0 initially & also set the current_image attribute to the initial frame index
        self.animation = [tk.PhotoImage(file="final-combined.gif",format = "gif -index %i" %(i)) for i in range(114)]
        self.frame_index = 0
        self.current_image = self.animation[self.frame_index]

        # We need a previous timestamp to check whether can we advance to the next frame/image for our cat.gif
        # time.time() returns the current time in seconds since the Epoch)
        self.previous_timestamp = time.time()

        # Generate random X,Y coordinates for your pet cat to spawn at (X: 1 to 1279 - random, Y: 608 - fixed)
        SCREEN_WIDTH = self.window.winfo_screenwidth()
        SCREEN_HEIGHT = self.window.winfo_screenheight()
        X_AXIS_LEFT_LIMIT = 0
        X_AXIS_RIGHT_LIMIT = 1280
        RANDOM_X_AXIS_START_POINT = random.randint(X_AXIS_LEFT_LIMIT + 1, X_AXIS_RIGHT_LIMIT - 1)
        FIXED_Y_AXIS_START_POINT = SCREEN_HEIGHT - 112
        print("Your screen dimensions: ", SCREEN_WIDTH, SCREEN_HEIGHT)
        print("Random X, Y starting points: ", RANDOM_X_AXIS_START_POINT, FIXED_Y_AXIS_START_POINT)

        # Save your randomly generated X,Y coordinates to the x_position and y_position attributes
        # Save the direction of your pet cat to the initial goRightNow = True and initial goLeftNow = False attributes
        self.x_position = int(RANDOM_X_AXIS_START_POINT)
        self.y_position = int(FIXED_Y_AXIS_START_POINT)
        self.goRightNow = True;
        self.goLeftNow = False;

        # Set your tkinter window of size 64x64 pixels to be spawned at the X,Y coordinates of (1 to 1279, 608) - random for X, fixed for Y
        self.window.geometry(f"64x64+{RANDOM_X_AXIS_START_POINT}+{FIXED_Y_AXIS_START_POINT}")

        # Add the image to our Label widget. Now our tkinter window will have the image of our pet cat.
        self.label.configure(image=self.current_image)

        # The .pack() method is used to help display the widget in the window.
        self.label.pack()

        # When mainloop() starts, we will run self.updateFramePosition() after 0ms
        self.window.after(0, self.updateFramePosition)

        # Start the mainloop
        self.window.mainloop()

    def startDeceasedAnimation(self):
        # Mark pet as deceased
        self.isDeceased = True

        # Create a Tkinter window by instantantiating a tk.Toplevel() object, which we will then be inserting under the windowTwo attribute
        self.windowTwo = tk.Toplevel()
        
        # Make window frameless
        self.windowTwo.overrideredirect(True)

        # Make window appear on top of others (similar concept to z-index: 999/some very high value in CSS --> to determine stack order of elements)
        self.windowTwo.attributes("-topmost", True)

        # Create a Label widget as a container that can be used to store our image (it can also store text)
        # 'bd' refers to the border width or size belonging to the Label widget (in px)
        self.label = tk.Label(self.windowTwo, bd=0, bg="white")

        # KIV till further notice - Adding text to Entry widget (Not fully working atm)
        # entry = tk.Entry(self.window)
        # entry.pack()
        # entry.insert("end", "Hello world!")
        # entry.configure({"background": "white", "foreground": "yellow","font": ("Helvetica", 6)})

        # Turn 'white' background color into transparent color instead
        self.windowTwo.wm_attributes("-transparentcolor", "white")

        # Pass in the gif file (which is a collection of different frames/images). 
        # We then use a list comprehension to generate an array of PhotoImage widgets of our pet cat (each PhotoImage contains a particular frame/image), and
        # Then set the frame index to 0 initially & also set the current_image attribute to the initial frame index
        self.animation = [tk.PhotoImage(file="final-combined.gif",format = "gif -index %i" %(i)) for i in range(114, 119)]
        self.frame_index = 0
        self.current_image = self.animation[self.frame_index]

        # We need a previous timestamp to check whether can we advance to the next frame/image for our cat.gif
        # time.time() returns the current time in seconds since the Epoch)
        self.previous_timestamp = time.time()

        # Generate random X,Y coordinates for your pet cat to spawn at (X: 1 to 1279 - random, Y: 608 - fixed)
        SCREEN_WIDTH = self.windowTwo.winfo_screenwidth()
        SCREEN_HEIGHT = self.windowTwo.winfo_screenheight()
        X_AXIS_LEFT_LIMIT = 0
        X_AXIS_RIGHT_LIMIT = 1280
        RANDOM_X_AXIS_START_POINT = random.randint(X_AXIS_LEFT_LIMIT + 1, X_AXIS_RIGHT_LIMIT - 1)
        FIXED_Y_AXIS_START_POINT = SCREEN_HEIGHT - 112
        print("Your screen dimensions: ", SCREEN_WIDTH, SCREEN_HEIGHT)
        print("Random X, Y starting points: ", RANDOM_X_AXIS_START_POINT, FIXED_Y_AXIS_START_POINT)

        # Save your randomly generated X,Y coordinates to the x_position and y_position attributes
        # Save the direction of your pet cat to the initial goRightNow = True and initial goLeftNow = False attributes
        self.x_position = int(RANDOM_X_AXIS_START_POINT)
        self.y_position = int(FIXED_Y_AXIS_START_POINT)
        self.goRightNow = True;
        self.goLeftNow = False;

        # Set your tkinter window of size 64x64 pixels to be spawned at the X,Y coordinates of (1 to 1279, 608) - random for X, fixed for Y
        self.windowTwo.geometry(f"64x64+{RANDOM_X_AXIS_START_POINT}+{FIXED_Y_AXIS_START_POINT}")

        # Add the image to our Label widget. Now our tkinter windowTwo will have the image of our pet cat.
        self.label.configure(image=self.current_image)

        # The .pack() method is used to help display the widget in the window.
        self.label.pack()

        # When mainloop() starts, we will run self.updateFramePosition() after 0ms
        self.windowTwo.after(0, self.updateFramePosition)

        # Start the mainloop
        self.windowTwo.mainloop()

    def reachedLeftEdge(self):
        return self.x_position <= 0

    def reachedRightEdge(self):
        return self.x_position >= 1280

    def reachedInBetweenEdges(self):
        return self.x_position > 0 and self.x_position < 1280

    def generateNextFrame(self):
        # Advance to the next frame/image if 100ms have passed & we loop back to 1 once last frame is reached
        current_timestamp = time.time()
        if current_timestamp > self.previous_timestamp + 0.100:
            self.previous_timestamp = time.time()
            # Cat.gif has 119 frames (114 frames healthy animation, 5 frames deceased animation)
            if (self.isDeceased):
                self.frame_index = (self.frame_index + 1) % 5
            else:
                self.frame_index = (self.frame_index + 1) % 114
            self.current_image = self.animation[self.frame_index]

        # Set your tkinter window of size 64x64 pixels to be spawned at the random coordinates for X, fixed for Y
        self.window.geometry(f"64x64+{self.x_position}+{self.y_position}")

        # Add the image to our label again
        self.label.configure(image=self.current_image)
        
        # The .pack() method is used to help display the widget in the window.
        self.label.pack()

        # Call updateFramePosition() again after 10ms
        self.window.after(10, self.updateFramePosition)

        # If not deceased:
        #   For demo, call switchToDeceasedAnimation() after 6 seconds (for demo purposes)
        #   For actual product, call switchToDeceasedAnimation() to prompt user to rest after 20 minutes based on 'American Optometric Association' 20-20-20 guidelines (Every 20mins, look at something 20ft away for 20 seconds)
        # not self.isDeceased and self.window.after(6000, self.switchToDeceasedAnimation)
        not self.isDeceased and self.window.after(1200000, self.switchToDeceasedAnimation)

    def updateFramePosition(self):
        reached_left_screen_edge = self.reachedLeftEdge()
        reached_right_screen_edge = self.reachedRightEdge()
        reached_in_between_edges = self.reachedInBetweenEdges()

        if (reached_left_screen_edge):
            # Once you hit the left edge of the screen, move to the right by one px
            self.goRightNow = True
            self.goLeftNow = False;
            self.x_position += 1
            self.generateNextFrame()
        elif (reached_right_screen_edge):
            # Once you hit the right edge of the screen, move to the left by one px
            self.goLeftNow = True
            self.goRightNow = False;
            self.x_position -= 1
            self.generateNextFrame()
        elif (reached_in_between_edges and self.goRightNow):
            # In between the left and right edges of the screen, move in accordance to direction of goRightNow or goLeftNow
            self.x_position += 1
            self.generateNextFrame()
        else:
            # In between the left and right edges of the screen, move in accordance to direction of goRightNow or goLeftNow
            self.x_position -= 1
            self.generateNextFrame()
    
    def switchToDeceasedAnimation(self):
        # Hide previous instance
        self.window.withdraw()
        
        # Create new instance & switch to deceased animation
        self.startDeceasedAnimation()

if __name__ == '__main__':
    PyCat()
