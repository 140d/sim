import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Physics Engine")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Ball class
class Ball:
    def __init__(self, x, y, radius, dx=0, dy=0, color=BLUE):
        self.x, self.y, self.radius = x, y, radius
        self.dx, self.dy, self.color = dx, dy, color

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def apply_gravity(self, gravity=0.2):
        self.dy += gravity  # Apply gravity to vertical velocity

    def bounce(self, width, height):
        # Bounce off left and right walls
        if self.x <= self.radius or self.x >= width - self.radius:
            self.dx *= -1

        # Bounce off top wall
        if self.y <= self.radius:
            self.dy *= -1

        # Handle bouncing off the bottom
        if self.y >= height - self.radius:
            self.y = height - self.radius  # Correct position to avoid going under the ground
            self.dy *= -0.9  # Apply damping to vertical velocity when bouncing off the floor

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Create a few balls with initial positions and velocities
balls = [
    Ball(random.randint(100, 300), random.randint(100, 300), radius=20, dx=2, dy=3, color=RED),
    Ball(random.randint(400, 600), random.randint(100, 300), radius=25, dx=-3, dy=2, color=GREEN),
    Ball(random.randint(300, 500), random.randint(400, 500), radius=15, dx=1, dy=-2, color=BLUE)
]

# Main game loop
def game_loop():
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(WHITE)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        # Update and render all balls
        for ball in balls:
            ball.apply_gravity()
            ball.move()
            ball.bounce(WIDTH, HEIGHT)
            ball.draw(screen)

        pygame.display.flip()  # Update the display

        # Set FPS
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Run the game loop
game_loop()
