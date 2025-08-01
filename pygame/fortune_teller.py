import pygame

from common import *


# 増加ボタンの設定
INCREASE_BUTTON = Button(
    font_file=JAPANESE_FONT_FILE,
    font_size=FONT_SIZE_S,
    x=INCREASE_BUTTON_X,
    y=INCREASE_OR_DECREASE_BUTTON_Y,
    w=INCREASE_OR_DECREASE_BUTTON_SIDE,
    h=INCREASE_OR_DECREASE_BUTTON_SIDE,
)
# 減少ボタンの設定
DECREASE_BUTTON = Button(
    font_file=JAPANESE_FONT_FILE,
    font_size=FONT_SIZE_S,
    x=DECREASE_BUTTON_X,
    y=INCREASE_OR_DECREASE_BUTTON_Y,
    w=INCREASE_OR_DECREASE_BUTTON_SIDE,
    h=INCREASE_OR_DECREASE_BUTTON_SIDE,
)
# 決定ボタンの設定
SELECT_BUTTON = Button(
    font_file=JAPANESE_FONT_FILE,
    font_size=FONT_SIZE_S,
    x=BUTTON_LEFT_X,
    y=BUTTON_Y,
    w=BUTTON_W,
    h=BUTTON_H,
)

# 戻るボタンの設定
BACK_BUTTON = Button(
    font_file=JAPANESE_FONT_FILE,
    font_size=FONT_SIZE_S,
    x=BUTTON_RIGHT_X,
    y=BUTTON_Y,
    w=BUTTON_W,
    h=BUTTON_H,
)


def draw_fortune_teller_scene(fortune_tell_index):
    pass


def update_fortune_teller_scene(fortune_tell_index, fortune_tell_index_max):
    pass
