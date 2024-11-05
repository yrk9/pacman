"""モジュールの説明
オブジェクトをフィールド上に描画する。

"""
from item import Item
from player import Player


class Field:
    """Fieldクラス
    Fieldクラスは、ゲームのフィールドを表すクラスです.
    プレイヤー、敵、アイテムの位置を更新し、Fieldを表示する機能を持ちます.
    位置を更新する際に衝突判定を行います.

    Attributes:
        players (list[Player]): プレイヤーのリスト
        field (list[list[str]]): フィールドの情報
        f_size (int): フィールドのサイズ
    """

    def __init__(
            self,
            players: list[Player],
            f_size: int = 6) -> None:
        """
        Fieldクラスの初期化を行う関数

        Args:
            players (list[Player]): プレイヤーのリスト
            f_size (int): フィールドのサイズ
        Example:
            p = [Player(1, 0, '😊')]
            f = Field(p, 3)
        """
        self.players = players
        self.f_size = f_size
        self.field = [["　" for _ in range(f_size)] for _ in range(f_size)]
        self.update_field()

    def print_field(self) -> None:
        """
        フィールドを描画する
        Args: なし
        Returns: なし
        Examples:
            >>> p=[Player(1, 0, '😊')]
            >>> p[0].icon = "p1"
            >>> field = Field(p, 3)
            >>> field.print_field()
        w: 上に移動
        a: 左に移動
        s: 下に移動
        d: 右に移動
        """
        print("w: 上に移動")
        print("a: 左に移動")
        print("s: 下に移動")
        print("d: 右に移動")

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
        for player in self.players:
            if player.status:
                self.field[player.now_y][player.now_x] = player.icon
        return self.field


if __name__ == "__main__":
    import doctest
    doctest.testmod()
