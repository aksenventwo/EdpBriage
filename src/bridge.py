#-*- coding:utf-8 -*-

from deck import Deck
from player import Player

def circleList(ls, start):
    ls = ls[start:] + ls[:start]
    return ls

class Bridge(object):

    def __init__(self):

        #intialize the players
        self.players = {n: Player(n, n) for n in ['N', 'E', 'S', 'W']}

        #initialize the deck
        self.deck = Deck()

        self.playing = None

        #deal out the cards
        for rnd in range(13):
            for player in self.players:
                card = self.deck.deal()
                player.recv(card)

    def _get_winner(self, suit):
        if len(cards) != 4:
            raise ValueError("The calculated card should be 4.")
        # TODO(zou): calc who winn
        win_player = None
        for player in _get_players(self.playing.pos)
            if win_player is None:
                win_player = player
            win_player = self._compare(win_player, player, suit)
        return win_player

    def _compare(self, player_a, player_b, suit):
        # TODO(zou): Calculate the card size of two players
        pass


    def _get_players(self, start):
        if start == 'N':
            return [self.players['N'], self.players['E'], self.players['S'], self.players['W']]
        elif start == 'E':
            return [self.players['E'], self.players['S'], self.players['W'], self.players['N']]
        elif start == 'S':
            return [self.players['S'], self.players['W'], self.players['N'], self.players['E']]
        elif start == 'W':
            return [self.players['W'], self.players['N'], self.players['E'], self.players['S']]
        else:
            raise ValueError("Error start, %s" % start)

    def play(self):
        start = 'N'
        suit = None
        for rnd in range(13):
            players = _get_player(start)
            self.playing = players[0]
            for player in players:
                player.pick(suit)
                print('%s play: %s' % player.name, player.card())
        
            win_player = self._get_winner()
            start = win_player.pos
            suit = win_player.card.suit
           

if __name__=='__main__':
    bridge = Bridge()
    bridge.play()



