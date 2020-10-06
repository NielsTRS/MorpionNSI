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
        image = pygame.image.load(r'./assets/images/main_menu.png')
        run = True
        while run:
            surf.blit(image, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()
        pygame.quit()
