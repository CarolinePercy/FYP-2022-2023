import pygame

from .. import globals

class InputBox():
    
    def __init__(self):
        centre = (globals.SCREEN_WIDTH / 2) - (self.inputRect.width / 2)
        self.inputRect.center = (centre, 200)

    def processEvents(self, t_event):

        entered = False

        if t_event.type == pygame.MOUSEBUTTONDOWN:

            if self.inputRect.collidepoint(t_event.pos):
                self.active = True
                self.color = self.color_active

            else:
                self.active = False
                self.color = self.color_passive

        if t_event.type == pygame.KEYDOWN and self.active:
  
            if t_event.key == pygame.K_BACKSPACE:
  
                self.user_text = self.user_text[:-1]

            elif t_event.key == pygame.K_RETURN:
                entered = True

            else:
                self.user_text += t_event.unicode
                print(t_event.unicode)

        return entered


    def Draw(self, t_screen):
        pygame.draw.rect(t_screen, self.color, self.inputRect)
  
        text_surface = self.font.render(self.user_text, True, (255, 255, 255))

        t_screen.blit(text_surface, (self.inputRect.x+5, self.inputRect.y+5))
      
        self.inputRect.w = max(100, text_surface.get_width()+10)

    def ReturnInput(self):
        value = self.user_text
        self.user_text = ""
        return value

    inputRect = pygame.Rect(0, 0, 300, 32)
    color_active = pygame.Color('lightskyblue3')
    color_passive = pygame.Color('chartreuse4')
    color = color_passive
    active = False
    font = pygame.font.Font(None, 32)
    user_text = ''