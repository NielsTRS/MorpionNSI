class Plateau:
    def __init__(self, pions=None):
        """
        Fonction init
        :param pions:
        """
        if pions is None:
            pions = []
        self.fill(pions)
        self.coups = 0

    def add(self, i: int, player: int):
        """
        Rajoute un pion à la case "i" souhaitée pour le joueur "player"
        :param i: Index de la case compris entre 0 et 8 inclus
        :type i: int 
        :param player: Numéro du joueur (1 pour J1 et -1 pour J2)
        :type i: int
        """
        if len(self.pions) < i or i < 0 or not isinstance(i, int):
            raise ValueError(
                f"{i} n'est pas une valeur valide (essayez avec un entier entre 0 et {len(self.pions) - 1})")
        if self.pions[i] != 0:
            return 0
        else:
            self.pions[i] = player
            self.coups += 1
            if self.coups > 4 and self.check_win(i, player):
                return 2
            return 1

    def win(self, player):
        """
        Exécute le code final lorsqu'une victoire est testée !
        :param player: Le joueur qui a remporté cette manche (1 pour J1 et -1 pour J2)
        :type player: int
        """
        # TODO
        print(f"Le joueur {player} a gagné !")

    def fill(self, pions=None):
        """
        Rempli le plateau avec des cases vides ou prédéfinies
        :param pions: Liste des cases prédéfinies (laissez vide pour remplir normalement)
        :type pions: array
        """
        if pions is None:
            pions = []
        self.pions = [0 for i in range(0, 9)] if len(pions) == 0 else pions

    def reset(self):
        """
        Vide et rempli le plateau
        """
        self.fill()
        self.pions = [0 for i in range(0, 9)]

    def check_win(self, i, player):
        """
        Vérifie les condition d'une victoire
        :param i: Case à vérifier (entre 0 et 8 inclus)
        :type i: int
        :param player: Le dernier joueur à avoir joué.
        :type player: int
        """
        # Victoire par Ligne
        if i < 3:
            l = 1
        elif 6 > i >= 3:
            l = 2
        else:
            l = 3
        if self.pions[(3 * l - 3)] == player and self.pions[3 * l - 2] == player and self.pions[3 * l - 1] == player:
            return True

        # Victoire par Colonne
        if i == 0 or i == 3 or i == 6:
            c = 1
        elif i == 1 or i == 4 or i == 7:
            c = 2
        else:
            c = 3
        if self.pions[c * 1 - 1] == player and self.pions[c * 1 + 2] == player and self.pions[c * 1 + 5] == player:
            return True

        # Victoire par Diagonale
        try:
            [0, 2, 4, 6, 8].index(i)  # On vérifie si le pion posé se trouve sur les coins ou au centre.
            if self.pions[0] == player and self.pions[4] == player and self.pions[
                8]:  # Diagonale haut gauche vers bas droite
                return True
            elif self.pions[2] == player and self.pions[4] == player and self.pions[
                6] == player:  # Diagonale haute droite vers bas gauche
                return True
        except:
            return False

    def __str__(self):
        """
        Affichage du plateau dans la console via un print
        """
        text = ""
        for i in range(0, 3):
            if i != 0: text += "\n"
            for j in range(i * 3, i * 3 + 3):
                text += "   " if (self.pions[j] == 0) else " X " if self.pions[j] == 1 else " O "
        return text
