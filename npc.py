import sys

import pygame
from button import Button

class NPC:
    def __init__(self, text):
        self.pos = (640, 360)
        self.text = text
        self.sprites = pygame.sprite.Group()
        self.x = 125 #X coordinate of text
        self.y = 100 #Y coordinate of text

    def create_buttons(self,button1,button2 ):
        self.sprites.add(Button(pygame.Color('dodgerblue'),
                                pygame.Color('cyan'),
                                pygame.Rect(150, 595, 190, 99),
                                button1,
                                'YES'
                                ))

        self.sprites.add(Button(pygame.Color('dodgerblue'),
                                pygame.Color('cyan'),
                                pygame.Rect(950, 595, 190, 99),
                                button2,
                                'NO'))
        return self.sprites

    def create_npc(self, pos=(1100, 150)):
        self.npc_img = pygame.image.load("../npc.png")
        rect = self.npc_img.get_rect(center=pos)
        return [self.npc_img, rect]

    def create_dialog(self):

        self.dialog_img = pygame.image.load("../background.png")
        self.dialog_img = pygame.transform.scale(self.dialog_img, (1530, 1150))
        rect = self.dialog_img.get_rect(center=self.pos)
        return [self.dialog_img, rect]

    def create_text(self,screen):
        font = pygame.font.SysFont('comicsans', 30)
        for line in self.text.splitlines(): # Handling multiline text
            text_surf = font.render(line, 1, pygame.Color('black'))
            self.y+=font.get_height() + 5 #increasing y coordinate for multline texts
            screen.blit(text_surf,(self.x,self.y))

    def blit(self, screen):
        imgNPC, rectNPC = self.create_npc()
        imgDialog, rectDialog = self.create_dialog()
        screen.blit(imgDialog, rectDialog)
        screen.blit(imgNPC, rectNPC)
        self.create_text(screen)
        self.y = 100 #resetting y to 0
