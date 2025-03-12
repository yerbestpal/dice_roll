import pygame
from pygame.locals import *
import random

pygame.init()
pygame.font.init()

font = pygame.font.SysFont('Courier New', 40)
window_size = (400, 400)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption('Dice Roll')
running = True

class Dice:
    def __init__(self):
        self.value = 1
        self.rect = pygame.Rect(0, 0, 400, 400)
        self.running = True

    def roll(self):
        self.value = random.randint(1, 6)
    
    def main(self):
        # game loop
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif (event.type == KEYDOWN and event.key == K_SPACE) or event.type == MOUSEBUTTONDOWN:
                    self.roll()

            window.fill((0, 0, 0))
            self.draw_face(self.value)
            pygame.display.flip()
        
        pygame.quit()
        
    def draw_face(self, number):
        try:
            match number:
                case 1:
                    img = pygame.image.load('images/1.png')
                case 2:
                    img = pygame.image.load('images/2.png')
                case 3:
                    img = pygame.image.load('images/3.png')
                case 4:
                    img = pygame.image.load('images/4.png')
                case 5:
                    img = pygame.image.load('images/5.png')
                case 6:
                    img = pygame.image.load('images/6.png')
                case _:
                    print('Invalid number')
                    return
            
            pygame.draw.rect(window, (255, 255, 255), self.rect)
            img = pygame.transform.scale(img, window_size)
            window.blit(img, (0, 0))
        except pygame.error as e:
            print(f"Error loading image: {e}")

if __name__ == '__main__':
    g = Dice()
    g.main()