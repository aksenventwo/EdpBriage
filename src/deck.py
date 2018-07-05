#-*- coding:utf-8 -*-

from card import Card
from random import shuffle as std_shuffle


class Deck(object):
    """一副牌的集合，表示现实世界中一副牌的对象
    在桥牌里，一副牌由去掉大小鬼牌的52张牌组成
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = ['S', 'H', 'D', 'C']

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        self.shuffle()

    def shuffle(self):
        #洗牌
        std_shuffle(self._cards)

    def deal(self):
        #发牌
        return self._cards.pop()

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]
