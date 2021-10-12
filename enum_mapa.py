"""
@melhamas 11/10/21

NOTE: Funciona de forma semelhante ao enum_personagens.py,
o arquivo é responsável por armazenar todos os tipos de mapas que criarmos. 
A informação de onde os personagens saem, faz mais sentido aqui, que lá no 
enum_personagens.py

NOTE: Criar um novo mapa
A cada mapa criado, ele deve ser previsto no arquivo mapa.py

"""
class EnumMapaInicial:
    LARGURA                 = 800
    ALTURA                  = 600
    TITULO                  = "Starting Template"
    FRONTEIRAS_LIMITADAS    = True
    POSX_INICIAL_PERSONAGEM = LARGURA / 2
    POSY_INICIAL_PERSONAGEM = 0
    
    POSX_INICIAL_INIMIGO    = LARGURA / 2
    POSY_INICIAL_INIMIGO = ALTURA
