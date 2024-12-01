import numpy as np
import re
from operator import countOf
fives = []
fours = []
fulls = []
threes = []
twos = []
ones = []
highs = []

card_ranks = {
    '2': 0,
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    'T': 8,
    'J': 9,
    'Q': 10,
    'K': 11,
    'A': 12
}

def sort_cards(card_list: list):
    ordered_cards = [] #ranked weakest to strongest
    num_cards = len(card_list)
    # if len(card_list) > 1:
    while len(card_list) > 0:
        weakest_card = card_list[0]
        for card in card_list:
            if weakest_card != card:
                weakest_card = get_weaker_hand(weakest_card, card)
        ordered_cards.append(weakest_card)
        card_list.remove(weakest_card)
    return ordered_cards


def get_type(hand):
    cards = re.findall(r'[A-Z2-9]', hand)
    unique_cards = np.unique(cards)
    occurences = {}
    for card in unique_cards:
        occurences[card] = countOf(cards, card)

    if( unique_cards.size == 1):
        fives.append(hand)
        return "five" #five of a kind
    elif (occurences[unique_cards[0]] == 4 or occurences[unique_cards[1]] == 4):
        fours.append(hand)
        return "four" #four of a kind
    elif (unique_cards.size == 2):
        if (occurences[unique_cards[0]] == 3 or occurences[unique_cards[1]] == 3):
            fulls.append(hand)
            return "full" #full house
    elif unique_cards.size == 3:
        if occurences[unique_cards[0]] == 3 or occurences[unique_cards[1]] == 3 or occurences[unique_cards[2]] == 3:
            threes.append(hand)
            return "three" #three of a kind
        elif {2, 2, 1} <= set(occurences.values()):
            twos.append(hand)
            return "two" #two pairs
    elif unique_cards.size == 4:
        if 2 in occurences.values():
            ones.append(hand)
            return "one" #one pair
    elif unique_cards.size == 5:
        highs.append(hand)
        return "high" #high card
    else:
        print("ERROR: ", hand)

    return cards

def get_weaker_hand(hand1, hand2):
    for idx in range(len(hand1)):
        if hand1[idx] == hand2[idx]:
            continue
        else:
            if card_ranks[hand1[idx]] < card_ranks[hand2[idx]]:
                return hand1
            else:
                return hand2
        
# def get_stronger_card(card1: str, card2: str):
#     if card1.isdigit() and card2.isdigit():
#         return max(card1, card2)

def get_value(hand):
    sum = 0
    for indx, card in enumerate(hand):
        sum += card_ranks[card] * pow(10, (10-indx))
    return sum

# def get_ranked_highs():
#     return_cards = []
#     highs.sort(get_value)
        


def part1():
    input = read_file()
    cards = input.read().splitlines()
    for idx in range(len(cards)):
        cards[idx] = cards[idx].split(' ')
    card_types = {}
    card_bids = {}
    for card in cards:
        card_types[card[0]] = get_type(card[0])
    for card in cards:
        card_bids[card[0]] = card[1]

    ordered_cards = [] #ranked weakest to strongest
    if len(highs) > 0:
        ordered_cards += sort_cards(highs)
    if len(ones) > 0:
        ordered_cards += sort_cards(ones)
    if len(twos) > 0:
        ordered_cards += sort_cards(twos)
    if len(threes) > 0:
        ordered_cards += sort_cards(threes)
    if len(fulls) > 0:
        ordered_cards += sort_cards(fulls)
    if len(fours) > 0:
        ordered_cards += sort_cards(fours)
    if len(fives) > 0:
        ordered_cards += sort_cards(fives)

    sum = 0
    for idx, card in enumerate(ordered_cards):
        # print("card: ", card, "type: ", card_types[card], "bid: ", card_bids[card], "idx: ", idx)
        sum += int(card_bids[card]) * (idx + 1)
    print(sum)
    # print("num of cards: ", len(cards))
    # print("num of cards in card types: ", len(card_types))
    # print("num of cards in card bids: ", len(card_bids))
    # print("ordered cards length: ", len(ordered_cards))

def get_type_part_two(hand):
    cards = re.findall(r'[A-Z2-9]', hand)
    unique_cards = np.unique(cards)
    occurences = {}
    j_occurences = countOf(cards, 'J')
    for card in unique_cards:
        if card != 'J':
            occurences[card] = countOf(cards, card)

    if( unique_cards.size == 1 or (unique_cards.size == 2 and j_occurences > 0)):
        fives.append(hand)
        return "five" #five of a kind
    elif (occurences[unique_cards[0]] == 4 or occurences[unique_cards[1]] == 4 or (occurences[unique_cards[0]] == 3 and j_occurences >= 1) or (occurences[unique_cards[1]] == 3 and j_occurences > 0)):
        fours.append(hand)
        return "four" #four of a kind
    elif (unique_cards.size == 2):
        if (occurences[unique_cards[0]] == 3 or occurences[unique_cards[1]] == 3):
            fulls.append(hand)
            return "full" #full house
    elif unique_cards.size == 3:
        if occurences[unique_cards[0]] == 3 or occurences[unique_cards[1]] == 3 or occurences[unique_cards[2]] == 3:
            threes.append(hand)
            return "three" #three of a kind
        elif {2, 2, 1} <= set(occurences.values()):
            twos.append(hand)
            return "two" #two pairs
    elif unique_cards.size == 4:
        if 2 in occurences.values():
            ones.append(hand)
            return "one" #one pair
    elif unique_cards.size == 5:
        highs.append(hand)
        return "high" #high card
    else:
        print("ERROR: ", hand)

    return cards
    
def part2():
    input = read_file()
    cards = input.read().splitlines()
    cards_without_j = input.read().replace()
    for idx in range(len(cards)):
        cards[idx] = cards[idx].split(' ')
    card_types = {}
    card_bids = {}
    for card in cards:
        card_types[card[0]] = get_type(card[0])
    for card in cards:
        card_bids[card[0]] = card[1]

    ordered_cards = [] #ranked weakest to strongest
    if len(highs) > 0:
        ordered_cards += sort_cards(highs)
    if len(ones) > 0:
        ordered_cards += sort_cards(ones)
    if len(twos) > 0:
        ordered_cards += sort_cards(twos)
    if len(threes) > 0:
        ordered_cards += sort_cards(threes)
    if len(fulls) > 0:
        ordered_cards += sort_cards(fulls)
    if len(fours) > 0:
        ordered_cards += sort_cards(fours)
    if len(fives) > 0:
        ordered_cards += sort_cards(fives)

    sum = 0
    for idx, card in enumerate(ordered_cards):
        # print("card: ", card, "type: ", card_types[card], "bid: ", card_bids[card], "idx: ", idx)
        sum += int(card_bids[card]) * (idx + 1)
    print(sum)

def read_file():
    input = open('input.txt', 'r')
    return input

print('Part1:')
part1()

print('Part2:')
part2()