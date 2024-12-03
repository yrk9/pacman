"""モジュールの説明
オブジェクトをフィールド上に描画する。

"""
from item import Item
from player import Player
from enemy import Enemy
from food import Food
from block import Block


class Field:
    """Fieldクラス
    Fieldクラスは、ゲームのフィールドを表すクラスです.
    プレイヤー、敵、アイテムの位置を更新し、Fieldを表示する機能を持ちます.
    位置を更新する際に衝突判定を行います.

    Attributes:
        players (list[Player]): プレイヤーのリスト
        enemys (list[Enemy]): 敵のリスト
        foods (list[Food]): 食べ物のリスト
        blocks (list[Block]): 障害物のリスト
        field (list[list[str]]): フィールドの情報
        f_size (int): フィールドのサイズ
    """

    def __init__(
            self,
            players: list[Player],
            enemys: list[Enemy],
            foods: list[Food],
            blocks: list[Block],
            f_size: int = 6) -> None:
        """
        Fieldクラスの初期化を行う関数

        Args:
            players (list[Player]): プレイヤーのリスト
            f_size (int): フィールドのサイズ
        Example:
            p = [Player(1, 0, '😊')]
            food = [Food(3, 3)]
            f = Field(p, food, 3)
        """
        self.players = players
        self.enemys = enemys
        self.foods = foods
        self.blocks = blocks
        self.f_size = f_size
        self.field = [["　" for _ in range(f_size)] for _ in range(f_size)]
        self.update_field()

    def print_field(self) -> None:
        """
        フィールドを描画する
        Args: なし
        Returns: なし
        Examples:
            >>> p = [Player(1, 0, "p1")]
            >>> food = [Food(3, 3)]
            >>> enemy = [Enemy(4, 4, "e1")]
            >>> block = [Block(5, 5)]
            >>> p[0].icon = "p1"
            >>> field = Field(p, food, enemy, block, 3)
            >>> field.print_field()
            キー配置
            ↖  ↑  ↗　Q W E
            ← 😊  →  A   D
            ↙  ↓  ↘　Z X C
        """
        print("キー配置")
        print("↖  ↑  ↗　Q W E")
        print("← " + self.players[0].icon + "  →  A   D")
        print("↙  ↓  ↘　Z X C")
        print("")

        # self.fieldを表示する処理を記述
        max_width = max(len(row) for row in self.field)  # フィールド内の最大幅を取得

        for row in self.field:
            # 各行の文字列を作成し、不足分を空白文字で埋める
            row_str = "".join(row)
            row_str = row_str.ljust(max_width)
            print(row_str)

    def update_field(self) -> list[list[str]]:
        """
        フィールドの情報を更新する
        Args: なし
        Returns: list[list[str]]: 更新されたField
        Examples:
            >>> p=[Player(1, 0, '😊')]
            >>> p[0].icon = "p1"
            >>> field = Field(p, 3)
            >>> field.update_field()
        """
        # fieldを一旦すべて空白にする
        for i in range(len(self.field)):
            for j in range(len(self.field[i])):
                self.field[i][j] = "　"
        #  Fieldを更新する処理を記述
        for enemy in self.enemys:
            if enemy.status:
                self.field[enemy.now_y][enemy.now_x] = enemy.icon
        for food in self.foods:
            if food.status:
                self.field[food.now_y][food.now_x] = food.icon
        for player in self.players:
            if player.status:
                self.field[player.now_y][player.now_x] = player.icon
        for block in self.blocks:
            if block.status:
                self.field[block.now_y][block.now_x] = block.icon
        return self.field

    def check_bump(
            self,
            target: Item,
            items: list[Item]) -> Item | None:
        """
        2つのアイテムの位置が重なっているか判定する関数

        Args:
            target (Item): アイテム1
            items (list[Item]): アイテムのリスト2

        Returns:
            Item | None: 重なっているアイテムがあればそのアイテム、なければNone

        Examples:
            >>> p = Item(0, 0)
            >>> e = Item(1, 1)
            >>> field = Field([p], [e], [], [])
            >>> p.next_x = 1
            >>> r = field.check_bump(p, [e])
            >>> r is None
            True
            >>> p.next_y = 1
            >>> r = field.check_bump(p, [e])
            >>> r is e
            True
        """
        # 衝突判定を行う処理を記述
        for item in items:
            if item.next_x == target.next_x and item.next_y == target.next_y:
                return item
            if item.now_x == target.now_x and item.now_y == target.now_y:
                return item
        return None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
