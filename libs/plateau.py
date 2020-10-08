class Plateau():
    def __init__(self, pions = []):
        self.fill(pions)
        self.coups = 0
    
    def add(self, i, player):
        if len(self.pions) < i or i < 0 or not isinstance(i, int):
            raise ValueError(f"{i} n'est pas une valeur valide (essayez avec un entier entre 0 et {len(self.pions)-1})")
        if self.pions[i] >= 1:
            return False
        else:
            self.pions[i] = player
            self.coups += 1
            if self.coups > 4: self.check_win(i, player)
            return True

    def fill(self, pions = []):
        self.pions = [0 for i in range(0,9)] if len(pions) == 0 else pions

    def reset(self):
        self.fill()
        self.pions = [0 for i in range(0,9)]

    def check_win(self, i, player):
        # Ligne
        if i < 3: l = 1
        elif i < 6 and i >= 3: l = 2
        else: l = 3
        print(l)
        # Colonne

        # Diagonale



    def __str__(self):
        print(self.pions)
        text = ""
        for i in range(0,3):
            if i!=0: text+="\n"
            for j in range(i*3,i*3+3):
                text += "   " if (self.pions[j] == 0) else " X " if self.pions[j] == 1 else " O "
        return text

def test():
    tableau = Plateau([
            1, -1, 1,
            1, 0, -1,
            -1, 1, -1
        ])
    tableau.check_win(7,1)
    tableau.check_win(1,1)
    tableau.check_win(2,1)
    tableau.check_win(4,1)


test()