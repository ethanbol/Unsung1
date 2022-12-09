import copy, random, sys, time

Width = 79  #grid width
Height = 20  #grid length

Alive = '0'  #living cell
Dead = ' '  # dead cell

nextcells = {}

for x in range(Width):
    for y in range(Height):
        if random.randint(0, 1) == 0:
            nextcells[(x, y)] = Alive
        else:
            nextcells[(x, y)] = Dead
while True:
    print('\n' * 50)
    cells = copy.deepcopy(nextcells)

for y in range(Height):
    for x in range(Width):
        print(cells[(x, y)], end='')
    print()
print("press Ctrl-C to quit.")

for x in range(Width):
    for y in range(Height):
        left = (x - 1) % Width
        right = (x + 1) % Width
        above = (y - 1) % Height
        below = (y + 1) % Height
        numNeighbors = 0
        if cells[(left, above)] == Alive:
            numNeighbors += 1
        if cells[(x, above)] == Alive:
            numNeighbors += 1
        if cells[(right, above)] == Alive:
            numNeighbors += 1
        if cells[(left, y)] == Alive:
            numNeighbors += 1
        if cells[(right, y)] == Alive:
            numNeighbors += 1
        if cells[(left, below)] == Alive:
            numNeighbors += 1
        if cells[(x, below)] == Alive:
            numNeighbors += 1
        if cells[(right, below)] == Alive:
            numNeighbors += 1

        if cells[(x, y)] == Alive and (numNeighbors == 2 or numNeighbors == 3):
            nextcells[(x, y)] = Alive

        elif cells[(x, y)] == Dead and numNeighbors == 3:
            nextcells[(x, y)] = Alive
        else:
            nextcells[(x, y)] = Dead
try:
    time.sleep(1)
except KeyboardInterrupt:
    print("Conyays Game of Life ")
    print("by Al Swiegart")
    sys.exit()
