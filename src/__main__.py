import sys
import pygame

def main():
    # Pygame initialisieren
    pygame.init()

    # Bildpfad und Laden
    image_path = "../assets/images/train.png"
    train_img = pygame.image.load(image_path)

    # Fenster erzeugen
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mein erstes Spiel")

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Hintergrund zeichnen
        screen.fill((30, 30, 30))

        # Zug zentriert darstellen
        rect = train_img.get_rect(center=(400, 300))
        screen.blit(train_img, rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
