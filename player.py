from item import Item


class Player(Item):
    """プレイヤークラス
    Itemを継承して作成したプレイヤークラス.
    入力から移動方向を受け取って移動しようとする方向を計算するメソッドと

    Attributes:
        self.icon(str) : 表示されるアイテムのアイコン
        self.now_x(int) : 現在のx座標
        self.now_y(int) : 現在のy座標
        self.next_x(int) : 次の時刻でのx座標
        self.next_y(int) : 次の時刻でのy座標
        icon(str) : 表示されるアイテムのアイコン
    """

    def __init__(self, x: int, y: int, icon: str) -> None:
        """
        itemクラスを継承し、初期座標とアイコンを引数として受け取り定める

        Args:
            x:x座標
            y:y座標
            icon:アイコン(str型)

        Examples:
            >>> player=(2,3,"😊")
        """
        pass

    def get_next_pos(self, dir: tuple[int, int]) -> tuple[int, int]:
        """
        入力から移動方向を受け取って移動しようとする方向を計算して次の座標を返すメソッド
        引数にキー入力から受け取った次に移動したい方向をとり,
        現在のプレイヤーの座標から次に移動したい座標を戻り値として出力する.


        Args:
            dir (tuple[int, int]): キー入力から受け取った次に移動したい方向.
            (例:右に1マス移動したかったら(1,0)を受け取る)

        Returns:
            tuple[int, int]: 次に移動したい座標(例:入力が(1,0)で現在のプレイヤーの座標が
            (2,3)だった時,戻り値は(3,3))

        Examples:
            >>> player = Player(2, 3,"😊")
            >>> player.get_next_pos((1, 0))
            (3, 3)
            >>> player = Player(2, 3,"😊")
            >>> player.get_next_pos((0, 1))
            (2, 4)

        """
        self.next_x = self.now_x + dir[0]
        self.next_y = self.now_y + dir[1]
        return (self.next_x, self.next_y)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
