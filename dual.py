import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Dual")


class Sprite(pygame.sprite.Sprite):

    __speed = 10
    __x_dir = __speed
    __y_dir = 0

    def __init__(self, pos, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])
        pygame.draw.circle(self.image, color, (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def move(self):
        self.rect.move_ip(self.__x_dir, self.__y_dir)

    def changeDir(self, x, y):
        self.__x_dir = x
        self.__y_dir = y

    def changeXDir(self, x):
        self.__x_dir = x

    def changeYDir(self, y):
        self.__y_dir = y

    def getDirection(self):
        return (self.__x_dir, self.__y_dir)
    def bounce(self, touch):
        print("das")
        change = math.floor(self.__speed/5)
        rand = random.randint(-change,change)
        if touch == 'right':
            self.changeXDir(-self.__speed)
            self.changeYDir(self.__y_dir+rand)
        elif touch == 'left':
            self.changeXDir(self.__speed)
            self.changeYDir(self.__y_dir+rand)
        elif touch == 'up':
            self.changeYDir(self.__speed)
            self.changeXDir(self.__x_dir+rand)
        elif touch == 'down':
            self.changeYDir(-self.__speed)
            self.changeXDir(self.__x_dir+rand)

    def changeSpeed(self, speed):
        self.__speed = speed

class Bat(pygame.sprite.Sprite):
    def __init__(self,pos,color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,80])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = pos



player_grp = pygame.sprite.Group()
player = Sprite([20, 20], (0, 255, 0))
player_grp.add(player)

bat_grp = pygame.sprite.Group()
batL = Bat([15,100],(0,0,255))
batR = Bat([screen.get_width()-15,100],(0,0,255))
bat_grp.add(batL)
bat_grp.add(batR)

def isTouchingWall(player, screen):
    height = screen.get_height()
    width = screen.get_width()
    if(0 < player.rect.x and player.rect.x < width and 0 < player.rect.y and player.rect.y < height):
        return False
    else:
        if player.rect.x <= 0:
            return 'left'
        elif player.rect.x >= width:
            return 'right'
        elif player.rect.y <= 0:
            return 'up'
        else:
            return 'down'

def isTouchingBat():
    if(pygame.sprite.spritecollide(batL,player_grp,True)):
        return 'left'
    elif pygame.sprite.spritecollide(batR,player_grp,True):
        return 'right'
    else:
        return False



def checkKey():
    key = pygame.key.get_pressed()
    if(key[pygame.K_DOWN] and batR.rect.centery < screen.get_height()):
        batR.rect.move_ip(0, 10)
    if(key[pygame.K_UP] and batR.rect.centery > 0):
        batR.rect.move_ip(0, -10)


def main():
    checkKey()
    touch = isTouchingWall(player, screen)
    touchBat = isTouchingBat()
    if touch:
        player.bounce(touch)
    if touchBat:
        player.bounce(touchBat)
    player.move()


def update():
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill([0, 0, 0])
    main()
    pygame.time.wait(30)
    bat_grp.draw(screen)
    player_grp.draw(screen)
    pygame.display.update()


while True:
    update()
