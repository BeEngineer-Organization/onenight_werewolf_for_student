import pygame

from common import *

# プレイヤーボタンの設定
PLAYER_BUTTON = Button(
    font_file=JAPANESE_FONT_FILE,
    font_size=FONT_SIZE_S,
    x=BUTTON_LEFT_X,
    y=BUTTON_Y,
    w=BUTTON_W,
    h=BUTTON_H,
)

# 墓地ボタンの設定
GRAVE_BUTTON = Button(
    font_file=JAPANESE_FONT_FILE,
    font_size=FONT_SIZE_S,
    x=BUTTON_RIGHT_X,
    y=BUTTON_Y,
    w=BUTTON_W,
    h=BUTTON_H,
)


def draw_fortune_teller_select_scene():
    # テキスト描画クラスの設定
    text_drawer = TextDrawer(JAPANESE_FONT_FILE)
    # タイトルテキストの描画
    text_drawer.draw_text_with_line_break(
        text="確認する役職を選んでください。",
        font_size=FONT_SIZE_M,
        x=TEXT_X,
        y=TEXT_Y,
        w=TEXT_W,
    )
    # 画像の描画
    SCREEN.blit(IMAGE_FORTUNE_TELLER_BIG, (IMAGE_X, IMAGE_Y))
    # ボタンの描画
    PLAYER_BUTTON.draw("プレイヤー")
    GRAVE_BUTTON.draw("墓地")


def update_fortune_teller_select_scene():
    pos = pygame.mouse.get_pos()
    scene = SCENE_FORTUNE_TELLER_SELECT
    if PLAYER_BUTTON.get_rect().collidepoint(pos):
        scene = SCENE_FORTUNE_TELLER
    elif GRAVE_BUTTON.get_rect().collidepoint(pos):
        scene = SCENE_FORTUNE_TELLER_ROLE
    return scene 
