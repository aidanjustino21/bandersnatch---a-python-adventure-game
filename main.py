import pygame
import sys
from settings import *
from level import Level
from npc import NPC

class Game:
    def __init__(self):
        # sound
        main_sound = pygame.mixer.Sound('../audio/Undertale OST- 023 - Shop [TRAP REMIX] @Mai [Bass Boosted].mp3')
        main_sound.set_volume(0.5)
        main_sound.play(loops=-1)

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Bandersnatch')
        self.clock = pygame.time.Clock()
        self.npc_state = False #monitors npc state
        self.level = Level()
        self.Npc = NPC("Hello,\n Would you like to go for an adventure ? \n YES or NO \n if you click on 'YES' you will be taken to the adventure, \n but if you say 'NO' the current adventure will end.")
        self.sprites = self.Npc.create_buttons(self.change_state, self.change_state)

    def run(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    #npc pops up on screen when you press space, you can change the condition as per your requirement
                    if event.key == pygame.K_SPACE:
                        self.npc_state = True
            if not self.npc_state:
                self.screen.fill('black')
                self.level.run()
            else:
                #You need to check for events here as well otherwise you'd not be able to exit the game
                for event in events:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                self.Npc.blit(self.screen)
                self.sprites.update(events)
                self.sprites.draw(self.screen)
            pygame.display.update()
            self.clock.tick(FPS)

    def change_state(self,*args):
        self.npc_state = False

if __name__ == '__main__':
    game = Game()
    game.run()
