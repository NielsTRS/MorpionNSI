# coding: utf-8

import libs.plateau as pl
import pygame
from playsound import playsound


class Core:
    def __init__(self, x: int, y: int):
        """
        Fonction init
        :param x: Taille de la fenêtre en longeur
        :param y: Taille de la fenêtre en largeur
        :type x: int
        :type y: int
        """
        if isinstance(x, int) and isinstance(y, int):
            pygame.font.init()

            # taille de la fenêtre
            self.x = x
            self.y = y

            # variables de jeu
            self.game_status = 0
            self.status = True

            # variables de surface
            self.surf = pygame.display.set_mode((self.x, self.y))
            self.surf_pions = pygame.display.set_mode((self.x, self.y))
            self.index_pions = [(132, 137), (285, 137), (434, 137), (132, 291), (285, 291), (434, 291), (132, 439),
                                (285, 439), (434, 439), ]

            # variables des joueurs
            self.player = -1
            self.players_pions = [
                pygame.transform.scale(self.__loadImage('./assets/images/players/circle.png'), (144, 144)),
                pygame.transform.scale(self.__loadImage('./assets/images/players/cross.png'), (144, 144))]

            # variables de font
            self.my_font = pygame.font.Font('./assets/fonts/montserrat.ttf', 36)
            self.text_displays = {
                "current_player": (676, 137),
                "rejouer": (660, 274),
                "victoire": (680, 230)
            }

            # variables pour l'image du jeu contre un bot
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

            # variables pour l'image du jeu en local
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

            # variables pour l'image du jeu en ligne
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

            # variables pour l'image de croix afin de terminer le jeu
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

            # variables pour l'image de boucle afin de recommencer le jeu
            self.replay_image = self.__loadImage('./assets/images/buttons/replay.png')
            self.replay_image_rect = pygame.rect.Rect.move(
                pygame.transform.scale(self.replay_image, (471, 172)).get_rect(), self.text_displays["rejouer"])

        else:
            raise TypeError("Les paramètres doivent être définis par des nombres")

    def start(self):
        """
        Fonction afin de lancer le jeu
        :return:
        """
        self.__showIndex()
        while self.status:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.status = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # clic gauche
                        if self.game_status == 0:  # Menu principal
                            if self.bot_image_rect.collidepoint(event.pos) or self.online_image_rect.collidepoint(
                                    event.pos):  # modes non disponibles pour le moment
                                playsound('./assets/sounds/no.mp3')

                            if self.local_image_rect.collidepoint(event.pos):  # mode local
                                self.__setBackgroundImage('./assets/images/game_screen.png')
                                self.surf.blit(self.local_image_icn,
                                               (self.local_sizes['pos_x_icn'], self.local_sizes['pos_y_icn']))
                                self.surf.blit(self.close_image, (self.close_sizes['pos_x'], self.close_sizes['pos_y']))
                                self.game_status = 2  # Démarrage de la partie en mode local
                                self.plateau = pl.Plateau([0, 0, 0, 0, 0, 0, 0, 0, 0])
                                self.__showTurn()
                                self.__showPions()

                        if self.game_status > 0:  # Partie démarrée et "non-finie"
                            if self.close_image_rect.collidepoint(event.pos):  # retourne à l'accueil
                                self.__showIndex()
                                self.game_status = 0

                            if self.game_status < 4:
                                index = self.__getIndex(event.pos)
                                if index >= 0:
                                    temp = self.plateau.add(index, self.player)
                                    if temp > 0:
                                        self.surf_pions.fill((255, 255, 255), (self.text_displays["current_player"][0],
                                                                               self.text_displays["current_player"][
                                                                                   1] - 20, 308, 122))
                                        self.__showPions()
                                        if temp == 2:
                                            self.game_status = 4
                                            new_text = self.__createText(
                                                f"J{int(0.5 * (self.player) + 1.5)} remporte la victoire !")
                                            self.surf_pions.blit(new_text, self.text_displays["victoire"])
                                            self.surf_pions.blit(self.__loadImage('./assets/images/buttons/replay.png'),
                                                                 self.text_displays["rejouer"])
                                        else:
                                            self.player *= -1
                                            self.__showTurn()

                                    else:
                                        playsound('./assets/sounds/no.mp3')
                            if self.game_status == 4:
                                if self.replay_image_rect.collidepoint(event.pos):
                                    self.game_status = 0
                                    self.__showIndex()
            pygame.display.flip()

    def __showIndex(self):
        """
        Fonction privée pour montrer la page d'accueil
        :return:
        """
        self.__setBackgroundImage('./assets/images/main_menu.png')
        self.surf.blit(self.bot_image, (self.bot_sizes['pos_x'], self.bot_sizes['pos_y']))
        self.surf.blit(self.local_image, (self.local_sizes['pos_x'], self.local_sizes['pos_y']))
        self.surf.blit(self.online_image, (self.online_sizes['pos_x'], self.online_sizes['pos_y']))

    def __loadImage(self, image: str):
        """
        Fonction privée pour charger une image
        :param image: link of the image
        :type image: str
        :return:
        """
        return pygame.image.load(fr'{image}').convert_alpha()

    def __setBackgroundImage(self, image: str):
        """
        Fonction privée pour charger une image en fond
        :param image: link of the image
        :type image: str
        :return:
        """
        self.surf.blit(self.__loadImage(image), (0, 0))

    def __getIndex(self, pos):
        """
        Retourne les indices
        :param pos:
        :return:
        """
        x = pos[0]
        y = pos[1]
        for i in range(0, len(self.index_pions)):
            if self.index_pions[i][0] <= x <= self.index_pions[i][0] + 144 and self.index_pions[i][1] <= y <= \
                    self.index_pions[i][1] + 144:
                return i
        return -1

    def __showPions(self):
        """
        Affiche les pions sur leur emplacement dans le plateau
        """
        pions = self.plateau.pions
        for i in range(0, len(pions)):
            if pions[i] != 0:
                self.surf_pions.blit(self.players_pions[int(0.5 * pions[i] + 0.5)], self.index_pions[i])

    def __createText(self, text, color=(0, 0, 0)):
        """
        Créer un nouveau texte
        :param text: Champ
        :param color: Couleur choisie
        :type text: String
        :type color: Tuple
        """
        return self.my_font.render(text, False, color)

    def __showTurn(self):
        """
        Affiche les éléments
        :return:
        """
        self.current_player = self.__createText(f"Au tour de J{int(0.5 * self.player + 1.5)}:")
        self.surf_pions.blit(self.current_player, self.text_displays["current_player"])
        self.surf_pions.blit(pygame.transform.scale(self.players_pions[int(0.5 * self.player + 0.5)], (71, 71)),
                             (910, 125))
