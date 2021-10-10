"""
Starting Template

Once you have learned how to use classes, you can begin your program with this
template.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.starting_template
"""
import arcade
from personagem import Personagem
from mapa import Mapa


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"

#Constantes personagem principal
LARGURA_PERSONAGEM = 100
ALTURA_PERSONAGEM = 100
POSX_INICIAL_PERSONAGEM = SCREEN_WIDTH / 2 + LARGURA_PERSONAGEM / 2
POSY_INICIAL_PERSONAGEM = ALTURA_PERSONAGEM / 2

class MyGame(arcade.Window):
    """
    Main application class.

    NOTE: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code. Don't leave 'pass' in this program.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLEU_DE_FRANCE)
        
        self.mapa = Mapa(width, height, title)
        self.personagem = Personagem(LARGURA_PERSONAGEM, ALTURA_PERSONAGEM, POSX_INICIAL_PERSONAGEM, POSY_INICIAL_PERSONAGEM, 2, arcade.color.YELLOW)
        

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
        arcade.draw_rectangle_filled(self.personagem.posx, self.personagem.posy, self.personagem.largura, self.personagem.altura, self.personagem.cor)


        

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.mapa.mov_intermitente_vertical(self.personagem)
        self.mapa.mov_intermitente_horizontal(self.personagem)
                
        
            

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

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
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()