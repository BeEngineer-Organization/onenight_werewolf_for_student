import pygame
import sys
import random

from common import *
from title import draw_title_scene, update_title_scene
from village import draw_village_scene, update_village_scene
from player import draw_player_scene, update_player_scene
from role import draw_role_scene, update_role_scene
from villager_poll import draw_villager_poll_scene, update_villager_poll_scene
from fortune_teller_select import (
    draw_fortune_teller_select_scene,
    update_fortune_teller_select_scene,
)
from fortune_teller import draw_fortune_teller_scene, update_fortune_teller_scene
from fortune_teller_role import (
    draw_fortune_teller_role_scene,
    update_fortune_teller_role_scene,
)
from werewolf import draw_werewolf_scene, update_werewolf_scene
from dicuss import draw_discuss_scene, update_discuss_scene
from player_for_poll import draw_player_for_poll_scene, update_player_for_poll_scene
from poll import draw_poll_scene, update_poll_scene
from punishment import draw_punishment_scene, update_punishment_scene
from result import draw_result_scene

# 村人の初期人数
VILLAGER_DEFAULT = 2
# 占い師の初期人数
FORTUNE_TELLER_DEFAULT = 1
# 人狼の初期人数
WEREWOLF_DEFAULT = 2


def main():
    # Pygameを初期化
    pygame.init()
    # ウィンドウのタイトルを設定
    pygame.display.set_caption("人狼ゲーム")
    # 初期シーンをタイトルに設定
    scene = SCENE_TITLE

    while True:
        # 画面を黒色に塗りつぶす
        SCREEN.fill(BLACK)

        # タイトルシーン
        if scene == SCENE_TITLE:
            pass
        # 村シーン
        elif scene == SCENE_VILLAGE:
            pass
        # プレイヤー確認シーン
        elif scene == SCENE_PLAYER:
            pass
        # 役職確認シーン
        elif scene == SCENE_ROLE:
            pass
        # 村人の投票シーン
        elif scene == SCENE_VILLAGER_POLL:
            pass
        # 占い師選択シーン
        elif scene == SCENE_FORTUNE_TELLER_SELECT:
            pass
        # 占い師シーン
        elif scene == SCENE_FORTUNE_TELLER:
            pass
        # 占い師役職シーン
        elif scene == SCENE_FORTUNE_TELLER_ROLE:
            pass
        # 人狼シーン
        elif scene == SCENE_WEREWOLF:
            pass
        # 議論シーン
        elif scene == SCENE_DISCUSS:
            pass
        # 投票用プレイヤーシーン
        elif scene == SCENE_PLAYER_FOR_POLL:
            pass
        # 投票シーン
        elif scene == SCENE_POLL:
            pass
        # 処刑シーン
        elif scene == SCENE_PUNISHMENT:
            pass
        # 結果シーン
        elif scene == SCENE_RESULT:
            pass

        # イベント処理
        for event in pygame.event.get():
            # 閉じるボタンが押されたら終了
            if event.type == pygame.QUIT:
                pygame.quit()  # Pygameを終了
                sys.exit()
            # クリックされた場合
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # タイトルシーン
                if scene == SCENE_TITLE:
                    pass
                # 村シーン
                elif scene == SCENE_VILLAGE:
                    pass
                # プレイヤー確認シーン
                elif scene == SCENE_PLAYER:
                    pass
                # 役職確認シーン
                elif scene == SCENE_ROLE:
                    pass
                # 村人の投票シーン
                elif scene == SCENE_VILLAGER_POLL:
                    pass
                # 占い師選択シーン
                elif scene == SCENE_FORTUNE_TELLER_SELECT:
                    pass
                # 占い師シーン
                elif scene == SCENE_FORTUNE_TELLER:
                    pass
                # 占い師役職シーン
                elif scene == SCENE_FORTUNE_TELLER_ROLE:
                    pass
                # 人狼シーン
                elif scene == SCENE_WEREWOLF:
                    pass
                # 議論シーン
                elif scene == SCENE_DISCUSS:
                    pass
                # 投票用プレイヤーシーン
                elif scene == SCENE_PLAYER_FOR_POLL:
                    pass
                # 投票シーン
                elif scene == SCENE_POLL:
                    pass
                # 処刑シーン
                elif scene == SCENE_PUNISHMENT:
                    pass

        # 画面を更新
        pygame.display.update()


if __name__ == "__main__":
    main()
