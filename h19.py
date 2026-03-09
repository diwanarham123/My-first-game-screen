import pygame
import os

def create_dummy_alpha_image(filename, size, color=(100, 100, 100), alpha=128):
    if not os.path.exists(filename):
        print(f"Creating dummy alpha image '{filename}'...")
        surf = pygame.Surface(size, pygame.SRCALPHA)
        surf.fill((color[0], color[1], color[2], alpha))
        pygame.image.save(surf, filename)

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
DISPLAY_SURFACE = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('My first game screen')

BACKGROUND_COLOR = (58, 58, 58)


main_image = pygame.transform.scale(
    pygame.image.load('penguin.png').convert_alpha(), (300, 300))
main_image_rect = main_image.get_rect(center=(SCREEN_WIDTH // 2,
    SCREEN_HEIGHT // 2))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        DISPLAY_SURFACE.fill(BACKGROUND_COLOR)

        
        DISPLAY_SURFACE.blit(main_image, main_image_rect)

        pygame.display.flip()

        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()