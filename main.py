import pygame, random
from square import *

def setup(winSize):
    global screen, clock, font, screenSize
    pygame.init()
    if winSize == 'fullscreen':
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, vsync=1)
        screenSize = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    else:
        screen = pygame.display.set_mode(winSize, vsync=1)
        screenSize = winSize

    pygame.display.set_caption('Car')
    pygame.SCALED = True
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('arial', 50)

inputs = [False, False, False, False]

resolution = 50

grid = []

setup((500, 500))
playerPos = resolution**2 - resolution/2

# objects = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
#            ' ', ' ', ' ', 'X', 'X', ' ', ' ', ' ', ' ', ' ',
#            ' ', ' ', 'G', ' ', ' ', ' ', 'X', ' ', ' ', ' ',
#            ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ',
#            ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ',
#            ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ',
#            ' ', ' ', 'X', 'X', 'X', 'X', 'X', ' ', ' ', ' ',
#            ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ',
#            ' ', ' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ',
#            ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
# ]
objects = []
for i in range(resolution**2):
    if i == resolution / 2:
        objects.append('G')
    elif random.randint(0, 3) == 0:
        objects.append('X')
    else:
        objects.append(' ')
    

def createGrid():
    grid.clear()
    for y in range(resolution):
        for x in range(resolution):
            if y*resolution + x == playerPos:
                grid.append(Square(x*screenSize[0]//resolution, y*screenSize[1]//resolution, screenSize[0]//resolution, screenSize[1]//resolution, 0))
            else:
                grid.append(Square(x*screenSize[0]//resolution, y*screenSize[1]//resolution, screenSize[0]//resolution, screenSize[1]//resolution, objects[y*resolution + x]))



def relPos(square):
    return [grid.index(square) - resolution, grid.index(square) + resolution, grid.index(square) - 1, grid.index(square) + 1]

def find(square):
    global searchDone
    positions = relPos(square)

    for i, position in enumerate(positions):
        if position < len(grid) and position >= 0:                   # eliminate out of map positions
            if grid[position].type != 'X' and grid[position].type != 'l':         # eliminate walls
                if grid[position].type == 'G':
                    grid[position].type = 'lineFront'
                    searchDone = True
                if grid[position].type == ' ':
                    if i == 0 or i == 1:
                        grid[position].type = n + 1
                    else:
                        if grid[position].y == square.y:
                            grid[position].type = n + 1

searchDone = False
finished  = False

def path(square):
    global finished
    positions = relPos(square)
    lowest = 999
    lowestPos = None

    for position in positions:
        if position < len(grid) and position >= 0:
            if isinstance(grid[position].type, int):
                if grid[position].type < lowest:
                    lowest = grid[position].type
                    lowestPos = position
            
    if lowestPos and grid[lowestPos].type != 0:
        grid[lowestPos].type = 'lineFront'
        square.type = 'l'
    else:
        finished = True


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                break
            if event.key == pygame.K_UP or event.key == ord('w'):
                inputs[0] = True

            if event.key == pygame.K_DOWN or event.key == ord('s'):
                inputs[1] = True

            if event.key == pygame.K_LEFT or event.key == ord('a'):
                inputs[2] = True

            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                inputs[3] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == ord('w'):
                inputs[0] = False

            if event.key == pygame.K_DOWN or event.key == ord('s'):
                inputs[1] = False

            if event.key == pygame.K_LEFT or event.key == ord('a'):
                inputs[2] = False

            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                inputs[3] = False
                
    screen.fill((0, 0, 0))

    n = 0
    searchDone = False
    finished  = False
    createGrid()
    while not finished:
        if searchDone:
            comp = False
            for square in grid:
                if square.type == 'lineFront' and not comp:
                    path(square)
                    comp = True
        else:
            for square in grid:
                if square.type == n:
                    find(square)
            n += 1

    for square in grid:
        if square.type == 'lineFront':
            square.type = 'l'
        elif square.type == 0:
            positions = relPos(square)
            if inputs[0]:
                if positions[0] < len(grid) and positions[0] >= 0:
                    if isinstance(grid[positions[0]].type, int):
                        playerPos -= resolution
                    elif grid[positions[0]].type == ' ' or grid[positions[0]].type == 'l' or grid[positions[0]].type == 'lineFront':
                        playerPos -= resolution

            elif inputs[1]:
                if positions[1] < len(grid) and positions[1] >= 0:
                    if isinstance(grid[positions[1]].type, int):
                        playerPos += resolution
                    elif grid[positions[1]].type == ' ' or grid[positions[1]].type == 'l' or grid[positions[1]].type == 'lineFront':
                        playerPos += resolution

            elif inputs[2]:
                if positions[2] < len(grid) and positions[2] >= 0:       
                    if isinstance(grid[positions[2]].type, int):
                        playerPos -= 1
                    elif grid[positions[2]].type == ' ' or grid[positions[2]].type == 'l' or grid[positions[2]].type == 'lineFront':
                        playerPos -= 1

            elif inputs[3]:
                if positions[3] < len(grid) and positions[3] >= 0:
                    if isinstance(grid[positions[3]].type, int):
                        playerPos += 1
                    elif grid[positions[3]].type == ' ' or grid[positions[3]].type == 'l' or grid[positions[3]].type == 'lineFront':
                        playerPos += 1

        square.display(screen, font)


    pygame.display.flip()
    clock.tick(10)