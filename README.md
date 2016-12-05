# EXAM: Python Basics

### Getting Started
 - Fork this repository under your own account
 - Clone the forked repository to your computer
 - Commit your progress frequently and with descriptive commit messages
 - All your answers and solutions should go in this repository

### What can I use?
- You can use any resource online, but **please work individually**
- **Don't just copy-paste** your answers and solutions, use your own words instead.


# Tasks
## 1-5. Complete the tasks seen in the first-fifth.py files! (~120 mins)
### Acceptance criteria
The application is accepted if:
- The solution works according to specification [1p each]
- Has proper error handling where the specification says it [1p each]
- Has the correct loops, methods, filters [1p each]
- The code is clean, without unnecessary repetition, and with descriptive names [1p each]
- You commit frequently, after each task, with descriptive commit messages [1p]
- The solution follows [styleguide](https://github.com/greenfox-academy/teaching-materials/blob/master/styleguide/python.md) [1p]

## 6. Question time! (~30 mins) [6p]

### Explain the algorithm seen in `third.py`. Use a flowchart, structogram or pseudo code. [2p]
#### Your answer:First it checks if the string parameter is actually a string, if its not it returns 0, if it's a string goes in a for loop all the way in the string, and if our letter is equals the current letter in the string we increment our number.

### How can you create a graphical user interface and draw a rectangle on it in python? What are the tools needed for it? [2p]
#### Your answer: First you need the tkinter module. Then you have to create a canvas, where you draw your rectangle (you need a mainloop so your canvas stays on the screen). You can draw a rectangle by creating a polygon with 3 points (canvas.create_polygon(), giving each point with x, y coords). Example:
###from tkinter import *
###root = Tk()\nsize = 400
###canvas = Canvas(root, width = size, height = size)
###canvas.pack()
###canvas.create_polygon(0, 0, 2, 2, 0, 2)
###root.mainloop()


### What does V stand for in MVC? [2p]
#### Your answer: The V in MVC stands for "View". In the standard MVC model you put everything in your View that is responsible for the visualization, so what the user sees.
