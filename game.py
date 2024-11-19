import time
from player import Player
from enemy import Enemy
from food import Food
from field import Field
from config import Parameters
from user_input import UserInput
import os


class Game:
    """Gameクラス

    Attributes:
        players (list[Player]): プレイヤー
        field (Field): フィールド
    """

    def __init__(self, params: Parameters) -> None:
        """初期化

        Args:
            params (Parameters): configのパラメータのインスタンス
        """
        self.players = []
        self.enemys = []
        self.foods = []
        self.field = None
        self.setup(params)
        self.start()

    def setup(self, params: Parameters) -> None:
        """初期設定を行う

        Args:
            param (Parameters): configのパラメータのインスタンス
        """
        f_size = params.field_size
        # フィールドの初期化
        self.players = [Player(1, 1, "😊")]
        self.enemys = [Enemy(2, 3, "👹")]
        self.foods = [Food(4, 4)]
        self.field = Field(self.players, self.enemys, self.foods, f_size)

    def start(self) -> None:
        """ゲームのメインループ

        Returns:
            str: ゲーム終了時のメッセージ
        """
        # ゲームのメインループ
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            self.field.print_field()

            # プレイヤーの移動を決定
            for player in self.players:
                # キー入力を受け取る
                key = UserInput.get_user_input()
                player.get_next_pos(key)

            # 敵の移動を決定
            for enemy in self.enemys:
                enemy.get_next_pos()

            # プレイヤーの移動
            for item in self.players:
                item.update_pos(stuck=True)
          

            self.field.update_field()

            time.sleep(0.3)
