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
    villager_count = VILLAGER_DEFAULT

    fortune_teller_count = FORTUNE_TELLER_DEFAULT

    werewolf_count = WEREWOLF_DEFAULT

    players = []

    player_index = 0

    villager_poll_index = 0

    fortune_tell_index = 0

    is_grave = True

    most_suspicious_player = {}

    discuss_start_time = 0

    player_index_for_poll = 0

    poll_index = 0

    poll_result = []

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
            draw_title_scene()
        # 村シーン
        elif scene == SCENE_VILLAGE:
            draw_village_scene(
                villager_count=villager_count,
                fortune_teller_count=fortune_teller_count,
                werewolf_count=werewolf_count,
            )
        # プレイヤー確認シーン
        elif scene == SCENE_PLAYER:
            if player_index < len(players)-2:
                draw_player_scene(
                    player=players[player_index],
                )
            else:
                most_suspicious_player = max(
                    players,
                    key=lambda p: p["villager_poll_count"],
                )
                discuss_start_time = pygame.time.get_ticks()
                scene = SCENE_DISCUSS
        # 役職確認シーン
        elif scene == SCENE_ROLE:
            draw_role_scene(player=players[player_index])
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
            draw_fortune_teller_scene(fortune_tell_index)
        # 占い師役職シーン
        elif scene == SCENE_FORTUNE_TELLER_ROLE:
            if is_grave:
                draw_fortune_teller_role_scene(players)
            else:
                draw_fortune_teller_role_scene(players,fortune_tell_index)
        # 人狼シーン
        elif scene == SCENE_WEREWOLF:
            draw_werewolf_scene(players)
        # 議論シーン
        elif scene == SCENE_DISCUSS:
            scene = draw_discuss_scene(discuss_start_time,most_suspicious_player)
        # 投票用プレイヤーシーン
        elif scene == SCENE_PLAYER_FOR_POLL:
            if player_index_for_poll < len(players) -2:
                draw_player_for_poll_scene(
                    player=players[player_index_for_poll],
                )
            else:
                poll = sorted(
                    players[:-2],
                    key=lambda p:int(p["poll_count"]),
                    reverse=True
                )
                for i in range(len(poll)):
                    if i == 0 or poll[i - 1]["poll_count"] == poll[i]["poll_count"]:
                        poll_result.append(poll[i])
                        if poll[i]["role"] == "人狼":
                            werewolf_is_winner = False
                    else:
                        break
                
                if len(poll_result) == len(poll):
                    poll_result = ["平和村"]
                    for p in poll:
                        if p["role"] == "人狼":
                            werewolf_is_winner = True
                            break
                        else:
                            werewolf_is_winner = False

                scene = SCENE_PUNISHMENT
        # 投票シーン
        elif scene == SCENE_POLL:
            draw_poll_scene(poll_index,players[player_index_for_poll])
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
                    scene = update_title_scene()
                # 村シーン
                elif scene == SCENE_VILLAGE:
                    (
                        scene,
                        villager_count,
                        fortune_teller_count,
                        werewolf_count,
                        players,
                    ) = update_village_scene(
                        villager_count=villager_count,
                        fortune_teller_count=fortune_teller_count,
                        werewolf_count=werewolf_count,
                        players=players,
                    )
                # プレイヤー確認シーン
                elif scene == SCENE_PLAYER:
                    scene = update_player_scene()
                # 役職確認シーン
                elif scene == SCENE_ROLE:
                    scene = update_role_scene(
                        player=players[player_index]
                    )
                # 村人の投票シーン
                elif scene == SCENE_VILLAGER_POLL:
                    scene,villager_poll_index,player_index,players = (
                        update_villager_poll_scene(
                        player_index=player_index,
                        villager_poll_index=villager_poll_index,
                        villager_poll_index_max=players.index(players[-1])-2,
                        players=players,
                        )
                    )
                    
                # 占い師選択シーン
                elif scene == SCENE_FORTUNE_TELLER_SELECT:
                    scene = update_fortune_teller_select_scene()
                # 占い師シーン
                elif scene == SCENE_FORTUNE_TELLER:
                    scene,fortune_tell_index,is_grave = update_fortune_teller_scene(
                        fortune_tell_index=fortune_tell_index,
                        fortune_tell_index_max=players.index(players[-1])-2,
                        is_grave=is_grave,
                    )
                # 占い師役職シーン
                elif scene == SCENE_FORTUNE_TELLER_ROLE:
                    scene,player_index = update_fortune_teller_role_scene(player_index)
                # 人狼シーン
                elif scene == SCENE_WEREWOLF:
                    scene,player_index = update_werewolf_scene(player_index)
                # 議論シーン
                elif scene == SCENE_DISCUSS:
                    scene = update_discuss_scene()
                # 投票用プレイヤーシーン
                elif scene == SCENE_PLAYER_FOR_POLL:
                    poll_index = 0
                    scene  = update_player_for_poll_scene()
                # 投票シーン
                elif scene == SCENE_POLL:
                    scene,player_index_for_poll,poll_index,players = (
                        update_poll_scene(
                            player_index_for_poll=player_index_for_poll,
                            poll_index=poll_index,
                            poll_index_max=players.index(players[-1])-2,
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
