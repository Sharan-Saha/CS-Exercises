def processString(old):
    new_string = ""
    for letter in old: 
        if letter.upper() == 'A':
            new_string += "B"
        if letter.upper() =="B":
            new_string += "AB"
        else:
            new_string += letter

    return new_string
    
def createLSystem(iters, axiom):
    end_string = ""
    for i in range(iters):
        end_string = processString(axiom)
        axiom = end_string
    return end_string
def main():
    result = createLSystem(30, "a")
    print(result)

main()