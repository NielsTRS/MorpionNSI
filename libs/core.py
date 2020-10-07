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

        bot_image = self.__setImage('./assets/images/modes/bot.png')
        bot_sizes = {
            'x': 261,
            'y': 261,
            'pos_x': 117,
            'pos_y': 340
        }
        bot_image = pygame.transform.scale(bot_image, (bot_sizes['x'], bot_sizes['y']))
        bot_image_rect = pygame.rect.Rect.move(bot_image.get_rect(), bot_sizes['pos_x'], bot_sizes['pos_y'])

        local_image = self.__setImage('./assets/images/modes/local.png')
        local_sizes = {
            'x': 261,
            'y': 261,
            'pos_x': 511,
            'pos_y': 340
        }
        local_image = pygame.transform.scale(local_image, (local_sizes['x'], local_sizes['y']))
        local_image_rect = pygame.rect.Rect.move(local_image.get_rect(), local_sizes['pos_x'], local_sizes['pos_y'])

        online_image = self.__setImage('./assets/images/modes/online.png')
        online_sizes = {
            'x': 261,
            'y': 261,
            'pos_x': 905,
            'pos_y': 340
        }
        online_image = pygame.transform.scale(online_image, (online_sizes['x'], online_sizes['y']))
        online_image_rect = pygame.rect.Rect.move(online_image.get_rect(), online_sizes['pos_x'], online_sizes['pos_y'])

        run = True
        while run:
            self.surf.blit(background_image, (0, 0))
            self.surf.blit(bot_image, (bot_sizes['pos_x'], bot_sizes['pos_y']))
            self.surf.blit(local_image, (local_sizes['pos_x'], local_sizes['pos_y']))
            self.surf.blit(online_image, (online_sizes['pos_x'], online_sizes['pos_y']))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # clic gauche
                        if bot_image_rect.collidepoint(event.pos):
                            self.bot()
                        if local_image_rect.collidepoint(event.pos):
                            self.friend()
                        if online_image_rect.collidepoint(event.pos):
                            self.stranger()
                        # if close_area.collidepoint(event.pos):
                        #     print('close')
            pygame.display.update()
        pygame.quit()

    def __setImage(self, image: str):
        return pygame.image.load(fr'{image}').convert_alpha()

    def bot(self):
        print('bot')

    def friend(self):
        print('friend')

    def stranger(self):
        print('stranger')
