# coding: utf-8

import pygame


class Core:
    def __init__(self, x: int, y: int):
        """
        :param x: Taille de la fenêtre en longeur
        :param y: Taille de la fenêtre en largeur
        :type x: int
        :type y: int
        """
        if isinstance(x, int) and isinstance(y, int):
            self.x = x
            self.y = y
            self.surf = pygame.display.set_mode((self.x, self.y))
        else:
            raise TypeError("Les paramètres doivent être définis par des nombres")

    def start(self):
        image = pygame.image.load(r'./assets/images/main_menu.png').convert()

        bot_area = pygame.Rect((117, 340), (261, 261))  # left, top, width, height
        friend_area = pygame.Rect((511, 340), (261, 261))  # left, top, width, height
        stranger_area = pygame.Rect((905, 340), (261, 261))  # left, top, width, height

        run = True
        while run:
            self.surf.blit(image, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # clic gauche
                        if bot_area.collidepoint(event.pos):
                            image = self.__setImage('./assets/images/game_screen.png')
                            self.bot()
                        if friend_area.collidepoint(event.pos):
                            image = self.__setImage('./assets/images/game_screen.png')
                            self.friend()
                        if stranger_area.collidepoint(event.pos):
                            image = self.__setImage('./assets/images/game_screen.png')
                            self.stranger()
            self.surf.blit(image, (0, 0))
            pygame.display.update()
        pygame.quit()

    def __setImage(self, image: str):
        return pygame.image.load(fr'{image}').convert()

    def bot(self):
        return True

    def friend(self):
        return True

    def stranger(self):
        return True
