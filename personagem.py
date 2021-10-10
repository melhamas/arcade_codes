
import arcade
from enum_personagens import EnumPersonagemA

class Personagem:
    def __init__(self, posx, posy, nomePersonagem):
        
        if(EnumPersonagemA):
            self._largura       = EnumPersonagemA.LARGURA
            self._altura        = EnumPersonagemA.ALTURA
            self._posx          = posx
            self._posy          = posy
            self._deslocamento  = EnumPersonagemA.VELOCIDADE
            self._cor           = EnumPersonagemA.COR
            
            
        
        

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

    ##################################  PERSONAGENS
    def desenhaPersonagemA(self):
        return arcade.draw_rectangle_filled(self.posx, self.posy, EnumPersonagemA.LARGURA, EnumPersonagemA.ALTURA, EnumPersonagemA.COR)


    ##################################  MECÂNICA    

    def moveCima(self):
        self.posy += self.deslocamento

    def moveBaixo(self):
        self.posy -= self.deslocamento

    def moveEsquerda(self):
        self.posx -= self.deslocamento

    def moveDireita(self):
        self.posx += self.deslocamento

    

    







    