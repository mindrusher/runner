import pygame
import random
import time
import sys
import os

from pygame.locals import (
    RLEACCEL,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_UP
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

FPS = 20

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

chosen_hero = 0

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
timing = time.time()

running = True

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Player(pygame.sprite.Sprite):
      
    def __init__(self):
        super(Player, self).__init__()
        self.images = [
            [
                pygame.image.load(resource_path('image/froggy_boy/r1.png')), pygame.image.load(resource_path('image/froggy_boy/r2.png')),
                pygame.image.load(resource_path('image/froggy_boy/r3.png')), pygame.image.load(resource_path('image/froggy_boy/r4.png')),
                pygame.image.load(resource_path('image/froggy_boy/r5.png')), pygame.image.load(resource_path('image/froggy_boy/r6.png')),
                pygame.image.load(resource_path('image/froggy_boy/r7.png')), pygame.image.load(resource_path('image/froggy_boy/r8.png')),
                pygame.image.load(resource_path('image/froggy_boy/r9.png')), pygame.image.load(resource_path('image/froggy_boy/r10.png')),
                pygame.image.load(resource_path('image/froggy_boy/r11.png'))
            ],
            [
                pygame.image.load(resource_path('image/Naruto_style/r1.png')), pygame.image.load(resource_path('image/Naruto_style/r2.png')),
                pygame.image.load(resource_path('image/Naruto_style/r3.png')), pygame.image.load(resource_path('image/Naruto_style/r4.png')),
                pygame.image.load(resource_path('image/Naruto_style/r5.png')), pygame.image.load(resource_path('image/Naruto_style/r6.png')),
                pygame.image.load(resource_path('image/Naruto_style/r7.png')), pygame.image.load(resource_path('image/Naruto_style/r8.png')),
                pygame.image.load(resource_path('image/Naruto_style/r9.png')), pygame.image.load(resource_path('image/Naruto_style/r10.png')),
            ],
            [
                pygame.image.load(resource_path('image/red_nek/r1.png')), pygame.image.load(resource_path('image/red_nek/r2.png')),
                pygame.image.load(resource_path('image/red_nek/r3.png')), pygame.image.load(resource_path('image/red_nek/r4.png')),
                pygame.image.load(resource_path('image/red_nek/r5.png')), pygame.image.load(resource_path('image/red_nek/r6.png')),
                pygame.image.load(resource_path('image/red_nek/r7.png')), pygame.image.load(resource_path('image/red_nek/r8.png')),
            ]
        ]
        self.index = 0
        self.rect = pygame.Rect(10, 475, 35, 35)
        self.image = self.images[self.index]
        self.rush = False
        self.rush_time = 8
        self.jump = False
        self.jump_time = 8

    def update(self, pressed_keys):
        global chosen_hero
        
        if chosen_hero == 1:
            self.index += 1       
            if self.index >= len(self.images[0]):
                self.index = 0
            self.image = self.images[0][self.index]

        if chosen_hero == 2:
            self.index += 1       
            if self.index >= len(self.images[1]):
                self.index = 0
            self.image = self.images[1][self.index]
        
        if chosen_hero == 3:
            self.index += 1        
            if self.index >= len(self.images[2]):
                self.index = 0
            self.image = self.images[2][self.index]

        if pressed_keys[K_SPACE] or pressed_keys[K_UP]:
            self.jump = True
        if self.jump is True:
            if self.jump_time >= -8:
                if self.jump_time < 0:
                    self.rect.move_ip(0, (self.jump_time ** 2)/2)
                else:
                    self.rect.move_ip(0, (-self.jump_time ** 2)/2)
                self.jump_time -= 1
            else:
                self.jump = False
                self.jump_time = 8            
            
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x_pos):
        super(Enemy, self).__init__()
        self.images = [
            pygame.image.load(resource_path('image/monster_mushroom/m1.png')), pygame.image.load(resource_path('image/monster_mushroom/m2.png')),
            pygame.image.load(resource_path('image/monster_mushroom/m3.png')), pygame.image.load(resource_path('image/monster_mushroom/m4.png')),
            pygame.image.load(resource_path('image/monster_mushroom/m5.png')), pygame.image.load(resource_path('image/monster_mushroom/m6.png')),
            pygame.image.load(resource_path('image/monster_mushroom/m7.png')), pygame.image.load(resource_path('image/monster_mushroom/m8.png')),
            pygame.image.load(resource_path('image/monster_mushroom/m9.png')), pygame.image.load(resource_path('image/monster_mushroom/m9.png'))
        ]
        self.x_pos = x_pos
        self.index = 0
        self.rect = pygame.Rect(self.x_pos, 480, 50, 50)
        self.image = self.images[self.index]
        self.speed = 10
        
    def update(self):
        global chosen_hero
        self.rect.move_ip(-self.speed, 0)
        
        if chosen_hero == 1:
            self.index += 1       
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]

surf_f = pygame.image.load(resource_path('image/red_nek/forest.png')).convert()
rect_f = surf_f.get_rect(center=(400, 300))
surf_f2 = pygame.image.load(resource_path('image/red_nek/forest.png')).convert()
rect_f2 = surf_f.get_rect(center=(1200, 300))

def Back_img():
    rect_f.move_ip(-5, 0)
    screen.blit(surf_f, rect_f)
    if rect_f.left <= 0 or rect_f.right >= 800:
        rect_f2.move_ip(-5, 0)
        screen.blit(surf_f2, rect_f2)       
    if rect_f2.right == 0:
        rect_f2.left = SCREEN_WIDTH
    if rect_f.right == 0:
        rect_f.left = SCREEN_WIDTH

surf1 = pygame.image.load(resource_path('image/red_nek/hero1.png'))
rect1 = surf1.get_rect(center=(162.5, 350))

surf2 = pygame.image.load(resource_path('image/red_nek/hero2.png'))
rect2 = surf2.get_rect(center=(400, 350))

surf3 = pygame.image.load(resource_path('image/red_nek/hero3.png'))
rect3 = surf3.get_rect(center=(637.5, 350))

f = pygame.font.Font(resource_path('image/red_nek/Pixel-Font.ttf'), 50)
text = f.render('Выбери своего героя', 1, (0, 0, 255))

def Menu():
    global chosen_hero
    global clock
    global FPS
    global running
    global surf1
    global surf2
    global surf3
    global rect1
    global rect2
    global rect3

    while chosen_hero == 0:

        screen.fill((38, 173, 222))

        screen.blit(text, (150, 140))

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
            elif event.type == QUIT:
                pygame.quit()
        
        screen.blit(surf1, rect1)
        screen.blit(surf2, rect2)
        screen.blit(surf3, rect3)

        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1] 

        if pygame.mouse.get_pressed()[0] and 87.5 <= mouse_x <= 237.5 and 250 <= mouse_y <= 450:
            chosen_hero = 1
            break

        if pygame.mouse.get_pressed()[0] and 325 <= mouse_x <= 475 and 250 <= mouse_y <= 450:
            chosen_hero = 2
            #FPS = 15
            break

        if pygame.mouse.get_pressed()[0] and 562.5 <= mouse_x <= 712.5 and 250 <= mouse_y <= 450:
            chosen_hero = 3
            #FPS = 15
            break

        pygame.display.flip()

        clock.tick(FPS)

def Game():
    global chosen_hero
    global clock
    global FPS
    global running

    frame_count = 0

    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 3000)
    ADDENEMY2 = pygame.USEREVENT + 2
    pygame.time.set_timer(ADDENEMY2, 5000)
    ADDENEMY2 = pygame.USEREVENT + 3
    pygame.time.set_timer(ADDENEMY2, 5000)
    
    while chosen_hero > 0:
        total_seconds = frame_count // FPS
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
            elif event.type == QUIT:
                pygame.quit()

            elif event.type == ADDENEMY:
                if 0 < seconds < 10 and minutes == 0:
                    enemy = Enemy(840)
                    enemies.add(enemy)
                if 10 < seconds < 20 and minutes == 0:
                    enemy = Enemy(840)
                    enemies.add(enemy)
                    enemy.speed = 12
                if 20 < seconds < 35 and minutes == 0:
                    enemy = Enemy(840)
                    enemies.add(enemy)
                    enemy.speed = 14
                if 35 < seconds < 50 and minutes == 0:
                    enemy = Enemy(840)
                    enemies.add(enemy)
                    enemy.speed = 16
                if 50 < seconds < 60 and minutes == 0:
                    enemy = Enemy(840)
                    enemies.add(enemy)
                    enemy.speed = 18
                if 0 < seconds < 20 and minutes == 1:
                    enemy = Enemy(840)
                    enemies.add(enemy)
                    enemy.speed = 20
                if 20 < seconds < 40 and minutes == 1:
                    enemy = Enemy(840)
                    enemies.add(enemy)
                    enemy.speed = 20
                if 40 < seconds < 60 and minutes == 1:
                    enemy = Enemy(840)
                    enemies.add(enemy)
                    enemy.speed = 24

            elif event.type == ADDENEMY2:
                if 0 < seconds < 30 and minutes == 0:
                    enemy = Enemy(840)
                    enemies.add(enemy)
                    enemy = Enemy(880)
                    enemies.add(enemy)
                if 30 < seconds < 50 and minutes == 0:
                    enemy = Enemy(840)
                    enemy.speed = 12
                    enemies.add(enemy)
                    enemy = Enemy(880)
                    enemy.speed = 12
                    enemies.add(enemy)
                if 0 < seconds < 20 and minutes == 1:
                    enemy = Enemy(840)
                    enemy.speed = 15
                    enemies.add(enemy)
                    enemy = Enemy(880)
                    enemy.speed = 15
                    enemies.add(enemy)
                if 20 < seconds < 40 and minutes == 1:
                    enemy = Enemy(840)
                    enemy.speed = 20
                    enemies.add(enemy)
                    enemy = Enemy(880)
                    enemy.speed = 20
                    enemies.add(enemy)
                if 40 < seconds < 60 and minutes == 1:
                    enemy = Enemy(840)
                    enemy.speed = 22
                    enemies.add(enemy)
                    enemy = Enemy(880)
                    enemy.speed = 22
                    enemies.add(enemy)
                
        Back_img()
        enemies.update()
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        
        text = f.render(output_string, True, BLACK)
        screen.blit(text, [250, 250])

        if 1 <= chosen_hero <= 3:
            enemies.draw(screen)
            hero.draw(screen)
            
    
        for i in enemies:
            if player.rect.colliderect(i):
                print('loh')
                #enemies.empty()
                #chosen_hero = 0
                #time.sleep(1)
                #break

        frame_count += 1
    
        pygame.display.flip()

        clock.tick(FPS)

player = Player()
hero = pygame.sprite.Group(player)

enemies = pygame.sprite.Group()

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    if chosen_hero == 0:
        Menu()
    elif chosen_hero > 0:
        Game()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()