import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()
screen.fill((255, 255, 255))
radius = 100
temp_radius = radius
        
def charge_animations(x, y, radius, screen):
        while radius > 0:
                pygame.draw.circle(screen, color, (x, y+radius), 2, 2)
                pygame.draw.circle(screen, color, (x, y-radius), 2, 2)
                pygame.draw.circle(screen, color, (x+radius, y), 2, 2)
                pygame.draw.circle(screen, color, (x-radius, y), 2, 2)
                pygame.draw.circle(screen, color, (x+radius, y+radius), 2, 2)
                pygame.draw.circle(screen, color, (x-radius, y-radius), 2, 2)
                pygame.draw.circle(screen, color, (x-radius, y+radius), 2, 2)
                pygame.draw.circle(screen, color, (x+radius, y-radius), 2, 2)
                radius -= 1
                screen.fill((255, 255, 255))
                
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3

        screen.fill((255, 255, 255))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        if temp_radius < 0:
                temp_radius = radius
        pygame.draw.circle(screen, color, (x, y), 10, 10)
        pygame.draw.circle(screen, color, (x, y+temp_radius), 2, 2)
        pygame.draw.circle(screen, color, (x, y-temp_radius), 2, 2)
        pygame.draw.circle(screen, color, (x+temp_radius, y), 2, 2)
        pygame.draw.circle(screen, color, (x-temp_radius, y), 2, 2)
        pygame.draw.circle(screen, color, (x+temp_radius, y+temp_radius), 2, 2)
        pygame.draw.circle(screen, color, (x-temp_radius, y-temp_radius), 2, 2)
        pygame.draw.circle(screen, color, (x-temp_radius, y+temp_radius), 2, 2)
        pygame.draw.circle(screen, color, (x+temp_radius, y-temp_radius), 2, 2)

        temp_radius -= 1
        #charge_animations(x, y, 100, screen)
        '''
        while radius > 0:
                pygame.draw.circle(screen, color, (x, y+radius), 2, 2)
                pygame.draw.circle(screen, color, (x, y-radius), 2, 2)
                pygame.draw.circle(screen, color, (x+radius, y), 2, 2)
                pygame.draw.circle(screen, color, (x-radius, y), 2, 2)
                pygame.draw.circle(screen, color, (x+radius, y+radius), 2, 2)
                pygame.draw.circle(screen, color, (x-radius, y-radius), 2, 2)
                pygame.draw.circle(screen, color, (x-radius, y+radius), 2, 2)
                pygame.draw.circle(screen, color, (x+radius, y-radius), 2, 2)
                radius -= 1
                screen.fill((255, 255, 255))
                #pygame.draw.circle(screen, color, (x, y), 10, 10)
        '''
        
        pygame.display.flip()
        clock.tick(60)
