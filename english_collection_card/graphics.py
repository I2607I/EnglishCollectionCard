import pygame
import random
from sprite import SpriteCard, Button

letters = [
    ['Q', 'W', 'E', 'R', 'T', 'Z', 'U', 'I', 'O'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K'],
    ['P', 'Y', 'X', 'C', 'V', 'B', 'N', 'M', 'L']
]
WHITE = (255, 255, 255)
LIGHT_BROWN = (200, 100, 150)
BROWN = (255, 200, 120)

pygame.init()

W = 1600  
H = 800
 
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Words")


n = 4
m = 2
count_words = n*m//2
field = [0 for i in range(n*m)]
words = ['tree', 'chair', 'drum', 'car']*2
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

def test1():
    print('123')
def test2():
    print(321)



def main_cycle():
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
        for item in field:
            sc.blit(item.image, item.rect)


        pygame.display.update()
        clock.tick(FPS)


back = pygame.image.load(f"../images/background.jpg").convert()
back = pygame.transform.scale(back, (back.get_width()*1.3, back.get_height()*1.3))
buttons = []

w_button = 300
h_button = 80
y = 150
button_functions = [test1, test2, None]
for i, item in enumerate(button_functions):
    buttons.append(Button(sc, W//2-300//2, 200 + y*i, w_button, h_button, '2607', item))


def menu_cycle():
    FPS = 30
    clock = pygame.time.Clock()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [b for b in buttons if b.buttonRect.collidepoint(pos)]
                for b in clicked_sprites:
                    b.onclickFunction()

        sc.fill(WHITE)
        sc.blit(back, sc.get_rect())
        for button in buttons:
            sc.blit(button.buttonSurface, button.buttonRect)
        pygame.display.update()
        clock.tick(FPS)



# main_cycle()
menu_cycle()
