import pygame
import random

from common import *

# 説明テキストのY座標
DESCRIPTION_Y = SIDE // 24

# 役職テキストのX座標
ROLE_X = SIDE // 24
# 村人の画像のX座標
IMAGE_VILLAGER_X = SIDE // 24 * 5
# 占い師の画像のX座標
IMAGE_FORTUNE_TELLER_X = SIDE // 24 * 7
# 人狼の画像のX座標
IMAGE_WEREWOLF_X = SIDE // 24 * 5
# 役職説明テキストのX座標
ROLE_DESCRIPTION_X = SIDE // 24 * 9
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
    # ここに村人に関するコードを追加


    # 占い師
    # 役職テキストの描画
    text_drawer.draw_text(
        text="占い師",
        font_size=FONT_SIZE_M,
        x=ROLE_X,
        y=FORTUNE_TELLER_Y,
    )
    # 画像表示
    SCREEN.blit(IMAGE_FORTUNE_TELLER, (IMAGE_FORTUNE_TELLER_X, FORTUNE_TELLER_Y))
    # 役職説明テキストの描画
    text_drawer.draw_text_with_line_break(
        text="村人チームです。プレイヤー1人か墓地の2枚の役職がわかります。",
        font_size=FONT_SIZE_S,
        x=ROLE_DESCRIPTION_X,
        y=FORTUNE_TELLER_Y,
        w=ROLE_DESCRIPTION_W,
    )
    # 占い師減少ボタンの描画
    DECREASE_FORTUNE_TELLER_BUTTON.draw("-")
    # 人数テキストの描画
    text_drawer.draw_text(
        text=str(fortune_teller_count),
        font_size=FONT_SIZE_M,
        x=ROLE_NUMBER_X,
        y=FORTUNE_TELLER_Y,
    )
    # 占い師増加ボタンの描画
    INCREASE_FORTUNE_TELLER_BUTTON.draw("+")

    # 人狼
    # 役職テキストの描画
    text_drawer.draw_text(
        text="人狼",
        font_size=FONT_SIZE_M,
        x=ROLE_X,
        y=WEREWOLF_Y,
    )
    # 画像表示
    SCREEN.blit(IMAGE_WEREWOLF, (IMAGE_WEREWOLF_X, WEREWOLF_Y))
    # 役職説明テキストの描画
    text_drawer.draw_text_with_line_break(
        text="人狼チームです。村人チームには、自分が人狼だとバレないようにしましょう。",
        font_size=FONT_SIZE_S,
        x=ROLE_DESCRIPTION_X,
        y=WEREWOLF_Y,
        w=ROLE_DESCRIPTION_W,
    )
    # 人狼減少ボタンの描画
    DECREASE_WEREWOLF_BUTTON.draw("-")
    # 人数テキストの描画
    text_drawer.draw_text(
        text=str(werewolf_count),
        font_size=FONT_SIZE_M,
        x=ROLE_NUMBER_X,
        y=WEREWOLF_Y,
    )
    # 人狼増加ボタンの描画
    INCREASE_WEREWOLF_BUTTON.draw("+")

    # ここにスタートボタンに関するコードを追加


def update_village_scene(
    villager_count,
    fortune_teller_count,
    werewolf_count,
    players,
):
    # シーン
    scene = ""
    # クリック位置を取得
    pos = ""
    if START_BUTTON.get_rect().collidepoint(pos):
        # スタートボタンがクリックされたときの処理を書く場所
        pass

    elif INCREASE_VILLAGER_BUTTON.get_rect().collidepoint(pos):
        # 村人増加ボタンがクリックされたときの処理を書く場所
        pass

    elif DECREASE_VILLAGER_BUTTON.get_rect().collidepoint(pos):
        # 村人減少ボタンがクリックされたときの処理を書く場所
        pass

    elif INCREASE_FORTUNE_TELLER_BUTTON.get_rect().collidepoint(pos):
        # クリック位置が占い師増加ボタンの範囲内なら占い師数増加
        fortune_teller_count += 1
        # 占い師の最大人数
        if fortune_teller_count > FORTUNE_TELLER_MAX:
            fortune_teller_count = FORTUNE_TELLER_MAX

    elif DECREASE_FORTUNE_TELLER_BUTTON.get_rect().collidepoint(pos):
        # クリック位置が占い師減少ボタンの範囲内なら占い師数減少
        fortune_teller_count -= 1
        # 占い師の最小人数
        if fortune_teller_count < FORTUNE_TELLER_MIN:
            fortune_teller_count = FORTUNE_TELLER_MIN

    elif INCREASE_WEREWOLF_BUTTON.get_rect().collidepoint(pos):
        # クリック位置が人狼増加ボタンの範囲内なら人狼数増加
        werewolf_count += 1
        # 人狼の最大人数
        if werewolf_count > WEREWOLF_MAX:
            werewolf_count = WEREWOLF_MAX

    elif DECREASE_WEREWOLF_BUTTON.get_rect().collidepoint(pos):
        # クリック位置が人狼減少ボタンの範囲内なら人狼数減少
        werewolf_count -= 1
        # 人狼の最小人数
        if werewolf_count < WEREWOLF_MIN:
            werewolf_count = WEREWOLF_MIN

    return 