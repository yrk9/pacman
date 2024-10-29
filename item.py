"""アイテム
player,enemy,の親クラス
"""


class Item:
    """
    player,enemy,の親クラス
    Attributes:
       now_x(int) : 現在のx座標
       now_y(int) : 現在のy座標
       next_x(int) : 次の時刻でのx座標
       next_y(int) : 次の時刻でのy座標
       icon(str) : 表示されるアイテムのアイコン
    """

    def __init__(self, x: int, y: int, icon: str) -> None:
        """
        各アイテムの初期設定
        初期座標(x,y)を受け取り座標を初期化する
        Args:
            x:x座標
            y:y座標
            icon:アイコン(str型)

        Examples:
            >>> player=(2,3,"😊")
        """
        pass

    def get_pos(self) -> tuple[int, int]:
        """
        次の時刻における座標を取得するメソッド

        Returns:
            tuple[int, int]: 現在の座標

        Examples:
            >>> item = Item(2, 3,"😊")
            >>> item.get_pos()
            (2, 3)
        """

        pass

    def update_pos(self, stuck: bool = False) -> None:
        """
        座標を更新するメソッド
        引数に次に移動したい座標をとり,その座標にプレイヤーの現在座標を更新する.

        Args:
            stuck (bool): そのターンに動けない場合にTrueを渡す (default: False)

        Returns:
            None

        Examples:
            >>> item = Item(2, 3,"😊")
            >>> item.next_x = 3
            >>> item.next_y = 4
            >>> item.get_pos()
            (2, 3)
            >>> item.update_pos()
            >>> item.get_pos()
            (3, 4)

        """
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
