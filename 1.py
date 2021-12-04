def partone():
    lines = []
    with open('INSERT PATH HERE') as f:
        lines = f.readlines()
    
    increaseCounter = 0
    cur = -1
    last = -1
    for line in lines:
        cur = int(line)
        if last == -1:
            last = cur
        if last < cur:
            increaseCounter += 1
        last = cur
    print(increaseCounter)

def parttwo():
    lines = []
    with open('INSERT PATH HERE') as f:
        lines = f.readlines()
    
    increaseCounter = 0
    cur = -1
    last = -1

    for i in range(len(lines)):

        if i > 1:
            cur = int(lines[i-2]) + int(lines[i-1]) + int(lines[i])
            if last == -1:
                last = cur
            if last < cur:
                increaseCounter += 1
            last = cur
    print(increaseCounter)

parttwo()