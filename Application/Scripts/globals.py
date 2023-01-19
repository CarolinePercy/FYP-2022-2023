from enum import Enum


SCREEN_WIDTH = 1280

SCREEN_HEIGHT = 720

FPS = 60


class Item(Enum):

    WINE = 0

    CLOCK = 1

    LAPTOP = 2

    BOOKS = 3


g_itemTypes = [

    ["GlassOfWine.png", (25, 60),(510,360), "Glass Of Wine"],

    ["Clock.png", (50, 50),(397,155), "Clock"],

    ["Laptop.png", (200, 100),(200,600), "Laptop"],

    ["StackOfBooks.png", (80, 80),(820,430), "Stack of Books"]

    ]