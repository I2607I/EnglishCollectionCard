import pygame

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 46)


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
            pygame.draw.rect(self.image_opened_clicked, RED, self.image_opened_clicked.get_rect(), 5)
            self.image_opened_won = pygame.image.load(f"../images/white.png").convert()
            pygame.draw.rect(self.image_opened_won, GREEN, self.image_opened_won.get_rect(), 5)
            a = pygame.font.Font.render(my_font, name, 1, (100, 100, 100))
            self.image_opened.blit(a, self.image_opened.get_rect().center)
            self.image_opened_clicked.blit(a, self.image_opened_clicked.get_rect().center)
            self.image_opened_won.blit(a, self.image_opened_won.get_rect().center)

        else:
            self.image_opened = pygame.image.load(f"../images/{name}.png").convert()
            self.image_opened_clicked = pygame.image.load(f"../images/{name}.png").convert()
            pygame.draw.rect(self.image_opened_clicked, RED, self.image_opened_clicked.get_rect(), 5)
            self.image_opened_won = pygame.image.load(f"../images/{name}.png").convert()
            pygame.draw.rect(self.image_opened_won, GREEN, self.image_opened_won.get_rect(), 5)
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

class Button():
    def __init__(self, screen, x, y, width, height, buttonText, onclickFunction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        if onclickFunction is None:
            self.onclickFunction = self.NoneFunction
        self.alreadyPressed = False
        self.screen = screen
        self.buttonText = buttonText

        self.fillColors = {
            'normal': '#987654',
            'hover': '#654321',
            'pressed': '#422d15',
            'border': '#000000'
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.buttonSurface, self.fillColors['normal'], self.buttonSurface.get_rect())
        pygame.draw.rect(self.buttonSurface, self.fillColors['border'], self.buttonSurface.get_rect(), 8)
        buttonSurf = pygame.font.Font.render(my_font, self.buttonText, True, (20, 20, 20))
        self.buttonSurface.blit(buttonSurf, [
            self.buttonRect.width/2 - buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - buttonSurf.get_rect().height/2
        ])
    def NoneFunction(self):
        pass


