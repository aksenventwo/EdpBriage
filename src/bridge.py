#-*- coding:utf-8 -*-

from deck import Deck
from player import Player

def circleList(ls, start):
    ls = ls[start:] + ls[:start]
    return ls

class Bridge(object):

    def __init__(self):

        #intialize the players
        self.players = [Player(n) for n in ['N', 'E', 'S', 'W']]

        #initialize the deck
        self.deck = Deck()

        #deal out the cards
        for rnd in range(13):
            for player in self.players:
                card = self.deck.deal()
                player.recv(card)


    def check_trick(self, trick):
        win = trick[0]
        lead_suit = trick[0].suit

        for card in trick[1:]:
            print card.value, win.value
            if card.value > win.value:
                win = card
        return trick.index(win)

    def play(self):
        start = 0
        for rnd in range(13):
            suit = None
            trick = []
            #新的一轮都要更新出牌人
            for player in circleList(self.players, start):
                #出牌
                print '%s play:' % player.name
                card = player.pick(suit)
                trick.append(card)
                #if its the first player
                if suit is None:
                    suit = card.suit     #update the suit
            #赢的一方作为出牌人
            start = self.check_trick(trick)
            #统计玩家赢的墩数
            self.players[start].piers_num += 1

        for p in self.players:
            print p.piers_num

def main():
    bridge = Bridge()
    bridge.play()

if __name__=='__main__':
    main()



