from enum_mapa import EnumMapaInicial
from personagem import Personagem

"""
@melhamas 11/10/21

NOTE: Classe responsável pela criação dos mapas
"""

class Mapa:
    def __init__(self, mapa):
        
        if(mapa == EnumMapaInicial):
            self._largura = mapa.LARGURA
            self._altura = mapa.ALTURA
            self._nome = mapa.TITULO

    
    
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
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        return self._nome

    ###################################### MECÂNICA
    """
    NOTE: Nessa mecânica, o mapa permite, dado um personagem, automatizar seu movimento
    no mapa.
    """

    def movParaCimaLiberado(self, personagem: Personagem):
        return personagem.getExtremidadeSuperior() < self.altura
            

    def movParaBaixoLiberado(self, personagem: Personagem):
        return personagem.getExtremidadeInferior() > 0
            
    
    def movParaDireitaLiberado(self, personagem: Personagem):
        return personagem.getExtremidadeDireita() < self.largura
    
    def movParaEsquerdaLiberado(self, personagem: Personagem):
        return personagem.getExtremidadeEsquerda() > 0

    
    """"
        NOTE: Movimenta um personagem infinitamente pelo mapa de jogo
    """
    def mov_intermitente_vertical(self, personagem: Personagem):
        if(personagem.movVertical):
            if(self.movParaCimaLiberado(personagem)):
                personagem.moveCima()
            else:
                personagem.inverteMovvertical()
                
        else:
            if(self.movParaBaixoLiberado(personagem)):
                personagem.moveBaixo()
            else:
                personagem.inverteMovvertical()

    def mov_intermitente_horizontal(self, personagem: Personagem):
        #movimento Horizontal
        if(personagem.movHorizontal):
            if(self.movParaDireitaLiberado(personagem)):
                personagem.moveDireita()
            else:
                personagem.inverteMovHorizontal()
                
        else:
            if(self.movParaEsquerdaLiberado(personagem)):
                personagem.moveEsquerda()
            else:
                personagem.inverteMovHorizontal()
    



