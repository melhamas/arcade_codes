from enum_controle import EnumControle
from personagem import Personagem


from personagem import Personagem

class Controle:

    def __init__(self):
        self._movimentoParaCima  = False
        self._movimentoParaDir   = False
        self._movimentoParaBaixo = False
        self._movimentoParaEsq   = False


    ############################### GETTERS    
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
    
    
    ################################ IDENTIFICANDO MOVIMENTOS
    def teclaPressionadaParaLiberar(self, tecla):
        if(tecla == EnumControle.TECLA_CIMA):
            self.liberaMovimentoParaCima()
        elif(tecla == EnumControle.TECLA_DIR):
            self.liberaMovimentoParaDir()
        elif(tecla == EnumControle.TECLA_BAIXO):
            self.liberaMovimentoParaBaixo()
        elif(tecla == EnumControle.TECLA_ESQ):
            self.liberaMovimentoParaEsq()
    
    def teclaPressionadaParaBloquear(self, tecla):
        if(tecla == EnumControle.TECLA_CIMA):
            self.bloqueiaMovimentoParaCima()
        elif(tecla == EnumControle.TECLA_DIR):
            self.bloqueiaMovimentoParaDir()
        elif(tecla == EnumControle.TECLA_BAIXO):
            self.bloqueiaMovimentoParaBaixo()
        elif(tecla == EnumControle.TECLA_ESQ):
            self.bloqueiaMovimentoParaEsq()
    



    ################################## MOVIMENTOS
    def executaMovimentos(self, personagem: Personagem):
        if(self.movimentoParaCima):
            personagem.moveCima()
        
        if(self.movimentoParaDir):
            personagem.moveDireita()
        
        if(self.movimentoParaBaixo):
            personagem.moveBaixo()
        
        if(self.movimentoParaEsq):
            personagem.moveEsquerda()

    