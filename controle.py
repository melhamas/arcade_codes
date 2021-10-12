"""""
@melhamas - 11/10/21

A classe é responsável por controlar um jogador. O padrão de teclas vem do 
enum_controle

A instância de um jogador é definida, de forma inicial como jogador primário: True
ou secundário: False.
"""

from enum_controle import EnumControlePrincpal, EnumControleSecundario
from personagem import Personagem
from enum_mapa import EnumMapaInicial

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
    """
    @melhamas 11/10/21

    NOTE: Um movimento liberado, indica que a biblioteca arcade pode
    ficar atualizando a posição de um personagem. 

    - Movimento Liberado
    A liberação é realizada quando o usuário pressiona uma tecla de movimentação.

    - Movimento Bloqueado
    O bloqueio de um movimento é realizado quando o usuário solta a tecla


    Teclas jogador primário: True {A, S, D, W}
    Teclas jogador secundário: False {LEFT, UP, RIGHT, DOWN}
    
    """
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
    
    """
    NOTE: Aqui as funçções são responsáveis por comparar a tecla pressionada com
    as teclas declaradas do jogador. Caso o match aconteça, as liberações ou bloqueios acontecem.
    """
    
    def teclaPressionadaParaLiberar(self, tecla):
        if(self.jogadorPrincipal):
            if(tecla == EnumControlePrincpal.TECLA_CIMA):
                self.liberaMovimentoParaCima()
            elif(tecla == EnumControlePrincpal.TECLA_DIR):
                self.liberaMovimentoParaDir()
            elif(tecla == EnumControlePrincpal.TECLA_BAIXO):
                self.liberaMovimentoParaBaixo()
            elif(tecla == EnumControlePrincpal.TECLA_ESQ):
                self.liberaMovimentoParaEsq()
        else:
            if(tecla == EnumControleSecundario.TECLA_CIMA_INIMIGO):
                self.liberaMovimentoParaCima()
            elif(tecla == EnumControleSecundario.TECLA_DIR_INIMIGO):
                self.liberaMovimentoParaDir()
            elif(tecla == EnumControleSecundario.TECLA_BAIXO_INIMIGO):
                self.liberaMovimentoParaBaixo()
            elif(tecla == EnumControleSecundario.TECLA_ESQ_INIMIGO):
                self.liberaMovimentoParaEsq()
    
    def teclaPressionadaParaBloquear(self, tecla):
        if(self.jogadorPrincipal):
            if(tecla == EnumControlePrincpal.TECLA_CIMA):
                self.bloqueiaMovimentoParaCima()
            elif(tecla == EnumControlePrincpal.TECLA_DIR):
                self.bloqueiaMovimentoParaDir()
            elif(tecla == EnumControlePrincpal.TECLA_BAIXO):
                self.bloqueiaMovimentoParaBaixo()
            elif(tecla == EnumControlePrincpal.TECLA_ESQ):
                self.bloqueiaMovimentoParaEsq()
        else:
            if(tecla == EnumControleSecundario.TECLA_CIMA_INIMIGO):
                self.bloqueiaMovimentoParaCima()
            elif(tecla == EnumControleSecundario.TECLA_DIR_INIMIGO):
                self.bloqueiaMovimentoParaDir()
            elif(tecla == EnumControleSecundario.TECLA_BAIXO_INIMIGO):
                self.bloqueiaMovimentoParaBaixo()
            elif(tecla == EnumControleSecundario.TECLA_ESQ_INIMIGO):
                self.bloqueiaMovimentoParaEsq()



    ################################## MOVIMENTOS

    """
    NOTE: A execução dos movimentos é dada nas seguintes funções. Quando chamadas, 
    as funções se preocupam apenas em executar a movimentação, supõe-se que as teclas já foram presisonadas.

    O único controle que existe é com relação à flag FRONTEIRAS_LIMITADAS que vem do arquivo enum_mapa.py
    que, se True existe as limitações de fronteiras e caso False, não há fronteiras.
    """
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
    