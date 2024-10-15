"""アイテム
player,enemy,の親クラス
"""


class Item():
    """
    player,enemy,の親クラス
    Attributes:
       now_x(int) : 現在のx座標
       now_y(int) : 現在のy座標
       next_x(int) : 次の時刻でのx座標
       next_y(int) : 次の時刻でのy座標
       icon(str) : 表示されるアイテムのアイコン
    """

    def __init__(self, x, y) -> None:
        """
        各アイテムの初期設定
        初期座標(x,y)を受け取り座標を初期化する
        """
        pass
