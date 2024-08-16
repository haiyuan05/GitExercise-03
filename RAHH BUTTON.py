import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Random Moving Button")

# Set up button
button_image = pygame.image.load("Assets/button.png")  
button_width, button_height = button_image.get_width(), button_image.get_height()

button_rect = button_image.get_rect()
button_rect.x = random.randint(0, width - button_width)
button_rect.y = random.randint(0, height - button_height)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the button is clicked
            if button_rect.collidepoint(event.pos):
                button_rect.x = random.randint(0, width - button_width)
                button_rect.y = random.randint(0, height - button_height)

    # Draw background
    window.fill((255, 255, 255))  # White

    # Draw button
    window.blit(button_image, button_rect.topleft)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)