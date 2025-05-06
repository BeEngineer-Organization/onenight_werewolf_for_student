import pygame
import random

from common import *

# 説明テキストのY座標
DESCRIPTION_Y = SIDE // 24

# 役職テキストのX座標
ROLE_X = SIDE // 24
# 役職説明テキストのX座標
ROLE_DESCRIPTION_X = SIDE // 24 * 8
# 役職説明テキストの幅
ROLE_DESCRIPTION_W = SIDE // 24 * 8
# 役職人数テキストのX座標
ROLE_NUMBER_X = SIDE // 24 * 19.5
# 村人のY座標
VILLAGER_Y = SIDE // 24 * 3
# 占い師のY座標
FORTUNE_TELLER_Y = SIDE // 24 * 7
# 人狼のY座標
WEREWOLF_Y = SIDE // 24 * 12

# 増加ボタンのX座標
INCREASE_BUTTON_X = SIDE // 24 * 22
# 減少ボタンのX座標
DECREASE_BUTTON_X = SIDE // 24 * 18
# 1段目の増減ボタンのY座標
INCREASE_OR_DECREASE_BUTTON_Y_1 = SIDE // 24 * 4
# 2段目の増減ボタンのY座標
INCREASE_OR_DECREASE_BUTTON_Y_2 = SIDE // 24 * 8
# 3段目の増減ボタンのY座標
INCREASE_OR_DECREASE_BUTTON_Y_3 = SIDE // 24 * 13

# 村人の最小人数
VILLAGER_MIN = 2
# 村人の最大人数
VILLAGER_MAX = 9
# 占い師の最小人数
FORTUNE_TELLER_MIN = 1
# 占い師の最大人数
FORTUNE_TELLER_MAX = 1
# 人狼の最小人数
WEREWOLF_MIN = 2
# 人狼の最大人数
WEREWOLF_MAX = 9

# 村人増加ボタンの設定
INCREASE_VILLAGER_BUTTON = Button(
    font_file=JAPANESE_FONT_FILE,
    font_size=FONT_SIZE_S,
    x=INCREASE_BUTTON_X,
    y=INCREASE_OR_DECREASE_BUTTON_Y_1,
    w=INCREASE_OR_DECREASE_BUTTON_SIDE,
    h=INCREASE_OR_DECREASE_BUTTON_SIDE,
)
# 村人減少ボタンの設定
DECREASE_VILLAGER_BUTTON = Button(
    font_file=JAPANESE_FONT_FILE,
    font_size=FONT_SIZE_S,
    x=DECREASE_BUTTON_X,
    y=INCREASE_OR_DECREASE_BUTTON_Y_1,
    w=INCREASE_OR_DECREASE_BUTTON_SIDE,
    h=INCREASE_OR_DECREASE_BUTTON_SIDE,
)
# 占い師増加ボタンの設定
INCREASE_FORTUNE_TELLER_BUTTON = Button(
    font_file=JAPANESE_FONT_FILE,
    font_size=FONT_SIZE_S,
    x=INCREASE_BUTTON_X,
    y=INCREASE_OR_DECREASE_BUTTON_Y_2,
    w=INCREASE_OR_DECREASE_BUTTON_SIDE,
    h=INCREASE_OR_DECREASE_BUTTON_SIDE,
)
# 占い師減少ボタンの設定
DECREASE_FORTUNE_TELLER_BUTTON = Button(
    font_file=JAPANESE_FONT_FILE,
    font_size=FONT_SIZE_S,
    x=DECREASE_BUTTON_X,
    y=INCREASE_OR_DECREASE_BUTTON_Y_2,
    w=INCREASE_OR_DECREASE_BUTTON_SIDE,
    h=INCREASE_OR_DECREASE_BUTTON_SIDE,
)
# 人狼増加ボタンの設定
INCREASE_WEREWOLF_BUTTON = Button(
    font_file=JAPANESE_FONT_FILE,
    font_size=FONT_SIZE_S,
    x=INCREASE_BUTTON_X,
    y=INCREASE_OR_DECREASE_BUTTON_Y_3,
    w=INCREASE_OR_DECREASE_BUTTON_SIDE,
    h=INCREASE_OR_DECREASE_BUTTON_SIDE,
)
# 人狼減少ボタンの設定
DECREASE_WEREWOLF_BUTTON = Button(
    font_file=JAPANESE_FONT_FILE,
    font_size=FONT_SIZE_S,
    x=DECREASE_BUTTON_X,
    y=INCREASE_OR_DECREASE_BUTTON_Y_3,
    w=INCREASE_OR_DECREASE_BUTTON_SIDE,
    h=INCREASE_OR_DECREASE_BUTTON_SIDE,
)
# スタートボタンの設定
START_BUTTON = Button(
    font_file=JAPANESE_FONT_FILE,
    font_size=FONT_SIZE_S,
    x=BUTTON_X,
    y=BUTTON_Y,
    w=BUTTON_W,
    h=BUTTON_H,
)


def draw_village_scene(
    villager_count,
    fortune_teller_count,
    werewolf_count,
):
    pass


def update_village_scene(
    villager_count,
    fortune_teller_count,
    werewolf_count,
    players,
):
    pass
