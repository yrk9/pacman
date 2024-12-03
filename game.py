import time
from player import Player
from enemy import Enemy
from food import Food
from block import Block
from field import Field
from config import Parameters
from user_input import UserInput
from random import randint
import random
import logging
import os

logger = logging.getLogger(__name__)


class Game:
    """Gameクラス (ゲームを実行する)

    Attributes:
        players (list[Player]): プレイヤー
        enemies (list[Enemy]): 敵のリスト
        foods (list[Food]): 食べ物のリスト
        field (Field): フィールドのインスタンス
    """

    def __init__(self, params: Parameters) -> None:
        """初期化

        Args:
            params (Parameters): configのパラメータのインスタンス
        """
        self.players: list[Player] = []
        self.enemys: list[Enemy] = []
        self.foods: list[Food] = []
        self.block: list[Block] = []
        self.field = Field([], [], [], [], 0)
        self.setup(params)
        self.start()

    def setup(self, params: Parameters) -> None:
        """初期設定を行う

        Args:
            param (Parameters): configのパラメータのインスタンス
        """
        enemy_icons = ["👹", "🐲", "👺"]
        f_size = params.field_size
        # フィールドの初期化
        self.players = [Player(1, 1, "😊")]
        self.enemys = [Enemy(randint(1, f_size - 2),
                             randint(1, f_size - 2),
                             random.choice(enemy_icons))]
        self.foods = [Food(4, 4)]
        self.blocks = [
            Block(x, y, "⛓️⛓️")
            for x in range(f_size)
            for y in range(f_size)
            if x == 0 or x == f_size - 1 or y == 0 or y == f_size - 1
        ]
        self.field = Field(self.players, self.enemys, self.foods,
                           self.blocks, f_size)

    def start(self) -> str:
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
            # プレイヤーと敵の移動
            for item in self.players + self.enemys:
                bumped_item = self.field.check_bump(item, list(self.blocks))
                if bumped_item is not None:
                    item.update_pos(stuck=True)
                else:
                    item.update_pos()

            for player in self.players:
                # 敵との衝突判定
                if self.field.check_bump(player, list(self.enemys)):
                    self.field.update_field()
                    os.system("cls" if os.name == "nt" else "clear")
                    # ターミナルをクリア
                    self.field.print_field()
                    logger.info("Game Over!")
                    return "Game Over!"

                # 食べ物との衝突判定
                bumped_item = self.field.check_bump(player, list(self.foods))
                if bumped_item is not None:
                    bumped_item.status = False
                    if all([not food.status for food in self.foods]):
                        self.field.update_field()
                        os.system("cls" if os.name == "nt" else "clear")
                        # ターミナルをクリア
                        self.field.print_field()
                        logger.info("Game Clear!")
                        return "Game Clear!"

            self.field.update_field()

            time.sleep(0.3)
