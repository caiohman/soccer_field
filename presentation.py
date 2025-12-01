import pygame
import pygame_widgets
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
import os
from video_edition import Video

class Presentation:

    def __init__(self):
        _ = pygame.init()

        screen = pygame.display.set_mode((1280,720))

        image = pygame.image.load(os.path.join("/home/caiohman/repo/soccer_field/", "logo.jpg"))
        image = pygame.transform.scale(image, (150, 150))

        login = self.textField(screen, 400, 400)
        password = self.textField(screen, 400, 500)

        button = self.button(screen, "Login", 450, 600)

        clock = pygame.time.Clock()

        while True:
            # Process player inputs.
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit

            # Do logical updates here.
            # ...

            _ = screen.fill("white")  # Fill the display with a solid color

            # Render the graphics here.
            # ...
            _ = pygame_widgets.update(events)
            _ = screen.blit(image, (450, 200))

            pygame.display.flip()  # Refresh on-screen display
            _ = clock.tick(60)         # wait until next frame (at 60 FPS)


    def textField(self, screen, positionx : int, positiony : int) :
        return TextBox(
            screen,
            positionx,
            positiony,
            200,
            40,
            colour = "white",
            fontSize = 20,
            borderColour = (255, 0, 0),
            textColour = "black",
            #onSubmit = output,
            radius = 5,
            borderThickness = 3
        )

    def button(self, screen, text, positionx : int, positiony : int) :
        return Button(
            screen, # Surface to place button on
            positionx, # X-coordinate of top left corner
            positiony, # Y-coordinate of top left corner
            100, # Width
            80, # Height
            text = text,  # Text to display
            fontSize = 20,  # Size of font
            margin = 20,  # Minimum distance between text/image and edge of button
            inactiveColour = (200, 50, 0),  # Colour of button when not being interacted with
            hoverColour = (150, 0, 0),  # Colour of button when being hovered over
            # pressedColour=(0, 200, 20),  # Colour of button when being clicked
            radius = 20,  # Radius of border corners (leave empty for not curved)
            onClick =  lambda: Video() # Function to call when clicked on)
        )
