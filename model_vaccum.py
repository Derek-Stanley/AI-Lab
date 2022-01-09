state = { 'A' : -1, 'B' : -1,}
env = { 'A' : 1, 'B' : 1,}

Loc = 'A'

def move():
    global Loc 
    if Loc == 'A':
        print('Moving to B\n')
        Loc = 'B'
    else:
        print('Moving to A\n')
        Loc = 'A'

def sense():
    env[Loc] = state[Loc]

def addDirt():
    for pos in 'A' 'B':
        d = input("Add dirt on " + pos)
        env[Loc] = 1


def main():
    start = input("Start cleaning (yes\\no) : ")
    if start == 'yes':
        while state['A'] and state['B']:
            print("At location " + Loc)
            sense()

            if  state[Loc]:
                print("Dirt found!")
                print("Operation : Cleaning \nDone!")
                state[Loc] = 0
                env[Loc] = 0
            else:
                print("No dirt found")
            move()
            if Loc == 'A':
                addDirt()
                sense()
            print(state['A'], state['B'], sep=" ")

main()
        



