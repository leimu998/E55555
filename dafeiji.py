import random

import pygame

SCREEN_RECT=pygame.Rect(0,0,660,909)

FRAME_PER_SEC=60

CREATE_ENEMY_EVENT=pygame.USEREVENT

HERO_FIRE_EVENT=pygame.USEREVENT+1

class GameSprite (pygame.sprite.Sprite):

    def __init__(self,image_name,speed=1,speed1=1):

        super().__init__()

        self.image = pygame.image.load(image_name)

        self.rect = self.image.get_rect()

        self.speed = speed

        self.speed1 = speed1

    def update(self):

        self.rect.y += self.speed

class Background(GameSprite):

    def __init__(self,is_alt=False):

        super().__init__("./ditu.jpg")

 

        if is_alt:

            self.rect.y=-self.rect.height

 

    def update(self):

        super().update()

 

        if self.rect.y>=SCREEN_RECT.height:

            self.rect.y=-self.rect.height

 

class Enemy(GameSprite):

    def __init__(self):

        if random.random()<0.21:          

            super().__init__("./bd2.png")

        elif random.random()>0.81:

            super().__init__("./bd4.png")

        elif random.random()>0.21 and random.random()<0.4 :

            super().__init__("./bd5.png")

            

        else:

            super().__init__("./bd6.png")

            

        self.speed=random.randint(1,2)

        self.rect.bottom=0

        max_x=SCREEN_RECT.width-self.rect.width

        self.rect.x=random.randint(0,max_x)

        pass

    def update(self):

        super().update()

        if self.rect.y>=SCREEN_RECT.height:

            self.kill()

    def __del__(self):

        pass

class Hero(GameSprite):

 

    def __init__(self):

        super().__init__("./ys1.png",0)

        self.rect.centerx=SCREEN_RECT.centerx

        self.rect.bottom=SCREEN_RECT.bottom-50

        self.bullets=pygame.sprite.Group()

        

    def update(self):

        self.rect.x += self.speed

        self.rect.y += self.speed1

        if self.rect.x<0:

            self.rect.x=0

        elif self.rect.right>SCREEN_RECT.right:

            self.rect.right=SCREEN_RECT.right

        elif self.rect.y>800:

            self.rect.y=800

        elif self.rect.y<SCREEN_RECT.top:

            self.rect.y=SCREEN_RECT.top

    def fire(self):        

        keys_pressed=pygame.key.get_pressed()

        if keys_pressed[pygame.K_SPACE]:

            sound3=pygame.mixer.Sound("./hu1.wav")

            sound3.play()

            for i in range(1):

                bullet=BUllet()

                bullet.rect.bottom=self.rect.y

                bullet.rect.centerx=self.rect.centerx+i*42

                self.bullets.add(bullet)

class BUllet(GameSprite):

    def __init__(self):

        super().__init__("./2.png",-4)

    def update(self):

        super().update()

        if self.rect.bottom<0:

            self.kill()

    def __del__(self):

        pass
