import time
from player import Player
from field import Field
from config import Parameters
import os


class Game:
    """Gameクラス
    
    Attributes:
        players (list[Player]): プレイヤー
        field (Field): フィールド
    """

    def __init__(self, params: Parameters) -> None:
        """初期化
        
        Args:
            params (Parameters): configのパラメータのインスタンス
        """
        pass

    def setup(self, params: Parameters) -> None:
        """初期設定を行う

        Args:
            param (Parameters): configのパラメータのインスタンス
        """

    def start(self) -> None:
        """ゲームのメインループ

        Returns:
            str: ゲーム終了時のメッセージ 
        """
        pass

