import pygame
import random


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

letters = [
    ['Q', 'W', 'E', 'R', 'T', 'Z', 'U', 'I', 'O'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K'],
    ['P', 'Y', 'X', 'C', 'V', 'B', 'N', 'M', 'L']
]


pygame.init()

W = 1600  
H = 800
 
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Words")

# background = pygame.image.load("images/background.jpg").convert()
button = pygame.image.load("../images/chair.png").convert()
button.set_colorkey(WHITE)
button2 = pygame.image.load("../images/chair.png").convert() 
pygame.draw.rect(button2, RED, button2.get_rect(), 5)
button3 = pygame.image.load("../images/chair.png").convert() 
pygame.draw.rect(button3, GREEN, button2.get_rect(), 5)

pygame.font.init()
text = '2607'
my_font = pygame.font.SysFont('Arial', 46)
a = pygame.font.Font.render(my_font, text, 1, (0, 0, 0))


class SpriteCard(pygame.sprite.Sprite):
    def __init__(self, x, y, name, is_text):
        pygame.sprite.Sprite.__init__(self)
        self.opened = False
        self.clicked = False
        self.won = False
        self.image_closed = pygame.image.load(f"../images/back.png").convert()
        if is_text:
            self.image_opened = pygame.image.load(f"../images/white.png").convert()
            self.image_opened_clicked = pygame.image.load(f"../images/white.png").convert()
            pygame.draw.rect(self.image_opened_clicked, RED, button2.get_rect(), 5)
            self.image_opened_won = pygame.image.load(f"../images/white.png").convert()
            pygame.draw.rect(self.image_opened_won, GREEN, button2.get_rect(), 5)
            a = pygame.font.Font.render(my_font, name, 1, (100, 100, 100))
            self.image_opened.blit(a, self.image_opened.get_rect().center)
            self.image_opened_clicked.blit(a, self.image_opened_clicked.get_rect().center)
            self.image_opened_won.blit(a, self.image_opened_won.get_rect().center)

        else:
            self.image_opened = pygame.image.load(f"../images/{name}.png").convert()
            self.image_opened_clicked = pygame.image.load(f"../images/{name}.png").convert()
            pygame.draw.rect(self.image_opened_clicked, RED, button2.get_rect(), 5)
            self.image_opened_won = pygame.image.load(f"../images/{name}.png").convert()
            pygame.draw.rect(self.image_opened_won, GREEN, button2.get_rect(), 5)
        self.image = self.image_closed
        # self.image.set_colorkey(WHITE)
        # self.image.blit(a, self.image.get_rect().center)
        # self.image.fill(GREEN)
        self.name = name
        self.rect = self.image.get_rect(topleft=(x, y))
    def turn(self):
        if not self.opened:
            self.image = self.image_opened
        else:
            self.image = self.image_closed
        self.opened = not self.opened
    def update(self):
        if self.opened:
            if self.clicked:
                self.image = self.image_opened_clicked
            else:
                self.image = self.image_opened
            if self.won:
                self.image = self.image_opened_won
        else:
            self.image = self.image_closed


n = 4
m = 2
count_words = n*m//2
field = [0 for i in range(n*m)]
words = ['tree', 'chair', 'drum', 'car']
words = ['tree', 'chair', 'tree', 'chair']*2
for i in range(count_words):
    pass
perm = random.sample(range(m*n), m*n)
use_word = set()
for word, ind in zip(words, perm):
    is_word = True if word in use_word else False
    j = ind%m
    i = (ind-j)//m
    field[ind] = SpriteCard(i*400, j*400, word, is_word)





# for i in range(n):
#     for j in range(m):
#         if i == 0 and j == 0:
#             field[i*m+j] = SpriteCard(i*400, j*400, 'tree', False)
#         elif i == 3 and j == 1:
#             field[i*m+j] = SpriteCard(i*400, j*400, 'tree', False)
#         else:
#             field[i*m+j] = SpriteCard(i*400, j*400, 'chair', True)



FPS = 30
clock = pygame.time.Clock()
prev_clicked = None
already_opened = []
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            clicked_sprites = [s for s in field if s.rect.collidepoint(pos)]
            for s in clicked_sprites:
                if s not in already_opened:
                    # s.turn()
                    if prev_clicked and prev_clicked != s and prev_clicked.name == s.name:
                        prev_clicked.won = True
                        s.won = True
                        already_opened.append(prev_clicked)
                        already_opened.append(s)
                        prev_clicked.update()
                        s.turn()
                        s.update()

                        prev_clicked = None
                    else:
                        s.clicked = True
                        s.turn()
                        # s.click()
                        if prev_clicked:
                            prev_clicked.clicked = False
                            prev_clicked.turn()
                            s.clicked = False
                            s.turn()
                            prev_clicked.update()
                            prev_clicked = None
                        else:
                            prev_clicked = s
                        s.update()
            
 
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