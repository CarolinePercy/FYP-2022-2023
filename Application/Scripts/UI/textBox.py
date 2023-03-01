import pygame

from .. import globals

class InputBox():
    
    def __init__(self):
        centre = (globals.SCREEN_WIDTH / 2, (globals.SCREEN_HEIGHT / 2))
        self.inputRect.center = centre

    def processEvents(self, t_event):

        entered = False

        if t_event.type == pygame.MOUSEBUTTONDOWN:

            if self.inputRect.collidepoint(t_event.pos):
                self.active = True
                self.colour = self.colour_active

            else:
                self.active = False
                self.colour = self.colour_passive

        if t_event.type == pygame.KEYDOWN and self.active:
  
            if t_event.key == pygame.K_BACKSPACE:
  
                self.user_text = self.user_text[:-1]

            elif t_event.key == pygame.K_RETURN:
                entered = True

            else:
                self.user_text += t_event.unicode

        return entered

    def Draw(self, t_screen):

        pygame.draw.rect(t_screen, self.colour, self.inputRect)
  
        text_surface = self.font.render(self.user_text, True, self.textColour)

        t_screen.blit(text_surface, (self.inputRect.x+5, self.inputRect.y+5))
      
        self.inputRect.w = max(self.inputWidth, text_surface.get_width()+10)

    def ReturnInput(self):
        value = self.user_text
        self.user_text = ""
        return value


    inputWidth = 700
    inputRect = pygame.Rect(0, 0, inputWidth, 32)
    active = False
    font = pygame.font.Font(None, 32)
    user_text = ''

    colour_active = pygame.Color('grey90')
    colour_passive = pygame.Color('white')
    colour = colour_passive
    textColour = pygame.Color('gray21')