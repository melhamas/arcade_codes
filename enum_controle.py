import arcade

"""
@melhamas 11/10/21

NOTE: Possíveis controles
"""

class EnumControlePrincpal:
    TECLA_CIMA  = arcade.key.W
    TECLA_DIR   = arcade.key.D
    TECLA_BAIXO = arcade.key.S
    TECLA_ESQ   = arcade.key.A

class EnumControleSecundario:
    TECLA_CIMA_INIMIGO  = arcade.key.UP
    TECLA_DIR_INIMIGO   = arcade.key.RIGHT
    TECLA_BAIXO_INIMIGO = arcade.key.DOWN
    TECLA_ESQ_INIMIGO   = arcade.key.LEFT