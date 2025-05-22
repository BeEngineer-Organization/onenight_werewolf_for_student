import pygame

from common import *


BUTTON = Button(
    font_file=JAPANESE_FONT_FILE,
    font_size=FONT_SIZE_S,
    x=BUTTON_X,
    y=BUTTON_Y,
    w=BUTTON_W,
    h=BUTTON_H,
)


def draw_role_scene(player):
    text_drawer = TextDrawer(JAPANESE_FONT_FILE)
    # テキストの描画
    text_drawer.draw_text_with_line_break(
        text=f"{player['name']}の役職は「{player['role']}」です。",
        font_size=FONT_SIZE_M,
        x=PLAYER_X,
        y=PLAYER_Y,
        w=PLAYER_W,
    )
    # 画像の描画
    if player["role"] == "村人":
        image = IMAGE_VILLAGER_BIG
    elif player["role"] == "占い師":
        image = IMAGE_FORTUNE_TELLER_BIG
    elif player["role"] == "人狼":
        image = IMAGE_WEREWOLF_BIG
    SCREEN.blit(image, (IMAGE_X, IMAGE_Y))
    # ボタンの描画
    BUTTON.draw("確認")


def update_role_scene(player):
    pass
