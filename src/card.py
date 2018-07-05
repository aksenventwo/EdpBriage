#-*- coding:utf-8 -*-

#扑克牌对象，抽象出牌这种结构。
#它可以表示一张牌
import logging
from .errors import (CardAppendError, CardSpilloverError,
                    CardRankError, CardSuitError)


class Card(object):
    """扑克牌类，表示现实世界中一张扑克牌对象
    :rank str 扑克牌的值 (2~10AKQJ)
    :suit str 扑克牌的花色 (黑桃、红心、方块、草花)
    """
    rank_val = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def __init__(self, rank, suit):
        self._logger = logging.getLogger('EdpBriage.Card')
        self.rank = self.check_rank(rank)
        self.suit = self.check_suit(suit)

    @property
    def value(self):
        #目前是无将打法，计算牌的大小没有将牌
        val = self.rank_val.get(self.rank)
        if val is None:
            return int(self.rank)
        return val

    def check_rank(self, rank):
        if rank not in '2 3 4 5 6 7 8 9 10 J Q K A'.split(' '):
            self._logger.error('The value of the card should be in the range of \
                                "2 3 4 5 6 7 8 9 10 J Q K A".')
            raise CardRankError
        return rank

    def check_suit(self, suit):
        if suit not in 'S H D C'.split(' '):
            raise CardSuitError
        return suit

    def __str__(self):
        return 'Card(rank="%s", suit="%s")' % (self.rank, self.suit)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.rank == other.rank \
            and self.suit == other.suit:
            return True
        return False


class Hand(object):
    """表示玩家手里的牌
    它包括出牌，给牌排序，计算牌的点数等功能
    """
    def __init__(self):
        self._cards = []

    def append(self, card):
        if not isinstance(card, Card):
            raise CardAppendError
        if len(self) >= 13:
            raise CardSpilloverError
        self._cards.append(card)

    def clear(self):
        self._cards = []

    def __str__(self):
        card_str = ''
        for card in self._cards:
            card_str += '%s%s ' % (card.suit, card.rank)
        return card_str

    def __len__(self):
        return len(self._cards)

    def __contains__(self, card):
        return any(c == card for c in self._cards)
