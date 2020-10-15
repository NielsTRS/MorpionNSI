# coding: utf-8

import pygame
import libs.plateau as pl

class Core:
    def __init__(self, x: int, y: int):
        """
        Init function to setup the game
        :param x: Taille de la fenêtre en longeur
        :param y: Taille de la fenêtre en largeur
        :type x: int
        :type y: int
        """
        if isinstance(x, int) and isinstance(y, int):
            self.x = x
            self.y = y
            self.game_status = 0
            self.status = True
            self.surf = pygame.display.set_mode((self.x, self.y))
            self.surf_pions = pygame.display.set_mode((self.x, self.y))
            pygame.font.init()
            self.my_font = pygame.font.Font('./assets/fonts/montserrat.ttf', 30)
            self.bot_image = self.__loadImage('./assets/images/modes/bot.png')
            self.bot_sizes = {
                'x': 261,
                'x_icn': 120,
                'y': 261,
                'y_icn': 120,
                'pos_x': 117,
                'pos_x_icn': 20,
                'pos_y': 340,
                'pos_y_icn': 10,
            }
            self.bot_image = pygame.transform.scale(self.bot_image, (self.bot_sizes['x'], self.bot_sizes['y']))
            self.bot_image_icn = pygame.transform.scale(self.bot_image,
                                                        (self.bot_sizes['x_icn'], self.bot_sizes['y_icn']))
            self.bot_image_rect = pygame.rect.Rect.move(self.bot_image.get_rect(), self.bot_sizes['pos_x'],
                                                        self.bot_sizes['pos_y'])

            self.local_image = self.__loadImage('./assets/images/modes/local.png')
            self.local_sizes = {
                'x': 261,
                'x_icn': 120,
                'y': 261,
                'y_icn': 120,
                'pos_x': 511,
                'pos_x_icn': 20,
                'pos_y': 340,
                'pos_y_icn': 10,
            }
            self.local_image = pygame.transform.scale(self.local_image, (self.local_sizes['x'], self.local_sizes['y']))
            self.local_image_icn = pygame.transform.scale(self.local_image,
                                                          (self.local_sizes['x_icn'], self.local_sizes['y_icn']))
            self.local_image_rect = pygame.rect.Rect.move(self.local_image.get_rect(), self.local_sizes['pos_x'],
                                                          self.local_sizes['pos_y'])

            self.online_image = self.__loadImage('./assets/images/modes/online.png')
            self.online_sizes = {
                'x': 261,
                'x_icn': 120,
                'y': 261,
                'y_icn': 120,
                'pos_x': 905,
                'pos_x_icn': 20,
                'pos_y': 340,
                'pos_y_icn': 10,

            }
            self.online_image = pygame.transform.scale(self.online_image,
                                                       (self.online_sizes['x'], self.online_sizes['y']))
            self.online_image_icn = pygame.transform.scale(self.online_image,
                                                           (self.online_sizes['x_icn'], self.online_sizes['y_icn']))
            self.online_image_rect = pygame.rect.Rect.move(self.online_image.get_rect(), self.online_sizes['pos_x'],
                                                           self.online_sizes['pos_y'])

            self.close_image = self.__loadImage('./assets/images/buttons/quit.png')
            self.close_sizes = {
                'x': 58,
                'y': 58,
                'pos_x': 1175,
                'pos_y': 45
            }
            self.close_image = pygame.transform.scale(self.close_image, (self.close_sizes['x'], self.close_sizes['y']))
            self.close_image_rect = pygame.rect.Rect.move(self.close_image.get_rect(), self.close_sizes['pos_x'],
                                                          self.close_sizes['pos_y'])

            self.index_pions = [
                (132,137),
                (285,137),
                (434,137),
                
                (132,291),
                (285,291),
                (434,291),

                (132,439),
                (285,439),
                (434,439),
            ]
            self.player = -1
            self.pions = []

            self.players_pions = [pygame.transform.scale(self.__loadImage('./assets/images/players/circle.png'), (144, 144)),pygame.transform.scale(self.__loadImage('./assets/images/players/cross.png'), (144, 144))]
        else:
            raise TypeError("Les paramètres doivent être définis par des nombres")

    def start(self):
        """
        Main function to start the game
        :return:
        """
        self.__showIndex()
        while self.status:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.status = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # left clic
                        if self.game_status == 0: #Menu principal
                            if self.bot_image_rect.collidepoint(event.pos): #bot mode
                                self.__setBackgroundImage('./assets/images/game_screen.png')
                                self.surf.blit(self.bot_image_icn,
                                            (self.bot_sizes['pos_x_icn'], self.bot_sizes['pos_y_icn']))
                                self.surf.blit(self.close_image, (self.close_sizes['pos_x'], self.close_sizes['pos_y']))
                                self.game_status = 1 # Démarrage de la partie en mode J1 Vs AI

                            if self.local_image_rect.collidepoint(event.pos): #local mode
                                self.__setBackgroundImage('./assets/images/game_screen.png')
                                self.surf.blit(self.local_image_icn,
                                            (self.local_sizes['pos_x_icn'], self.local_sizes['pos_y_icn']))
                                self.surf.blit(self.close_image, (self.close_sizes['pos_x'], self.close_sizes['pos_y']))
                                self.game_status = 2 # Démarrage de la partie en mode local
                                self.plateau = pl.Plateau([0,0,0,0,0,0,0,0,0])
                                self.__showPions()

                            if self.online_image_rect.collidepoint(event.pos): #online mode
                                self.__setBackgroundImage('./assets/images/game_screen.png')
                                self.surf.blit(self.online_image_icn,
                                            (self.online_sizes['pos_x_icn'], self.online_sizes['pos_y_icn']))
                                self.surf.blit(self.close_image, (self.close_sizes['pos_x'], self.close_sizes['pos_y']))
                                self.game_status = 3 # Démarrage de la partie en mode J1 Vs J2

                        if self.game_status > 0 and self.game_status < 4: #Partie démarrée et "non-finie"
                            print(event.pos)
                            if self.close_image_rect.collidepoint(event.pos): #return to index
                                self.__showIndex()
                                self.game_status = 0
                            
                            index = self.__getIndex(event.pos)
                            if index >= 0:
                                temp = self.plateau.add(index, self.player)
                                if temp > 0:
                                    print(f"Pion placé en index {index+1} par le joueur {self.player}")
                                    self.player *= -1
                                    self.__showPions()
                                    if temp == 2:
                                        print("VICTOIRE !!!")
                                else:
                                    print(f"Le pion placé en index {index+1} n'a pas pu être placé en {self.player}")


            pygame.display.flip()

    def __showIndex(self):
        """
        Private function to show the index window
        :return:
        """
        self.__setBackgroundImage('./assets/images/main_menu.png')
        self.surf.blit(self.bot_image, (self.bot_sizes['pos_x'], self.bot_sizes['pos_y']))
        self.surf.blit(self.local_image, (self.local_sizes['pos_x'], self.local_sizes['pos_y']))
        self.surf.blit(self.online_image, (self.online_sizes['pos_x'], self.online_sizes['pos_y']))

    def __loadImage(self, image: str):
        """
        Private function to load an image
        :param image: link of the image
        :type image: str
        :return:
        """
        return pygame.image.load(fr'{image}').convert_alpha()

    def __setBackgroundImage(self, image: str):
        """
        Show the image in background
        :param image: link of the image
        :type image: str
        :return:
        """
        self.surf.blit(self.__loadImage(image), (0, 0))

    def __getIndex(self, pos):
        x = pos[0]
        y = pos[1]
        for i in range(0,len(self.index_pions)):
            if self.index_pions[i][0] <= x <= self.index_pions[i][0]+144 and self.index_pions[i][1] <= y <= self.index_pions[i][1]+144:
                return i
        return -1

    def __showPions(self):
        """
        Description: Affiche les pions sur leur emplacement dans le plateau
        """
        print(self.plateau.pions)
        pions = self.plateau.pions
        for i in range(0,len(pions)):
            if pions[i] != 0:
                # print(f"Pion détecté en index {i+1}")
                self.surf_pions.blit(self.players_pions[int(0.5*pions[i]+0.5)], self.index_pions[i])
