"""
@msvinicioos
"""

from enum_controle import EnumControle, EnumControle_B
from personagem import Personagem
from enum_mapa import EnumMapaInicial

from personagem import Personagem

class Controle:

    def __init__(self, jogadorPrincipal: bool):
        self._jogadorPrincpal    = jogadorPrincipal
        self._movimentoParaCima  = False
        self._movimentoParaDir   = False
        self._movimentoParaBaixo = False
        self._movimentoParaEsq   = False


    ############################### GETTERS    
    @property
    def jogadorPrincipal(self):
        return self._jogadorPrincpal
    
    @property
    def movimentoParaCima(self):
        return self._movimentoParaCima

    @property
    def movimentoParaDir(self):
        return self._movimentoParaDir

    @property
    def movimentoParaBaixo(self):
        return self._movimentoParaBaixo

    @property
    def movimentoParaEsq(self):
        return self._movimentoParaEsq

    
    ################################ BLOQUEIOS E LIBERAÇÕES
    def liberaMovimentoParaCima(self):
        self._movimentoParaCima = True
    
    def liberaMovimentoParaDir(self):
        self._movimentoParaDir = True

    def liberaMovimentoParaBaixo(self):
        self._movimentoParaBaixo = True

    def liberaMovimentoParaEsq(self):
        self._movimentoParaEsq = True
    
    def bloqueiaMovimentoParaCima(self):
        self._movimentoParaCima = False
    
    def bloqueiaMovimentoParaDir(self):
        self._movimentoParaDir = False

    def bloqueiaMovimentoParaBaixo(self):
        self._movimentoParaBaixo = False

    def bloqueiaMovimentoParaEsq(self):
        self._movimentoParaEsq = False
    
    
    ################################ IDENTIFICANDO MOVIMENTOS DO PERSONAGEM E DO INIMIGO
    
    
    def teclaPressionadaParaLiberar(self, tecla):
        if(self.jogadorPrincipal):
            if(tecla == EnumControle.TECLA_CIMA):
                self.liberaMovimentoParaCima()
            elif(tecla == EnumControle.TECLA_DIR):
                self.liberaMovimentoParaDir()
            elif(tecla == EnumControle.TECLA_BAIXO):
                self.liberaMovimentoParaBaixo()
            elif(tecla == EnumControle.TECLA_ESQ):
                self.liberaMovimentoParaEsq()
        else:
            if(tecla == EnumControle_B.TECLA_CIMA_INIMIGO):
                self.liberaMovimentoParaCima()
            elif(tecla == EnumControle_B.TECLA_DIR_INIMIGO):
                self.liberaMovimentoParaDir()
            elif(tecla == EnumControle_B.TECLA_BAIXO_INIMIGO):
                self.liberaMovimentoParaBaixo()
            elif(tecla == EnumControle_B.TECLA_ESQ_INIMIGO):
                self.liberaMovimentoParaEsq()
    
    def teclaPressionadaParaBloquear(self, tecla):
        if(self.jogadorPrincipal):
            if(tecla == EnumControle.TECLA_CIMA):
                self.bloqueiaMovimentoParaCima()
            elif(tecla == EnumControle.TECLA_DIR):
                self.bloqueiaMovimentoParaDir()
            elif(tecla == EnumControle.TECLA_BAIXO):
                self.bloqueiaMovimentoParaBaixo()
            elif(tecla == EnumControle.TECLA_ESQ):
                self.bloqueiaMovimentoParaEsq()
        else:
            if(tecla == EnumControle_B.TECLA_CIMA_INIMIGO):
                self.bloqueiaMovimentoParaCima()
            elif(tecla == EnumControle_B.TECLA_DIR_INIMIGO):
                self.bloqueiaMovimentoParaDir()
            elif(tecla == EnumControle_B.TECLA_BAIXO_INIMIGO):
                self.bloqueiaMovimentoParaBaixo()
            elif(tecla == EnumControle_B.TECLA_ESQ_INIMIGO):
                self.bloqueiaMovimentoParaEsq()



    ################################## MOVIMENTOS
    def executaMovimentos(self, personagem: Personagem):
        if(self.movimentoParaCima):
            if(not EnumMapaInicial.FRONTEIRAS_LIMITADAS):
                personagem.moveCima() 
            else:
                if(personagem.getExtremidadeSuperior() < EnumMapaInicial.ALTURA):
                    personagem.moveCima() 

        
        if(self.movimentoParaDir):
            if(not EnumMapaInicial.FRONTEIRAS_LIMITADAS):
                personagem.moveDireita()
            else:
                if(personagem.getExtremidadeDireita() < EnumMapaInicial.LARGURA):
                    personagem.moveDireita() 
        
        
        if(self.movimentoParaBaixo):
            if(not EnumMapaInicial.FRONTEIRAS_LIMITADAS):
                personagem.moveBaixo()
            else:
                if(personagem.getExtremidadeInferior() > 0):
                    personagem.moveBaixo() 

        if(self.movimentoParaEsq):
            if(not EnumMapaInicial.FRONTEIRAS_LIMITADAS):
                personagem.moveEsquerda()
            else:
                if(personagem.getExtremidadeEsquerda() > 0):
                    personagem.moveEsquerda() 
    