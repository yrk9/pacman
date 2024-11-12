from item import Item
import random


class Enemy(Item):
    """プレイヤークラス
    Itemを継承して作成したエネミークラス.
    ランダムで移動する

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
            >>> enemy=(2,3,"👹")
        """
        super().__init__(x, y, "👹")
        self.icon = "👹"

    def get_next_pos(self, dir: tuple[int, int]) -> tuple[int, int]:
        """
        ランダムで移動方向を決定し，移動しようとする方向を計算して次の座標を返すメソッド
        現在のエネミーの座標から次に移動したい座標を戻り値として出力する.


        Args:
            dir (tuple[int, int]): ランダムに決定された次に移動したい方向.
            (例:右に1マス移動したかったら(1,0)を受け取る)

        Returns:
            tuple[int, int]: 次に移動したい座標(例:入力が(1,0)で現在のエネミーの座標が
            (2,3)だった時,戻り値は(3,3))

        Examples:
            >>> enemy = Enemy(2, 3,"👹")
            >>> enemy.get_next_pos((1, 0))
            (3, 3)
            >>> enemy = Enemy(2, 3,"👹")
            >>> enemy.get_next_pos((0, 1))
            (2, 4)

        """
        # 上下左右に移動
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # directionの中からランダムで選択
        dir = random.choice(direction)
        self.next_x = self.now_x + dir[0]
        self.next_y = self.now_y + dir[1]
        return (self.next_x, self.next_y)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
