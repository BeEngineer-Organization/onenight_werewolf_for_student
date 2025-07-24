import pygame

from common import *


# ボタンの設定
BUTTON = Button(
    font_file=JAPANESE_FONT_FILE,
    font_size=FONT_SIZE_S,
    x=BUTTON_X,
    y=BUTTON_Y,
    w=BUTTON_W,
    h=BUTTON_H,
)


def draw_punishment_scene(poll_result):
    pass


def update_punishment_scene():
    # クリック位置を取得
    pos = pygame.mouse.get_pos()
    scene = SCENE_PUNISHMENT
    if BUTTON.get_rect().collidepoint(pos):
        # クリック位置がボタンの範囲内なら結果シーンに移動
        scene = SCENE_RESULT
    return scene
