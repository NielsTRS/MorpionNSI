# coding: utf-8
class Player():
    def __init__(self):
        self.victoires = 0
        self.defaites = 0
        self.nuls = 0
    def nouvelleVictoire(self):
        self.victoires += 1
    def nouvelleDefaite(self):
        self.defaites += 1
    def nouveauMatchNul(self):
        self.nuls += 1
