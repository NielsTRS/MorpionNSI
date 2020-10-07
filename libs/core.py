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
        background_image = self.__setImage('./assets/images/main_menu.png')

        bot_image = self.__setImage('./assets/images/modes/ia.png')
        bot_image_rect = bot_image.get_rect()
        bot_image = pygame.transform.scale(bot_image, (261, 261))

        local_image = self.__setImage('./assets/images/modes/local.png')
        local_image_rect = local_image.get_rect()
        local_image = pygame.transform.scale(local_image, (261, 261))

        online_image = self.__setImage('./assets/images/modes/online.png')
        online_image_rect = online_image.get_rect()
        online_image = pygame.transform.scale(online_image, (261, 261))

        run = True
        while run:
            self.surf.blit(background_image, (0, 0))
            self.surf.blit(bot_image, (117, 340))
            self.surf.blit(local_image, (511, 340))
            self.surf.blit(online_image, (905, 340))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # clic gauche
                        if bot_image_rect.collidepoint(event.pos):
                            print('bot')
                        if local_image_rect.collidepoint(event.pos):
                            print('friend')
                        if online_image_rect.collidepoint(event.pos):
                            print('stranger')
                        # if close_area.collidepoint(event.pos):
                        #     print('close')
            pygame.display.update()
        pygame.quit()

    def __setImage(self, image: str):
        return pygame.image.load(fr'{image}').convert_alpha()

    def bot(self):
        return True

    def friend(self):
        return True

    def stranger(self):
        return True
