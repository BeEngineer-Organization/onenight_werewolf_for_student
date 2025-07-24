import pygame

from common import *

# 何秒間待機するか
SECOND = 120

# ボタンの設定
BUTTON = Button(
    font_file=JAPANESE_FONT_FILE,
    font_size=FONT_SIZE_S,
    x=BUTTON_X,
    y=BUTTON_Y,
    w=BUTTON_W,
    h=BUTTON_H,
)


def draw_discuss_scene(discuss_start_time, most_suspicious_player):
    # テキスト描画クラスの設定
    text_drawer = TextDrawer(JAPANESE_FONT_FILE)

    # タイトルテキストの描画
    text = "誰が人狼か明らかにするための議論を開始してください。村人から最も怪しまれているのは"
    for player in most_suspicious_player:
        text += f"「{player['name']}」"
    text += "です。"
    text_drawer.draw_text_with_line_break(
        text=text,
        font_size=FONT_SIZE_M,
        x=TEXT_X,
        y=LONG_TEXT_Y,
        w=TEXT_W,
    )

    # 経過時間テキストの描画
    timedelta = pygame.time.get_ticks() - discuss_start_time
    text_drawer.draw_text(
        text=f"{SECOND - timedelta // 1000}秒後に画面移動します。",
        font_size=FONT_SIZE_S,
        x=TIMEDELTA_TEXT_X,
        y=TIMEDELTA_TEXT_Y,
    )
    # ボタンの描画
    BUTTON.draw("投票へ")

    scene = SCENE_DISCUSS
    if timedelta > SECOND * 1000:
        # SECOND * 1000ミリ秒経過で、投票用プレイヤーシーンに移動
        scene = SCENE_PLAYER_FOR_POLL
    return scene


def update_discuss_scene():
    # クリック位置を取得
    pos = pygame.mouse.get_pos()
    scene = SCENE_DISCUSS
    if BUTTON.get_rect().collidepoint(pos):
        # クリック位置がボタンの範囲内なら投票用プレイヤーシーンに移動
        scene = SCENE_PLAYER_FOR_POLL
    return scene
