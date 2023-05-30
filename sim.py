import pygame
from constants import *
from maple import *
from squirrel import *

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maple Tree Simulator")

# Define the map (a simple 2D grid)
map_data = [[0 for i in range(MAP_WIDTH)] for i in range(MAP_HEIGHT)]

# Define arrays to hold entities
maples = []
squirrels = []

# Populate the map with some mature maples
for i in range(0, 50):
    new_maple = Maple()
    new_maple.age = new_maple.maturity
    map_data[new_maple.y][new_maple.x] = 1
    maples.append(new_maple)

# Populate the map with some squirrels
for i in range(0, 200):
    new_squirrel = Squirrel()
    map_data[new_squirrel.y][new_squirrel.x] = 3
    squirrels.append(new_squirrel)

# Main game loop
running = True
time = 0
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Print stats
    print('Time: {},\t Maples: {},\t Squirrels: {}'.format(time, len(maples), len(squirrels)))

    # First squirrel loop
    for squirrel in squirrels:
        # Death
        if squirrel.age >= squirrel.max_age:
            map_data[squirrel.y][squirrel.x] = 0
            squirrels.remove(squirrel)
            continue
        
        # Movement
        x = squirrel.x
        y = squirrel.y
        while x == squirrel.x or x < 0 or x >= MAP_WIDTH:
            x = random.randint(squirrel.x - 1, squirrel.x + 1)
        while y == squirrel.y or y < 0 or y >= MAP_HEIGHT:
            y = random.randint(squirrel.y - 1, squirrel.y + 1)
        # Remove the old squirrel spot
        map_data[squirrel.y][squirrel.x] = 0
        squirrel.x = x
        squirrel.y = y
        # Render the squirrel
        map_data[squirrel.y][squirrel.x] = 3

    # Render maples
    for maple in maples:
        # Maturity
        if maple.age < maple.maturity:
            map_data[maple.y][maple.x] = 1
        elif (maple.age >= maple.maturity):
            map_data[maple.y][maple.x] = 2

    # Handle maple behavior
    for maple in maples:
        # Death
        if maple.age >= maple.max_age:
            map_data[maple.y][maple.x] = 0
            maples.remove(maple)
            continue
        
        # Cast a seed at every maturity cycle
        if maple.age >= maple.maturity and time % SEED_CYCLE == 0:
            new_maples = maple.cast_seed(num = MAX_SEEDS_PER_CYCLE)
            for new in new_maples:
                if (map_data[new.y][new.x] != 1):
                    map_data[new.y][new.x] = 1
                    maples.append(new)
                        
        # Increment the age of the maple
        maple.increment_age()


    # Draw the map
    for row in range(MAP_HEIGHT):
        for col in range(MAP_WIDTH):
            tile = map_data[row][col]
            if tile == 0:
                pygame.draw.rect(screen, BLACK, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif tile == 1:
                pygame.draw.rect(screen, GREEN, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif tile == 2:
                pygame.draw.rect(screen, BROWN, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif tile == 3:
                pygame.draw.rect(screen, WHITE, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Update the display
    pygame.display.flip()

    # Increment the time
    time += 1

# Quit the game
pygame.quit()
