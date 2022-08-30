import sys

import pygame
from pygame import mixer
pygame.init()

font = pygame.font.SysFont('comicsans', 30)


class Button(pygame.sprite.Sprite):
    def __init__(self, color, hover_color, rect, callback, text=""):
        super().__init__()
        self.text = text
        tmp_rect = pygame.Rect(0, 0, *rect.size)
        self.nav_mus = mixer.Sound(r"../audio/navigation.wav")
        self.org = self.create_button(color, text, tmp_rect) #original button
        self.hov = self.create_button(hover_color, text, tmp_rect) #blit new button (with change color) on hover
        self.image = self.org
        self.rect = rect
        self.played = False
        self.callback = callback

    #create buttons
    def create_button(self, color, text, rect):
        btn = pygame.Surface(rect.size)
        btn.fill(color)
        if text:
            text_surf = font.render(text, 1, pygame.Color('black'))
            text_rect = text_surf.get_rect(center=rect.center)
            btn.blit(text_surf, text_rect)
        return btn

    def update(self, events):
        pos = pygame.mouse.get_pos()
        clicked = self.rect.collidepoint(pos) #check if user hovers on button
        if not clicked:
            self.played = False
        else:
            self.play_click_sound()
        self.image = self.hov if clicked else self.org

        for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and clicked:
                    self.callback(self)

    #play sound on hover
    def play_click_sound(self):
        if not self.played:
            self.nav_mus.play()
            self.played = True

