
import arcade

class Personagem:
    def __init__(self, largura, altura, posx, posy, txDeslocamento, cor):
        self._largura       = largura
        self._altura        = altura
        self._posx          = posx
        self._posy          = posy
        self._deslocamento  = txDeslocamento
        self._cor           = cor
        self._movHorizontal = True
        self._movVertical   = True
    

    @property
    def largura(self):
        return self._largura
    
    @largura.setter
    def largura(self, largura):
        self._largura = largura
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, altura):
        self._altura = altura
    
    @property
    def posx(self):
        return self._posx
    
    @posx.setter
    def posx(self, posx):
        self._posx = posx
    
    @property
    def posy(self):
        return self._posy
    
    @posy.setter
    def posy(self, posy):
        self._posy = posy
    
    @property
    def deslocamento(self):
        return self._deslocamento
    
    @deslocamento.setter
    def deslocamento(self, deslocamento):
        self._deslocamento = deslocamento
    

    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, cor):
        self._cor = cor

    @property
    def movHorizontal(self):
        return self._movHorizontal
    
    def inverteMovHorizontal(self):
        self._movHorizontal = not self._movHorizontal


    
    @property
    def movVertical(self):
        return self._movVertical
    
    def inverteMovvertical(self):
        self._movVertical = not self._movVertical

    def getExtremidadeInferior(self):
        return self.posy - self.altura / 2
    
    def getExtremidadeSuperior(self):
        return self.posy + self.altura / 2
    
    def getExtremidadeEsquerda(self):
        return self.posx - self.largura / 2
    
    def getExtremidadeDireita(self):
        return self.posx + self.largura / 2


    ##################################  MECÂNICA    

    def moveCima(self):
        self.posy += self.deslocamento

    def moveBaixo(self):
        self.posy -= self.deslocamento

    def moveEsquerda(self):
        self.posx -= self.deslocamento

    def moveDireita(self):
        self.posx += self.deslocamento

    

    







    