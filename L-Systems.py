import turtle

def processString(old):
    new = ""
    for ch in old:
        if ch == "F":
            new += "F-F++F-F"
        else:
            new += ch
    return new
def createLSystem(i, a):
    for i in range(i):
        a = processString(a)
    return a

def drawLSystem(pattern):
    wn = turtle.Screen()
    mike = turtle.Turtle()
    mike.shape("turtle")
    mike.color("pink")
    mike.speed(10)

    for ins in pattern:
        if ins == "F":
            mike.forward(15)
        elif ins == "-":
            mike.left(90)
        elif ins == "+":
            mike.right(90)

    wn.exitonclick()

def main():
    axiom = 'F'
    rule = ['F', 'F-F++F-F']
    iters = int(input("Num iters?: "))
    result = createLSystem(iters, axiom)
    print(result)
    
    drawLSystem(result)

main()


