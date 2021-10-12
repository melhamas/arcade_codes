import arcade

"""
@melhamas 11/10/21

NOTE: Arquivo responsável por guardar as características dos personagens

NOTE: Criar um novo personagem
A cada novo personagem criado, ele deve ser previsto no arquivo 
personagem.py

NOTE: MELHORIAS

* Verificar possibilidade de já colocar o formato dos personagens aqui. 
Problema: as posições de saída dos personagens que está no enum_mapa.py
"""

class EnumPersonagemMelhamas:
    LARGURA     = 100
    ALTURA      = 100
    COR         = arcade.color.YELLOW
    VELOCIDADE  = 10
    

class EnumPersonagemInimigo:
    LARGURA     = 50
    ALTURA      = 50
    COR         = arcade.color.RED
    VELOCIDADE  = 50