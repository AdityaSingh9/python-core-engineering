print('''
      
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
      |  \/ K|                            _/ |                
      '------'                           |__/           
      ''')

import random

def play_blackjack():
    # 1. Create the deck and card values
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    random.shuffle(cards)

    # 2. Deal initial cards
    player_hand = [cards.pop(), cards.pop()]
    dealer_hand = [cards.pop(), cards.pop()]

    def calculate_score(hand):
        score = sum(hand)
        # Handle Ace (11) becoming 1 if score > 21
        if score > 21 and 11 in hand:
            hand.remove(11)
            hand.append(1)
            return sum(hand)
        return score

    game_over = False

    # 3. Player's Turn
    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)
        
        print(f"\nYour cards: {player_hand}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        if player_score == 21:
            print("Blackjack! You win! 🃏")
            return
        elif player_score > 21:
            print("You went over. You lose! 💥")
            game_over = True
            break

        action = input("Type 'h' to Hit, 's' to Stand: ").lower()
        if action == 'h':
            player_hand.append(cards.pop())
        else:
            game_over = True

    # 4. Dealer's Turn (only if player didn't bust)
    if calculate_score(player_hand) <= 21:
        while calculate_score(dealer_hand) < 17:
            dealer_hand.append(cards.pop())

        player_final = calculate_score(player_hand)
        dealer_final = calculate_score(dealer_hand)

        print(f"\nYour final hand: {player_hand}, final score: {player_final}")
        print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_final}")

        if dealer_final > 21:
            print("Dealer busted! You win! 🏆")
        elif player_final > dealer_final:
            print("You win! 🏆")
        elif player_final < dealer_final:
            print("You lose! 📉")
        else:
            print("It's a draw! 🤝")

if __name__ == "__main__":
    print("--- Welcome to Simple Blackjack ---")
    play_blackjack()