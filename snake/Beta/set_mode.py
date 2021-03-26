import pygame
from image import icon
from color import ORANGE,GRAY
# 전체화면 사이즈
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

# 메인화면 사이즈
MAIN_SURFACE_WIDTH = 1200
MAIN_SURFACE_HEIGHT = 700

# 픽셀 사이즈
PIXEL_SIZE = 20
PIXEL_WIDTH = MAIN_SURFACE_WIDTH / PIXEL_SIZE
PIXEL_HEIGHT = MAIN_SURFACE_HEIGHT / PIXEL_SIZE

# 색상코드

# 방향
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# 속도
FPS = 11
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

mainsurface = pygame.Surface((MAIN_SURFACE_WIDTH, MAIN_SURFACE_HEIGHT))
mainsurface = mainsurface.convert()
mainsurface.fill(GRAY)
# 화면 레이아웃 설정 => barsurface
# 상태 화면
barsurface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT - MAIN_SURFACE_HEIGHT))
barsurface = barsurface.convert()
barsurface.fill(ORANGE)

pygame.display.set_caption("Team While Succeed")
pygame.display.set_icon(icon)