import pygame
import random

# Inicjalizacja Pygame
pygame.init()

# Ustalenie rozmiaru okna
szerokosc_okna = 800
wysokosc_okna = 600
okno_gry = pygame.display.set_mode((szerokosc_okna, wysokosc_okna))
pygame.display.set_caption("Stateczki z przeszkodą")

# Kolory
bialy = (255, 255, 255)
czarny = (0, 0, 0)
czerwony = (255, 0, 0)

tlo = pygame.transform.scale(pygame.image.load('tlo.png.jfif'), (szerokosc_okna, wysokosc_okna))
# Postać gracza
gracz_img = pygame.transform.scale(pygame.image.load("gracz.png.jfif"), (50, 50))
gracz_szerokosc = 50
gracz_wysokosc = 50
gracz_x = szerokosc_okna // 2 - gracz_szerokosc // 2
gracz_y = wysokosc_okna - gracz_wysokosc - 10
gracz_predkosc = 5

# Przeszkody
przeszkoda_img = pygame.transform.scale(pygame.image.load("kula.jfif"), (50, 50))
przeszkoda_szerokosc = 50
przeszkoda_wysokosc = 50
przeszkoda_x = random.randint(0, szerokosc_okna - przeszkoda_szerokosc)
przeszkoda_y = -50
przeszkoda_predkosc = 3

# Punktacja
punkty = 0
font = pygame.font.Font(None, 36)

# Główna pętla gry
gra_aktywna = True
clock = pygame.time.Clock()
while gra_aktywna:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gra_aktywna = False

    # Poruszanie się gracza
    klawisze = pygame.key.get_pressed()
    if klawisze[pygame.K_LEFT] and gracz_x > 0:
        gracz_x -= gracz_predkosc
    if klawisze[pygame.K_RIGHT] and gracz_x < szerokosc_okna - gracz_szerokosc:
        gracz_x += gracz_predkosc

    # Poruszanie się przeszkody
    przeszkoda_y += przeszkoda_predkosc
    if przeszkoda_y > wysokosc_okna:
        przeszkoda_x = random.randint(0, szerokosc_okna - przeszkoda_szerokosc)
        przeszkoda_y = -przeszkoda_wysokosc
        punkty += 1

    # Kolizja
    if gracz_x < przeszkoda_x + przeszkoda_szerokosc and \
            gracz_x + gracz_szerokosc > przeszkoda_x and \
            gracz_y < przeszkoda_y + przeszkoda_wysokosc and \
            gracz_y + gracz_wysokosc > przeszkoda_y:
        gra_aktywna = False

    # Wypełnienie tła
    okno_gry.blit(tlo, (0, 0))

    # Rysowanie gracza
    okno_gry.blit(gracz_img, (gracz_x, gracz_y))

    #    # Rysowanie przeszkody
    okno_gry.blit(przeszkoda_img, (przeszkoda_x, przeszkoda_y))

    # Wyświetlanie punktacji
    tekst_punkty = font.render("Punkty: " + str(punkty), True, czarny)
    okno_gry.blit(tekst_punkty, (10, 10))

    # Aktualizacja okna
    pygame.display.update()

    # Ograniczenie liczby klatek na sekundę
    clock.tick(60)

# Zakończenie Pygame
pygame.quit()
