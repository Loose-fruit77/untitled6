import pygame

pygame.init()
screen = pygame.display.set_mode((400,300))
done = False
x = 30
y = 30
is_blue = True

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 1
    if pressed[pygame.K_DOWN]: y += 1
    if pressed[pygame.K_LEFT]: x -= 1
    if pressed[pygame.K_RIGHT]: x += 1


    screen.fill((0, 0, 0))

    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)

    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

    pygame.draw.polygon(screen, (255, 128, 0), [(100, 45), (200, 130), (115, 115)])


    pygame.display.flip()
