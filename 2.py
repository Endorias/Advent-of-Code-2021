def partone():
    lines = []
    with open('INSERT PATH HERE') as f:
        lines = f.readlines()

    x = 0
    y = 0
    for line in lines:
        command = line.split(' ')

        
        if command[0] == 'forward':
            x = x + int(command[1])
            print("FORWARD")
        if command[0] == 'down':
            y = y + int(command[1])
            print("DOWN")
        if command[0] == 'up':
            y = y - int(command[1])
            print("UP")

    print(x)
    print(y)
    print(x*y)

def parttwo():
    lines = []
    with open('INSERT PATH HERE') as f:
        lines = f.readlines()

    x = 0
    y = 0
    aim = 0
    for line in lines:
        command = line.split(' ')

        
        if command[0] == 'forward':
            x = x + int(command[1])
            y = y + (aim * int(command[1]))
            print("FORWARD")
        if command[0] == 'down':
            aim = aim + int(command[1])
            print("DOWN")
        if command[0] == 'up':
            aim = aim - int(command[1])
            print("UP")

    print(x)
    print(y)
    print(x*y)

parttwo()