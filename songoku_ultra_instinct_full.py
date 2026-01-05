import pygame
import sys
import math
import random

pygame.init()

WIDTH, HEIGHT = 900, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SONGOKU – ULTRA INSTINCT (FULL)")

clock = pygame.time.Clock()

# ===== COLORS =====
BLACK = (10, 10, 20)
WHITE = (245, 245, 245)
SILVER = (220, 220, 220)
BLUE = (120, 200, 255)
DARK_BLUE = (40, 120, 255)
GRAY = (160, 160, 160)

cx, cy = WIDTH // 2, HEIGHT // 2 - 60

# ===== AURA PARTICLES =====
aura_particles = []
for _ in range(120):
    aura_particles.append({
        "angle": random.uniform(0, 2 * math.pi),
        "radius": random.randint(90, 150),
        "speed": random.uniform(0.01, 0.03)
    })


def draw_aura(surface, x, y, frame):
    for p in aura_particles:
        p["angle"] += p["speed"]
        r = p["radius"] + math.sin(frame * 0.1) * 10
        ax = x + math.cos(p["angle"]) * r
        ay = y + math.sin(p["angle"]) * r

        pygame.draw.circle(surface, BLUE, (int(ax), int(ay)), 4)
        pygame.draw.circle(surface, DARK_BLUE, (int(ax), int(ay)), 8, 1)


def draw_hair(surface, x, y, frame):
    sway = math.sin(frame * 0.08) * 4
    spikes = [
        (-60, -120), (-40, -170), (-20, -130),
        (0, -190), (20, -130), (40, -170),
        (60, -120)
    ]
    for sx, sy in spikes:
        pygame.draw.polygon(
            surface,
            SILVER,
            [
                (x, y - 20),
                (x + sx, y + sy + sway),
                (x + sx // 2, y - 10)
            ]
        )


def draw_face(surface, x, y):
    pygame.draw.circle(surface, WHITE, (x, y), 50)
    pygame.draw.circle(surface, BLACK, (x, y), 50, 2)

    # Eyes glow
    pygame.draw.ellipse(surface, BLUE, (x - 26, y - 12, 20, 10))
    pygame.draw.ellipse(surface, BLUE, (x + 6, y - 12, 20, 10))

    pygame.draw.ellipse(surface, BLACK, (x - 26, y - 12, 20, 10), 2)
    pygame.draw.ellipse(surface, BLACK, (x + 6, y - 12, 20, 10), 2)

    # Eyebrows
    pygame.draw.line(surface, BLACK, (x - 35, y - 22), (x - 5, y - 26), 3)
    pygame.draw.line(surface, BLACK, (x + 5, y - 26), (x + 35, y - 22), 3)

    # Mouth
    pygame.draw.arc(surface, BLACK, (x - 18, y + 10, 36, 20), math.pi, 2 * math.pi, 2)


def draw_body(surface, x, y):
    pygame.draw.rect(surface, GRAY, (x - 35, y + 50, 70, 110))
    pygame.draw.line(surface, BLACK, (x - 35, y + 80), (x - 90, y + 140), 6)
    pygame.draw.line(surface, BLACK, (x + 35, y + 80), (x + 90, y + 140), 6)


def draw_energy_wave(surface, frame):
    if frame % 200 < 80:
        length = (frame % 80) * 6
        for i in range(5):
            pygame.draw.circle(
                surface,
                BLUE,
                (cx + length, cy + 30),
                20 + i * 6,
                2
            )


frame = 0
running = True
while running:
    clock.tick(60)
    frame += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Aura layer
    draw_aura(screen, cx, cy, frame)

    # Character
    draw_hair(screen, cx, cy, frame)
    draw_face(screen, cx, cy)
    draw_body(screen, cx, cy)

    # Energy attack
    draw_energy_wave(screen, frame)

    pygame.display.flip()

pygame.quit()
sys.exit()
