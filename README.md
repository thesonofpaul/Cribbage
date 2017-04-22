# Cribbage

this is a simple command line based cribbage program.  you can play as player versus player, player against bot, or bot against bot.

How to Start

1.  cd into Cribbage main directory
2.  call 'python Game.py <choice> <choice>'
      parameters are for player type
      choices are bot or player
     
    ex. 'python Game.py player player'    'python Game.py bot player'      'python Game.py bot bot'

How to Play


      *****Discard*****
1.    Current player is shown along with current hand with indices
2.    Current player is asked to discard two cards one at a time
3.    Enter index of desired discard
4.    Next player discards
      *****Counting*****
5.    Current player shown current hand with indices
6.    Enter index of desired card
7.    Counter will increase until 31
8.    If player cannot play a card or plays invalid card, will be prompted to try again or not
9.    Enter: 'y' if card in hand can be played
             'n' if cannot play any cards
10.   Once played, card removed from hand
11.   Once all cards played, score for each hand and crib is calculated and score is displayed
12.   Repeat 1-11 until player reaches score of 121
