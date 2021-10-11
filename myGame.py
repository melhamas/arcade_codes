"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
from enum_personagens import EnumPersonagemInimigo, EnumPersonagemMelhamas
from personagem import Personagem
from mapa import Mapa
from enum_mapa import EnumMapaInicial
from controle import Controle



class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, mapa, personagem):
        super().__init__(mapa.LARGURA, mapa.ALTURA, mapa.TITULO)

        arcade.set_background_color(arcade.color.BLEU_DE_FRANCE)
        
        self.mapa       = Mapa(mapa.LARGURA, mapa.ALTURA, mapa.TITULO)
        self.personagem = Personagem(mapa.POSX_INICIAL_PERSONAGEM, mapa.POSY_INICIAL_PERSONAGEM, personagem)
        self.inimigo    = Personagem(mapa.POSX_INICIAL_INIMIGO, mapa.POSY_INICIAL_INIMIGO, EnumPersonagemInimigo) 
        self.controleA  = Controle(True)
        self.controleB  = Controle(False)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        arcade.start_render()

        # Call draw() on all your sprite lists below
        self.personagem.desenhaPersonagemA()
        self.inimigo.desenhaPersonagemA()


        
    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        

        
        self.controleA.executaMovimentos(self.personagem)
        
        self.controleB.executaMovimentos(self.inimigo)
        #self.mapa.mov_intermitente_horizontal(self.inimigo)
        #self.mapa.mov_intermitente_vertical(self.inimigo)
        
            

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        self.controleA.teclaPressionadaParaLiberar(key)
        self.controleB.teclaPressionadaParaLiberar(key)

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        self.controleA.teclaPressionadaParaBloquear(key)
        self.controleB.teclaPressionadaParaBloquear(key)

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main function """
    game = MyGame(EnumMapaInicial, EnumPersonagemMelhamas)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()