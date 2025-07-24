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


def draw_player_scene(player):
    text_drawer = TextDrawer(JAPANESE_FONT_FILE)
    # テキストの描画
    text_drawer.draw_text_with_line_break(
        text=f"{player['name']}にデバイスを渡してください。",
        font_size=FONT_SIZE_M,
        x=PLAYER_X,
        y=PLAYER_Y,
        w=PLAYER_W,
    )
    BUTTON.draw(f"{player['name']}です")


def update_player_scene():
    # クリック位置を取得
    pos = pygame.mouse.get_pos()
    scene = SCENE_PLAYER
    if BUTTON.get_rect().collidepoint(pos):
        # クリック位置がボタンの範囲内なら役職確認シーンに移動
        scene =  SCENE_ROLE
    return scene
