import pygame, math

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("140d Sim")

radius = 20


class Ball:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.dx, self.dy = 2, 3
        self.mass = radius

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def apply_gravity(self, gravity=0.2):
        self.dy += gravity

    def bounce(self, width, height):
        if self.x <= radius:
            self.x = radius
            self.dx *= -1
        elif self.x >= width - radius:
            self.x = width - radius
            self.dx *= -1

        if self.y <= radius:
            self.y = radius
            self.dy *= -1
        elif self.y >= height - radius:
            self.y = height - radius
            self.dy *= -0.9

    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (int(self.x), int(self.y)), radius, 3)
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), 3)

    def check_collision(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        distance = math.sqrt(dx**2 + dy**2)

        if distance < radius + radius:
            overlap = 0.5 * (radius + radius - distance)
            self.x -= overlap * (dx / distance)
            self.y -= overlap * (dy / distance)
            other.x += overlap * (dx / distance)
            other.y += overlap * (dy / distance)

            nx, ny = dx / distance, dy / distance

            tx, ty = -ny, nx

            dpTan1 = self.dx * tx + self.dy * ty
            dpTan2 = other.dx * tx + other.dy * ty

            dpNorm1 = self.dx * nx + self.dy * ny
            dpNorm2 = other.dx * nx + other.dy * ny

            m1, m2 = self.mass, other.mass
            v1 = (dpNorm1 * (m1 - m2) + 2 * m2 * dpNorm2) / (m1 + m2)
            v2 = (dpNorm2 * (m2 - m1) + 2 * m1 * dpNorm1) / (m1 + m2)

            self.dx = tx * dpTan1 + nx * v1
            self.dy = ty * dpTan1 + ny * v1
            other.dx = tx * dpTan2 + nx * v2
            other.dy = ty * dpTan2 + ny * v2


balls = [
    Ball(100, 400),
    Ball(200, 300),
    Ball(300, 200),
    Ball(400, 100),
]


def game_loop():
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill((160, 160, 160))

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                running = False

        for ball in balls:
            ball.apply_gravity()
            ball.move()
            ball.bounce(WIDTH, HEIGHT)

            ball.draw(screen)

        for i, ball in enumerate(balls):
            for other in balls[i + 1 :]:
                ball.check_collision(other)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


game_loop()
