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


def draw_fortune_teller_role_scene(players, fortune_tell_index, is_grave):
    # テキスト描画クラスの設定
    text_drawer = TextDrawer(JAPANESE_FONT_FILE)
    # テキスト
    if is_grave == True:
        text = f"墓地に残された2つの役職は「{players[-2]['role']}」と「{players[-1]['role']}」です。"
    else:
        text = f"{players[fortune_tell_index]['name']}の役職は「{players[fortune_tell_index]['role']}」です。"
    # テキストの描画
    text_drawer.draw_text_with_line_break(
        text=text,
        font_size=FONT_SIZE_M,
        x=TEXT_X,
        y=TEXT_Y,
        w=TEXT_W,
    )
    # 画像の描画
    SCREEN.blit(IMAGE_FORTUNE_TELLER_BIG, (IMAGE_X, IMAGE_Y))
    # ボタンの描画
    BUTTON.draw("確認")


def update_fortune_teller_role_scene(player_index):
    # クリック位置を取得
    pos = pygame.mouse.get_pos()
    scene = SCENE_FORTUNE_TELLER_ROLE
    if BUTTON.get_rect().collidepoint(pos):
        # クリック位置がボタンの範囲内ならプレイヤーシーンに移動
        player_index += 1
        scene = SCENE_PLAYER
    return scene, player_index