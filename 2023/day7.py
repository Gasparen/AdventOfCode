import pandas as pd
from itertools import groupby
from functools import total_ordering

# day7_testdata_2 taken from this reddit thread
# https://www.reddit.com/r/adventofcode/comments/18cr4xr/2023_day_7_better_example_input_not_a_spoiler/

def read_files():
    df = pd.read_csv(filepath_or_buffer='inputs\day7_indata.csv', delimiter=' ', header=None)
    return df

class Card:
    def transmute(self, value:str) -> int:
     if value=='A': return 14
     if value=='K': return 13
     if value=='Q': return 12
     if value=='J': return 11
     if value=='T': return 10
     return int(value)

    def __init__(self, card):
        self.card = card
        self.cardValue = self.transmute(card)

    def __repr__(self):
        return self.card

# Code taken from https://www.geeksforgeeks.org/python-group-list-elements-based-on-frequency/
def group_list(lst):
    return [(el, len(list(group))) for el, group in groupby(lst)]

@total_ordering
class CardHand:
    def __init__(self, cards, bid):
        self.bid = int(bid)
        self.cards = list(map(lambda c: Card(c), cards))
        s = ''
        for c in self.cards:
            s += c.card
        self.cardHandString = s
        cardValues = map(lambda c: c.cardValue, self.cards)
        cardValuesSorted = sorted(map(lambda c: c.cardValue, self.cards), reverse=True)
        groups = group_list(cardValuesSorted)
        self.sortedGroups = sorted(groups, key=lambda x: (x[1], x[0]), reverse=True)
        self.handRanking = self.determine_hand_ranking()
        [self.c1, self.c2, self.c3, self.c4, self.c5] = cardValues

    def determine_hand_ranking(self):
        (card_value_1, group_count_1) = self.sortedGroups[0]
        # Five of a kind
        if (group_count_1 == 5):
            return 7 + card_value_1
        (card_value_2, group_count_2) = self.sortedGroups[1]
        # Four of a kind
        if (group_count_1 == 4):
            return 6
        # Full House
        if (group_count_1 == 3 and group_count_2 == 2):
            return 5
        # Three of a kind
        (card_value_3, _) = self.sortedGroups[2]
        if (group_count_1 == 3):
            return 4
        # Two pair
        if (group_count_1 == 2 and group_count_2 == 2):
            return 3
        # One pair
        if (group_count_1 == 2):
            return 2
        return 1
    


    def __eq__(self, obj):
        if (self.handRanking == obj.handRanking and self.c1 == obj.c1 and self.c2 == obj.c2 and self.c3 == obj.c3 and self.c4 == obj.c4 and self.c5 == obj.c5):
            return True
        return False

    def __lt__(self, obj):
        if (self.handRanking < obj.handRanking): return True
        if (self.handRanking > obj.handRanking): return False
        # Same Ranking, sort by cards in order
        if(self.c1 < obj.c1): return True
        if(self.c1 > obj.c1): return False

        if(self.c2 < obj.c2): return True
        if(self.c2 > obj.c2): return False

        if(self.c3 < obj.c3): return True
        if(self.c3 > obj.c3): return False

        if(self.c4 < obj.c4): return True
        if(self.c4 > obj.c4): return False

        if(self.c5 < obj.c5): return True
        return False

    def __le__(self, obj):
        return (self == obj or self < obj)

    def __gt__(self, obj):
        return not(self <= obj)

    def __ge__(self, obj):
        return not(self < obj)

    def __repr__(self):
        return self.cardHandString
        

def main():
    df = read_files()
    df.columns = ['cardString', 'bid']
    df['cards'] = df['cardString'].map(lambda s: list(s))
    df['cardHands'] = df.apply(lambda row: CardHand(row['cards'], row['bid']),axis=1)
    df['sortedGroups'] = df['cardHands'].map(lambda l: l.sortedGroups)
    df['handRanking'] = df['cardHands'].map(lambda l: l.handRanking)
    df = df.sort_values(by='cardHands')
    df = df.reset_index()
    df['points'] = df.apply(lambda row: (row.name+1)*row['bid'],axis=1)


    print(df)
    print(df['points'].sum())

if __name__ == '__main__':
    main()