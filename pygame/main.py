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
    pygame.display.set_caption("ワンナイト人狼")
    # 初期シーンをタイトルに設定
    scene = SCENE_TITLE

    # プレイヤーのインデックス
    player_index = 0
    # 村人に怪しいと投票されるプレイヤーのインデックス
    villager_poll_index = 0

    # 占われるのが墓地か
    is_grave = False
    # 最も疑われているプレイヤー
    most_suspicious_player = []
    # 議論シーン開始時間
    discuss_start_time = 0


    # 投票結果
    poll_result = []
    # 人狼が勝者か
    werewolf_is_winner = True

    while True:
        # マップの描画
        if scene < SCENE_DISCUSS:
            # 画面を紺色に塗りつぶす
            SCREEN.fill(BLUE_STRONG)
            map_data = MAP_DATA_NIGHT
        else:
            # 画面を水色に塗りつぶす
            SCREEN.fill(BLUE_LIGHT)
            map_data = MAP_DATA_DAY
        map = Map(MAP_DICT, map_data, 32)
        map.draw()
        # 半透明なレイヤーを設置
        SCREEN.blit(LAYER, (0, 0))

        # タイトルシーン
        if scene == SCENE_TITLE:
            pass
        # 村シーン
        elif scene == SCENE_VILLAGE:
            pass
        # プレイヤー確認シーン
        elif scene == SCENE_PLAYER:
            if player_index < len(players) - 2:
                # 墓地にある役職2つ以外の場合
                draw_player_scene(
                    player=players[player_index],
                )
            else:
                # 村人から最も怪しまれているプレイヤーを選び出す
                villager_poll = sorted(
                    players[:-2],
                    key=lambda p: p["villager_poll_count"],
                    reverse=True
                )
                for i in range(len(villager_poll)):
                    if i == 0 or villager_poll[i - 1]["villager_poll_count"] == villager_poll[i]["villager_poll_count"]:
                        # 初項、または、1つ前の項と投票数が同じ場合、結果に追加
                        most_suspicious_player.append(villager_poll[i])
                    else:
                        # 投票数が同数ではないならそれよりあとは投票数が少ないプレイヤーなので、
                        # 確認する必要がない。
                        break
                # タイマーの開始時間をセット
                discuss_start_time = pygame.time.get_ticks()
                # プレイヤー全員が確認したら、議論シーンへ
                scene = SCENE_DISCUSS

        # 役職確認シーン
        elif scene == SCENE_ROLE:
            pass
        # 村人の投票シーン
        elif scene == SCENE_VILLAGER_POLL:
            draw_villager_poll_scene(
                villager_poll_index=villager_poll_index,
            )
        # 占い師選択シーン
        elif scene == SCENE_FORTUNE_TELLER_SELECT:
            draw_fortune_teller_select_scene()
        # 占い師シーン
        elif scene == SCENE_FORTUNE_TELLER:
            pass
        # 占い師役職シーン
        elif scene == SCENE_FORTUNE_TELLER_ROLE:
            draw_fortune_teller_role_scene(players, fortune_tell_index, is_grave)
        # 人狼シーン
        elif scene == SCENE_WEREWOLF:
            pass
        # 議論シーン
        elif scene == SCENE_DISCUSS:
            scene = draw_discuss_scene(discuss_start_time, most_suspicious_player)
        # 投票用プレイヤーシーン
        elif scene == SCENE_PLAYER_FOR_POLL:
            pass
        # 投票シーン
        elif scene == SCENE_POLL:
            draw_poll_scene(poll_index, players[player_index_for_poll])
        # 処刑シーン
        elif scene == SCENE_PUNISHMENT:
            draw_punishment_scene(poll_result)
        # 結果シーン
        elif scene == SCENE_RESULT:
            draw_result_scene(werewolf_is_winner)

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
                    scene = update_player_scene()
                # 役職確認シーン
                elif scene == SCENE_ROLE:
                    pass
                # 村人の投票シーン
                elif scene == SCENE_VILLAGER_POLL:
                    scene, player_index, villager_poll_index, players = (
                        update_villager_poll_scene(
                            player_index=player_index,
                            villager_poll_index=villager_poll_index,
                            villager_poll_index_max=players.index(players[-1]) - 2,  # 選べるのは墓地の2枚以外
                            players=players,
                        )
                    )
                # 占い師選択シーン
                elif scene == SCENE_FORTUNE_TELLER_SELECT:
                    scene, is_grave = update_fortune_teller_select_scene(is_grave)
                # 占い師シーン
                elif scene == SCENE_FORTUNE_TELLER:
                    pass
                # 占い師役職シーン
                elif scene == SCENE_FORTUNE_TELLER_ROLE:
                    scene, player_index = update_fortune_teller_role_scene(player_index)
                # 人狼シーン
                elif scene == SCENE_WEREWOLF:
                    pass
                # 議論シーン
                elif scene == SCENE_DISCUSS:
                    scene = update_discuss_scene()
                # 投票用プレイヤーシーン
                elif scene == SCENE_PLAYER_FOR_POLL:
                    pass
                # 投票シーン
                elif scene == SCENE_POLL:
                    scene, player_index_for_poll, poll_index, players = (
                        update_poll_scene(
                            player_index_for_poll=player_index_for_poll,
                            poll_index=poll_index,
                            poll_index_max=players.index(players[-1]) - 2,  # プレイヤーの人数は墓地の2つを除く
                            players=players,
                        )
                    )
                # 処刑シーン
                elif scene == SCENE_PUNISHMENT:
                    scene = update_punishment_scene()

        # 画面を更新
        pygame.display.update()


if __name__ == "__main__":
    main()
