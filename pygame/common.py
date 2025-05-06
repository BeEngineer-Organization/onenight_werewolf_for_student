import pygame


# 正方形の画面の1辺
SIDE = 512

# ウィンドウを初期化（画面サイズ SIDE * SIDE）
SCREEN = pygame.display.set_mode((SIDE, SIDE))

# 確定ボタンのX座標
BUTTON_X = SIDE // 24 * 12
# 確定ボタンのY座標
BUTTON_Y = SIDE // 24 * 20
# 確定ボタンの幅
BUTTON_W = SIDE // 24 * 9
# 確定ボタンの高さ
BUTTON_H = SIDE // 24 * 3

# 上のボタンのY座標
UPPER_BUTTON_Y = SIDE // 24 * 16

# テキストのX座標
TEXT_X = SIDE // 24 * 3
# テキストのY座標
TEXT_Y = SIDE // 24 * 7
# 長文テキストのY座標
LONG_TEXT_Y = SIDE // 24 * 4
# テキストの幅
TEXT_W = SIDE // 24 * 20

# 経過時間テキストのX座標
TIMEDELTA_TEXT_X = SIDE // 24 * 7
# 経過時間テキストのY座標
TIMEDELTA_TEXT_Y = SIDE // 24 * 15

# 選択対象のプレイヤーのX座標
SELECTED_PLAYER_X = SIDE // 24 * 4
# 選択対象のプレイヤーのY座標
SELECTED_PLAYER_Y = SIDE // 24 * 6
# 増加ボタンのX座標
INCREASE_BUTTON_X = SIDE // 24 * 19
# 減少ボタンのX座標
DECREASE_BUTTON_X = SIDE // 24 * 15
# 増減ボタンのY座標
INCREASE_OR_DECREASE_BUTTON_Y = SIDE // 24 * 7
# 選択対象のプレイヤーの数字テキストのX座標
PLAYER_NUMBER_X = SIDE // 24 * 16.5
# 追加テキストのY座標
ADDITIONAL_TEXT_Y = SIDE // 24 * 9

# 増減ボタンの1辺
INCREASE_OR_DECREASE_BUTTON_SIDE = SIDE // 24 * 2

# 日本語フォント
JAPANESE_FONT_FILE = "ipaexg.ttf"
# フォントサイズL
FONT_SIZE_L = 60
# フォントサイズM
FONT_SIZE_M = 40
# フォントサイズS
FONT_SIZE_S = 20

# プレイヤー確認テキストの座標
PLAYER_X = SIDE // 24 * 2
PLAYER_Y = SIDE // 24 * 8
PLAYER_W = SIDE // 24 * 22

# 黒
BLACK = (0, 0, 0)
# 白
WHITE = (255, 255, 255)

# タイトルシーン
SCENE_TITLE = 0
# 村シーン
SCENE_VILLAGE = 1
# プレイヤー確認シーン
SCENE_PLAYER = 2
# 役職確認シーン
SCENE_ROLE = 3
# 村人の投票シーン
SCENE_VILLAGER_POLL = 4
# 占い師選択シーン
SCENE_FORTUNE_TELLER_SELECT = 5
# 占い師シーン
SCENE_FORTUNE_TELLER = 6
# 占い師役職シーン
SCENE_FORTUNE_TELLER_ROLE = 7
# 人狼シーン
SCENE_WEREWOLF = 8
# 議論シーン
SCENE_DISCUSS = 9
# 投票用のプレイヤーシーン
SCENE_PLAYER_FOR_POLL = 10
# 投票シーン
SCENE_POLL = 11
# 処刑シーン
SCENE_PUNISHMENT = 12
# 結果シーン
SCENE_RESULT = 13


# テキスト描画クラス
class TextDrawer:
    def __init__(self, font_file):
        self.font_file = font_file

    # 改行なしのテキストを描画する関数
    def draw_text(self, text, font_size, x, y, color=WHITE):
        # 文字のフォントと大きさを設定
        font = pygame.font.Font(self.font_file, font_size)
        # テキストをサーフェスに変換
        text_surface = font.render(text, True, color)
        # 画面上に描画
        SCREEN.blit(text_surface, (x, y))

    # 改行ありのテキストを描画する関数
    def draw_text_with_line_break(self, text, font_size, x, y, w, color=WHITE):
        # 文字のフォントと大きさを設定
        font = pygame.font.Font(self.font_file, font_size)
        # 描画する位置
        blit_x = x
        blit_y = y
        # テキストから1文字ずつ取る
        for character in text:
            # 文字をサーフェスに変換
            character_surface = font.render(character, True, color)
            # 指定された幅からはみ出したら、1段下げて左から描画する
            if blit_x + character_surface.get_rect().w >= x + w:
                blit_x = x
                blit_y += character_surface.get_rect().h
            # 画面上に描画
            SCREEN.blit(character_surface, (blit_x, blit_y))
            # 描画した文字の幅だけ、描画開始点が右にずれる
            blit_x += character_surface.get_rect().w


# ボタンクラス
class Button:
    def __init__(
        self,
        font_file,
        font_size,
        x,
        y,
        w,
        h,
        color=BLACK,
        bg_color=WHITE,
    ):
        self.font_file = font_file
        self.font_size = font_size
        # 描画の基準点は中央
        self.x = x - w // 2
        self.y = y - h // 2
        self.w = w
        self.h = h
        self.color = color
        self.bg_color = bg_color

    def draw(self, text):
        # 文字のフォントと大きさを設定
        font = pygame.font.Font(self.font_file, self.font_size)
        # ボタンの四角形部分
        button_rect = self.get_rect()
        # テキストをサーフェスに変換
        button_text_surface = font.render(text, True, self.color)
        # 中央揃えにする
        button_text_rect = button_text_surface.get_rect(
            center=(self.x + self.w // 2, self.y + self.h // 2)
        )
        # 画面上に描画
        pygame.draw.rect(SCREEN, self.bg_color, button_rect)
        SCREEN.blit(button_text_surface, button_text_rect)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)
