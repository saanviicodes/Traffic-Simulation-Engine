import pygame
pygame.init()
screen=pygame.display.set_mode((800, 600))
pygame.display.set_caption("Traffic Simulator")
clock = pygame.time.Clock()
running=True
car_x=150
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((0, 0, 0)) 
    pygame.draw.rect(screen, (50, 50, 50), (100, 200, 600, 150))
    pygame.draw.rect(screen, (255, 105, 180), (car_x, 245, 50, 25))
    pygame.display.flip()
    car_x+=2
    if car_x > 800:
        car_x = -50
    clock.tick(60) 
pygame.quit()