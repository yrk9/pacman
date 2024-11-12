from item import Item


class Food(Item):
    """
    Foodクラス
    達成条件の食べ物
    Attributes:
    self.x(int) : 食べ物のx座標
    self.y(int) : 食べ物のy座標
    """

    def __init__(self, x: int, y: int) -> None:
        """
        Args:
            x:x座標
            y:y座標
            icon:アイコン(str型)

        Examples:
            >>> food = Food(3, 3)
        """

        super().__init__(x, y, "🍜")
        self.icon = "🍜"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
