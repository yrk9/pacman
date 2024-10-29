"""モジュールの説明
オブジェクトをフィールド上に描画する。

"""

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
        pass

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

        """
        pass

    def update_field(self) -> None:
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
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
