import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks] # 初始化牌组属性，包含52张牌

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position] #此特殊方法把操作委托给了[]运算符，使得我们可以通过下标来访问牌组中的牌
    