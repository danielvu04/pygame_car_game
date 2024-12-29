import pygame, sys, time
from pygame.locals import *
from settings import *
from sprites import Player, Enemy

# Initializing
pygame.init()

# Setting up FPS
FramePerSec = pygame.time.Clock()

# Creating game display
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Game")

# Loading assets
background = pygame.image.load("assets/AnimatedStreet.png")
game_over = font.render("Game Over", True, BLACK)

# Setting up Sprites
P1 = Player()
E1 = Enemy()

# Creating sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# Adding custom event for increasing speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    # Moves and redraws all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Collision detection
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('assets/crash.wav').play()
        time.sleep(1)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
