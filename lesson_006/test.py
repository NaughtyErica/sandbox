import pygame



pygame.init()

running = True
clock = pygame.time.Clock()
screen_size = (100, 100)
screen = pygame.display.set_mode(screen_size)
my_color = [250, 250, 100]

while running:
    # здесь смотрим,какие события произошли
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # нажатие на крестик: выход
            running = False
        if event.type == pygame.KEYDOWN:  # тип события - нажатие на кнопку
            if event.key == pygame.K_w:  # нажатие на w
                print("w")
            if event.key == pygame.K_s:  # нажатие на s
                print("s")

    screen.fill(my_color)
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
