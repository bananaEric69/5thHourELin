import pygame
import random
import sys
pip install pygame

# Initialize Pygame
pygame.init()

# Set up the game window
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")

# Define colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Pac-Man class
class PacMan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 15
        self.color = YELLOW
        self.speed = 5

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Dot class
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 5
        self.color = WHITE

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Ghost class (Simple for now)
class Ghost:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.radius = 15
        self.color = color
        self.speed = 2

    def move(self):
        self.x += random.choice([-self.speed, self.speed])
        self.y += random.choice([-self.speed, self.speed])

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Initialize Pac-Man
pacman = PacMan(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Initialize dots
dots = [Dot(random.randint(20, SCREEN_WIDTH - 20), random.randint(20, SCREEN_HEIGHT - 20)) for _ in range(10)]

# Initialize ghosts
ghosts = [Ghost(random.randint(100, SCREEN_WIDTH - 100), random.randint(100, SCREEN_HEIGHT - 100), RED) for _ in range(2)]

# Game loop
def game_loop():
    clock = pygame.time.Clock()
    score = 0
    dx, dy = 0, 0
    running = True

    while running:
        screen.fill(BLACK)

        # Check for events (like quitting)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Handle key press for Pac-Man movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dx = -pacman.speed
            dy = 0
        elif keys[pygame.K_RIGHT]:
            dx = pacman.speed
            dy = 0
        elif keys[pygame.K_UP]:
            dx = 0
            dy = -pacman.speed
        elif keys[pygame.K_DOWN]:
            dx = 0
            dy = pacman.speed
        else:
            dx, dy = 0, 0

        # Move Pac-Man
        pacman.move(dx, dy)

        # Check for collision with dots
        for dot in dots[:]:
            if (pacman.x - dot.x) ** 2 + (pacman.y - dot.y) ** 2 <= (pacman.radius + dot.radius) ** 2:
                dots.remove(dot)
                score += 1

        # Check for collision with ghosts (simple collision detection)
        for ghost in ghosts:
            if (pacman.x - ghost.x) ** 2 + (pacman.y - ghost.y) ** 2 <= (pacman.radius + ghost.radius) ** 2:
                running = False  # End the game if Pac-Man touches a ghost

        # Move ghosts
        for ghost in ghosts:
            ghost.move()

        # Draw Pac-Man, dots, and ghosts
        pacman.draw()

        for dot in dots:
            dot.draw()

        for ghost in ghosts:
            ghost.draw()

        # Display the score
        font = pygame.font.SysFont("Arial", 20)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.update()

        # Set the frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Start the game
if __name__ == "__main__":
    game_loop()

python pacman.py