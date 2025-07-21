import pygame
import random

from common import *

from datetime import datetime

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
FORTUNE_TELLER_MAX = 9
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
    text_drawer = TextDrawer(JAPANESE_FONT_FILE)
    # 説明テキストの描画
    text_drawer.draw_text(
        text="役職の合計を（参加人数＋２）人にしてください。",
        font_size=FONT_SIZE_S,
        x=ROLE_X,
        y=DESCRIPTION_Y,
    )

    # 村人
    # 役職テキストの描画
    text_drawer.draw_text(
        text="村人",
        font_size=FONT_SIZE_M,
        x=ROLE_X,
        y=VILLAGER_Y,
    )
    # 画像表示
    SCREEN.blit(IMAGE_VILLAGER, (IMAGE_VILLAGER_X, VILLAGER_Y))
    # 役職説明テキストの描画
    text_drawer.draw_text_with_line_break(
        text="村人チームです。特に役割はありません。",
        font_size=FONT_SIZE_S,
        x=ROLE_DESCRIPTION_X,
        y=VILLAGER_Y,
        w=ROLE_DESCRIPTION_W,
    )
    # 村人減少ボタンの描画
    DECREASE_VILLAGER_BUTTON.draw("-")
    # 人数テキストの描画
    text_drawer.draw_text(
        text=str(villager_count),
        font_size=FONT_SIZE_M,
        x=ROLE_NUMBER_X,
        y=VILLAGER_Y,
    )
    # 村人増加ボタンの描画
    INCREASE_VILLAGER_BUTTON.draw("+")

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

    # スタートボタンの描画
    START_BUTTON.draw("スタート")


def update_village_scene(
    villager_count,
    fortune_teller_count,
    werewolf_count,
    players,
):
    scene = SCENE_VILLAGE
    pos = pygame.mouse.get_pos()

    if START_BUTTON.get_rect().collidepoint(pos):
        roles = []
        for _ in range(villager_count):
            roles.append("村人")
        for _ in range(fortune_teller_count):
            roles.append("占い師")
        for _ in range(werewolf_count):
            roles.append("人狼")

        scene = SCENE_PLAYER
        now = datetime.now()
        milliseconds = int(now.timestamp() * 1000)
        random.seed(milliseconds)
        random.shuffle(roles)

        for i in range(villager_count + fortune_teller_count + werewolf_count):
            if i < villager_count + fortune_teller_count + werewolf_count -2:
                name = f"プレイヤー{i + 1}"
            else:
                name = "墓地"
            players.append(
                {
                    "name":name,
                    "role":roles.pop(),
                    "villager_poll_count":0,
                    "poll_count":0,
                }
            )
        

    

    if START_BUTTON.get_rect().collidepoint(pos):
        pass

    elif INCREASE_VILLAGER_BUTTON.get_rect().collidepoint(pos):
        villager_count += 1
        if villager_count > VILLAGER_MAX:
            villager_count = VILLAGER_MAX

    elif DECREASE_VILLAGER_BUTTON.get_rect().collidepoint(pos):
        villager_count -= 1
        if villager_count < VILLAGER_MIN:
            villager_count = VILLAGER_MIN

    elif INCREASE_FORTUNE_TELLER_BUTTON.get_rect().collidepoint(pos):
        fortune_teller_count += 1
        if fortune_teller_count > FORTUNE_TELLER_MAX:
            fortune_teller_count = FORTUNE_TELLER_MAX

    elif DECREASE_FORTUNE_TELLER_BUTTON.get_rect().collidepoint(pos):
        fortune_teller_count -= 1
        if fortune_teller_count < FORTUNE_TELLER_MIN:
            fortune_teller_count = FORTUNE_TELLER_MIN

    elif INCREASE_WEREWOLF_BUTTON.get_rect().collidepoint(pos):
        werewolf_count += 1
        if werewolf_count > WEREWOLF_MAX:
            werewolf_count = WEREWOLF_MAX

    elif DECREASE_WEREWOLF_BUTTON.get_rect().collidepoint(pos):
        werewolf_count -= 1
        if werewolf_count < WEREWOLF_MIN:
            werewolf_count = WEREWOLF_MIN

    return (
        scene,
        villager_count,
        fortune_teller_count,
        werewolf_count,
        players,
    )