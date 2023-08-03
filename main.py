# Pygame    		             //
# Version 1.0	 		        ('>
# 011004 			            /rr
# ©2023 by KralicekGamer       *\))_

import pygame

pygame.init()
window_width = 800
window_height = 800
dark_green = (0, 100, 0)
lime_green = (52, 235, 70)
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('PyGame')

FPS = 30
clock = pygame.time.Clock()

pole = 40
pole_size = window_width // pole

postava_x, postava_y = 0, 0
postava_posunout = pole

postava_img = pygame.image.load("player.png")
postava_img = pygame.transform.scale(postava_img, (pole, pole))

font = pygame.font.SysFont(None, 25)


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10
        self.color = (128, 128, 128)
        self.radius = 5

    def move(self):
        self.x += self.speed

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)


running = True
bullets = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    horizontal_movement = 0
    vertical_movement = 0
    if keys[pygame.K_a]:
        horizontal_movement -= postava_posunout
    if keys[pygame.K_d]:
        horizontal_movement += postava_posunout
    if keys[pygame.K_w]:
        vertical_movement -= postava_posunout
    if keys[pygame.K_s]:
        vertical_movement += postava_posunout
    if keys[pygame.K_SPACE]:
        # Stisknutí klávesy mezerník vytvoří novou střelu
        bullet = Bullet(postava_x + pole // 2, postava_y + pole // 2)
        bullets.append(bullet)

    postava_x = max(0, min(postava_x + horizontal_movement, window_width - pole))
    postava_y = max(0, min(postava_y + vertical_movement, window_height - pole))

    for row in range(pole_size):
        for col in range(pole_size):
            x = col * pole
            y = row * pole
            if (row + col) % 2 == 0:
                pygame.draw.rect(window, lime_green, (x, y, pole, pole))
            else:
                pygame.draw.rect(window, dark_green, (x, y, pole, pole))

    window.blit(postava_img, (postava_x, postava_y))

    for bullet in bullets:
        bullet.move()
        bullet.draw(window)
        if bullet.x > window_width:
            bullets.remove(bullet)

    fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, (0, 0, 0))
    window.blit(fps_text, (window_width - 100, 10))

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
