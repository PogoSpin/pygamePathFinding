import pygame

class Square:
    def __init__(self, x, y, width, height, type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.value = None

        self.type = type

    def display(self, screen, font):
        if self.type == ' ':
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x, self.y, self.width, self.height))
        elif self.type == 'X':
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self.x, self.y, self.width, self.height))
        elif self.type == 'l':
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(self.x, self.y, self.width, self.height))
        elif self.type == 0:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, self.width, self.height))
        elif self.type == 'G':
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(self.x, self.y, self.width, self.height))
        elif self.type == 'lineFront':
            pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x, self.y, self.width, self.height))
            # text = font.render(str(self.type), True, (0, 0, 0))
            # textRect = text.get_rect(center=(self.x + self.width/2, self.y + self.height/2))
            # screen.blit(text, textRect)






