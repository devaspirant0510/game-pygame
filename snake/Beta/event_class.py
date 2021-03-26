import pygame
class Button(object):
    # 위치 크기 생성
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    # 마우스 좌표값 불러와서 생성한 버튼내에 마우스좌표가 들어가있는지 판단
    def isover(self, p):
        if self.x < p[0] and p[0] < self.x + self.w:
            if self.y < p[1] and p[1] < self.y + self.h:
                # 마우스 좌표가 버튼 범위 내에 들어있으면 True 리턴
                return True

def nexon_free_font(var_m, var_a, txt_color, txt_size, po, su):
    font = pygame.font.Font("font/Maplestory Bold.ttf", txt_size)
    text = font.render(var_m + str(var_a), 1, txt_color)
    pos = text.get_rect()
    su.blit(text, (po[0], po[1]))

def namu_free_font(var_m, var_a, txt_color, txt_size, po, su):
    font = pygame.font.Font("font/NanumPen.ttf", txt_size)
    text = font.render(var_m + str(var_a), 1, txt_color)
    pos = text.get_rect()
    su.blit(text, (po[0], po[1]))
