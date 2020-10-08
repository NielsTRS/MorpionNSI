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
            self.status = True
        else:
            raise TypeError("Les paramètres doivent être définis par des nombres")

    def start(self):
        pygame.init()
        pygame.font.init()
        while self.status:
            self.showIndex()
            pygame.display.flip()

    def showIndex(self):
        bot_image = self.__loadImage('./assets/images/modes/bot.png')
        bot_sizes = {
            'x': 261,
            'y': 261,
            'pos_x': 117,
            'pos_y': 340
        }
        bot_image = pygame.transform.scale(bot_image, (bot_sizes['x'], bot_sizes['y']))
        bot_image_rect = pygame.rect.Rect.move(bot_image.get_rect(), bot_sizes['pos_x'], bot_sizes['pos_y'])

        local_image = self.__loadImage('./assets/images/modes/local.png')
        local_sizes = {
            'x': 261,
            'y': 261,
            'pos_x': 511,
            'pos_y': 340
        }
        local_image = pygame.transform.scale(local_image, (local_sizes['x'], local_sizes['y']))
        local_image_rect = pygame.rect.Rect.move(local_image.get_rect(), local_sizes['pos_x'], local_sizes['pos_y'])

        online_image = self.__loadImage('./assets/images/modes/online.png')
        online_sizes = {
            'x': 261,
            'y': 261,
            'pos_x': 905,
            'pos_y': 340
        }
        online_image = pygame.transform.scale(online_image, (online_sizes['x'], online_sizes['y']))
        online_image_rect = pygame.rect.Rect.move(online_image.get_rect(), online_sizes['pos_x'], online_sizes['pos_y'])

        self.__setBackgroundImage('./assets/images/main_menu.png')
        self.surf.blit(bot_image, (bot_sizes['pos_x'], bot_sizes['pos_y']))
        self.surf.blit(local_image, (local_sizes['pos_x'], local_sizes['pos_y']))
        self.surf.blit(online_image, (online_sizes['pos_x'], online_sizes['pos_y']))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # clic gauche
                    if bot_image_rect.collidepoint(event.pos):
                        self.showBot()
                    if local_image_rect.collidepoint(event.pos):
                        self.showLocal()
                    if online_image_rect.collidepoint(event.pos):
                        self.showOnline()

    def showBot(self):
        self.__setBackgroundImage('./assets/images/game_screen.png')

    def showLocal(self):
        print('friend')

    def showOnline(self):
        print('stranger')

    def __loadImage(self, image: str):
        return pygame.image.load(fr'{image}').convert_alpha()

    def __setBackgroundImage(self, image: str):
        self.surf.blit(self.__loadImage(image), (0, 0))
