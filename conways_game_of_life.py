import copy, random, sys , time

Width = 79 #grid width
length = 20 #grid length

Alive = '0' #living cell
Dead = ' ' # dead cell

nextcells = {}

for x in range(Width):
  for y in range(length):
    if random.randint(0,1) == 0:
      nextcells[(x,y)] = Alive
    else:
      nextcells[(x,y)] = Dead
while True:
  