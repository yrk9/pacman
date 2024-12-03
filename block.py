from item import Item


class Block(Item):
    """ブロッククラス
    Itemを継承して作成したブロッククラス.
    ブロックの座標を管理
    移動はしない

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
            >>> block=(2,3,"⛓️")
        """
        super().__init__(x, y, icon)
        self.icon = icon


if __name__ == "__main__":
    import doctest
    doctest.testmod()
