import pygame


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

letters = [
    ['Q', 'W', 'E', 'R', 'T', 'Z', 'U', 'I', 'O'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K'],
    ['P', 'Y', 'X', 'C', 'V', 'B', 'N', 'M', 'L']
]


pygame.init()

W = 800
H = 800
 
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Words")

# background = pygame.image.load("images/background.jpg").convert()
button = pygame.image.load("../images/chair.png").convert()
button.set_colorkey(WHITE)
button2 = pygame.image.load("../images/chair.png").convert() 
pygame.draw.rect(button2, RED, button2.get_rect(), 5)

class SpriteCard(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../images/chair.png").convert()
        self.image.set_colorkey(WHITE)
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect(topleft=(x, y))

n = 2
m = 2
field = []
for i in range(n):
    for j in range(m):
        field.append(SpriteCard(i*400, j*400))



FPS = 30
clock = pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in field if s.rect.collidepoint(pos)]
            for s in clicked_sprites:
                s.image = button2
            
 
    sc.fill(WHITE)
    # sc.blit(background, (0, 0))
    # sc.blit(button, (50, 600))
    # sc.blit(button, (100, 600))
    # for i, row in enumerate(letters):
    #     for j, letter in enumerate(row):
            # sc.blit(lamp, (50+j*78.25 + (i%2)*78.25/2, 368+i*40))
            # sc.blit(button, (50+j*78.25 + (i%2)*78.25/2, 558+i*68))
    # sc.blit(button6, (200, 200))
    # sc.blit(button8, (200, 300))
    for item in field:
        sc.blit(item.image, item.rect)
    # sc.blit(button, (0, 0))
    # sc.blit(button, (400, 0))
    # sc.blit(button, (0, 400))
    # sc.blit(button, (400, 400))


    pygame.display.update()
    clock.tick(FPS)