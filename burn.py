import pygame
import random
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FIRE_COLORS = [(255, 100, 0), (255, 150, 50), (255, 50, 0)]
DECAY_RATE = 0.1
NPC_MOVE_RATE = 2
NPC_PANIC_RATE = 4

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Burning Simulation")

class FireParticle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = random.randint(5, 10)
        self.color = random.choice(FIRE_COLORS)
        self.lifespan = random.randint(20, 40)

    def update(self):
        """Move the particle upward and reduce its lifespan."""
        self.y -= random.randint(1, 3)
        self.radius -= 0.1
        self.lifespan -= 1

    def draw(self, screen):
        if self.radius > 0:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.radius))

class Fire:
    def __init__(self):
        self.particles = []
        self.max_particles = 100
        self.base_max_particles = 100
        self.heat = 0

    def add_particle(self):
        """Add a new particle at the base of the fire."""
        if len(self.particles) < self.max_particles:
            x = SCREEN_WIDTH // 2 + random.randint(-20, 20)
            y = SCREEN_HEIGHT - 100
            particle = FireParticle(x, y)
            self.particles.append(particle)

    def update(self):
        """Update all particles (movement, lifespan, etc.)."""
        self.add_particle()
        for particle in self.particles[:]:
            particle.update()
            if particle.lifespan <= 0:
                self.particles.remove(particle)
        if self.heat <= 0:
            self.max_particles = max(self.base_max_particles, self.max_particles - DECAY_RATE)
        else:
            self.heat -= 1

    def grow(self, amount):
        """Increase the maximum number of particles to simulate fire growth."""
        self.max_particles += amount
        self.heat += 10 * amount

    def draw(self, screen):
        """Draw all the particles to the screen."""
        for particle in self.particles:
            particle.draw(screen)

class Burnable:
    def __init__(self, x, y, width, height, burn_threshold):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (139, 69, 19)
        self.burning = False
        self.heat = 0
        self.burn_threshold = burn_threshold

    def absorb_heat(self, fire_heat):
        """Absorb heat from the fire."""
        if not self.burning:
            self.heat += fire_heat
            if self.heat >= self.burn_threshold:
                self.burning = True 

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def burn(self):
        """Simulate burning by shrinking the object."""
        if self.rect.height > 0:
            self.rect.height -= 1
class NPC:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 60)
        self.color = (0, 255, 0)
        self.burning = False
        self.burn_time = 0
        self.direction = random.choice(['left', 'right', 'up', 'down'])
        self.state = 'idle'
        self.idle_timer = random.randint(30, 60)
        self.panic = False

    def move(self):
        """Move the NPC in a random direction or idle, with boundary checks."""
        if self.panic:
            self.state = 'panic'
            speed = NPC_PANIC_RATE
        else:
            speed = NPC_MOVE_RATE

        if self.state == 'idle':
            self.idle_timer -= 1
            if self.idle_timer <= 0:
                self.state = 'walking'
            return

        if self.direction == 'left' and self.rect.left > 0:
            self.rect.x -= speed
        elif self.direction == 'right' and self.rect.right < SCREEN_WIDTH:
            self.rect.x += speed
        elif self.direction == 'up' and self.rect.top > 0:
            self.rect.y -= speed
        elif self.direction == 'down' and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += speed

        if random.randint(0, 100) < 2:
            self.direction = random.choice(['left', 'right', 'up', 'down'])
        if random.randint(0, 100) < 1:
            self.state = 'idle'
            self.idle_timer = random.randint(30, 60)

    def interact_with_fire(self, fire_rect):
        """NPC interacts with fire, has a 1 in 5 chance of catching fire."""
        if self.rect.colliderect(fire_rect) and not self.burning:
            if random.randint(1, 5) == 1:
                self.burning = True
                self.burn_time = 120
                self.panic = True

    def update(self):
        """Update NPC behavior."""
        if self.burning:
            self.burn_time -= 1
            if self.burn_time <= 0:
                self.burning = False
                self.panic = False
        self.move()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

fire = Fire()
burnables = []
npc = NPC(100, 100)

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            wood = Burnable(x, y, 40, 60, random.randint(30, 60))
            burnables.append(wood)

    fire_rect = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 100 - 50, 100, 100)

    npc.interact_with_fire(fire_rect)
    npc.update()

    for burnable in burnables:
        if burnable.rect.colliderect(fire_rect):
            burnable.absorb_heat(1)

        if burnable.burning:
            burnable.burn()
            fire.grow(2)

    fire.update()
    fire.draw(screen)

    for burnable in burnables:
        burnable.draw(screen)

    npc.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
