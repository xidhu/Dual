import pygame
import random


pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Particles")

particle_count = 1000

class Sprite(pygame.sprite.Sprite):
    __x_dir = 10
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
        rand = random.randint(-2, 2)
        if touch == 'right':
            self.changeXDir(-10)
            self.changeYDir(self.__y_dir+rand)
        elif touch == 'left':
            self.changeXDir(10)
            self.changeYDir(self.__y_dir+rand)
        elif touch == 'up':
            self.changeYDir(10)
            self.changeXDir(self.__x_dir+rand)
        elif touch == 'down':
            self.changeYDir(-10)
            self.changeXDir(self.__x_dir+rand)


player_grp = pygame.sprite.Group()

for i in range(particle_count):
    player_grp.add(Sprite([20, 20], (0, 255, 0)))


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


def checkKey():
    key = pygame.key.get_pressed()
    if(key[pygame.K_DOWN]):
        player.rect.move_ip(0, 10)
    if(key[pygame.K_UP]):
        player.rect.move_ip(0, -10)
    if(key[pygame.K_RIGHT]):
        player.rect.move_ip(10, 0)
    if(key[pygame.K_LEFT]):
        player.rect.move_ip(-10, 0)


def main():
    #checkKey()
    for player in player_grp.sprites():
        touch = isTouchingWall(player, screen)
        if touch:
            player.bounce(touch)
        player.move()


def update():
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill([0, 0, 0])
    main()
    pygame.time.wait(30)
    player_grp.draw(screen)
    pygame.display.update()


while True:
    update()
