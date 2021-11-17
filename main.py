#   a123_apple_1.py
import turtle
import random

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = turtle.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
apple = turtle.Turtle()
apple2 = turtle.Turtle()
apple3 = turtle.Turtle()
apple4 = turtle.Turtle()
apple5 = turtle.Turtle()
drawer = turtle.Turtle()
drawer.hideturtle()
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = []
num_of_apples = 0
n = 0
apple.speed(0)
drawer.speed(0)
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file

def draw_apple(active_apple):
  global num_of_apples
  x = random.randint(-250, 250)
  y = random.randint(-150, 150)
  active_apple.shape(apple_image)
  active_apple.up()
  active_apple.goto(x, y)
  active_apple.down()
  draw_an_letter(x, y)

  num_of_apples = num_of_apples + 1

def drop_apple():
  apple.up()
  drawer.hideturtle()
  drawer.clear()
  apple.goto(0,-160)
  apple.down()

def randomlettergen():
  num = random.randint(0, 25)
  return num

def draw_an_letter(x, y):
  randomletter = randomlettergen()
  drawer.up()
  drawer.goto(x-18,y-40)
  drawer.down()
  drawer.color("white")
  drawer.write(letters[randomletter], font=("Arial", 40, "bold"))
  numbers.append(randomletter)

#-----function calls-----

draw_apple(apple)
num = str(numbers[n])
num = int(num)
wn.onkeypress(drop_apple, letters[num])
n = n + 1

draw_apple(apple2)
num = str(numbers[n])
num = int(num)
wn.onkeypress(drop_apple, letters[num])
n = n + 1

draw_apple(apple3)
num = str(numbers[n])
num = int(num)
wn.onkeypress(drop_apple, letters[num])
n = n + 1

draw_apple(apple4)
num = str(numbers[n])
num = int(num)
wn.onkeypress(drop_apple, letters[num])
n = n + 1

draw_apple(apple5)
num = str(numbers[n])
num = int(num)
wn.onkeypress(drop_apple, letters[num])
n = n + 1

wn.mainloop()
