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
    # テキスト描画クラスの設定
    text_drawer = TextDrawer(JAPANESE_FONT_FILE)
    # 選択対象のプレイヤーの描画
    text_drawer.draw_text(
        text="プレイヤー",
        font_size=FONT_SIZE_M,
        x=SELECTED_PLAYER_X,
        y=SELECTED_PLAYER_Y,
    )
    # 減少ボタンの描画
    DECREASE_BUTTON.draw("-")
    # 人数テキストの描画
    text_drawer.draw_text(
        text=str(fortune_tell_index + 1),
        font_size=FONT_SIZE_M,
        x=PLAYER_NUMBER_X,
        y=SELECTED_PLAYER_Y,
    )
    # 増加ボタンの描画
    INCREASE_BUTTON.draw("+")
    # テキストの描画
    text_drawer.draw_text(
        text="の役職を確認する。",
        font_size=FONT_SIZE_M,
        x=SELECTED_PLAYER_X,
        y=ADDITIONAL_TEXT_Y,
    )
    # 画像の描画
    SCREEN.blit(IMAGE_FORTUNE_TELLER_BIG, (IMAGE_X, IMAGE_Y))
    # ボタンの描画
    SELECT_BUTTON.draw("決定")
    BACK_BUTTON.draw("戻る")


def update_fortune_teller_scene(fortune_tell_index, fortune_tell_index_max,is_grave):
    scene = SCENE_FORTUNE_TELLER
    pos = pygame.mouse.get_pos()
    if INCREASE_BUTTON.get_rect().collidepoint(pos):
        fortune_tell_index += 1
        if fortune_tell_index > fortune_tell_index_max:
            fortune_tell_index = fortune_tell_index_max

    elif DECREASE_BUTTON.get_rect().collidepoint(pos):
        fortune_tell_index -= 1
        if fortune_tell_index < 0:
            fortune_tell_index = 0
    
    elif SELECT_BUTTON.get_rect().collidepoint(pos):
        scene = SCENE_FORTUNE_TELLER_ROLE
        is_grave = False

    elif BACK_BUTTON.get_rect().collidepoint(pos):
        scene = SCENE_FORTUNE_TELLER_SELECT
    
    return (scene,fortune_tell_index,is_grave)
