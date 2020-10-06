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
        else:
            raise TypeError("La taille de la fenêtre doivent être défini par des nombres")

    def start(self):
        surf = pygame.display.set_mode((self.x, self.y))
        image = pygame.image.load(r'./assets/images/main_menu.png').convert()

        bot_area = pygame.Rect((117, 340), (261, 261))  # left, top, width, height
        friend_area = pygame.Rect((511, 340), (261, 261))  # left, top, width, height
        stranger_area = pygame.Rect((905, 340), (261, 261))  # left, top, width, height

        run = True
        while run:
            surf.blit(image, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # clic gauche
                        if bot_area.collidepoint(event.pos):
                            self.bot()
                        if friend_area.collidepoint(event.pos):
                            self.friend()
                        if stranger_area.collidepoint(event.pos):
                            self.stranger()

            pygame.display.update()
        pygame.quit()

    def bot(self):
        return True

    def friend(self):
        return True

    def stranger(self):
        return True
