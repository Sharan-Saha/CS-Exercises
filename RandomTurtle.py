import random 
import turtle
def isInScreen(screen, turtle):
    left = -(screen.window_width() / 2)
    right = screen.window_width() / 2
    top = screen.window_height() / 2
    bottom = -(screen.window_height() / 2)

    x = turtle.xcor()
    y = turtle.ycor()

    if x > right or x < left or y > top or y < bottom:
        return False
    else:
        return True
        
def main():
    t = turtle.Turtle()
    wn = turtle.Screen()
    t.shape('turtle')
    t.color('pink')
    while isInScreen(wn, t):
        coin = random.randrange(0,2)
        if coin: 
            t.left(90)
        else:
            t.right(90)
        t.forward(10)
        
main()
