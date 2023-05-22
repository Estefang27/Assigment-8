#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

class HumanPlayer:
    def __init__(self):
        self.score = 0
        
    def turn(self, current_score, roll):
        print(f"Your current score is {self.score}.")
        print(f"You rolled a {roll}.")
        
        while True:
            action = input("Do you want to roll or hold? ")
            
            if action.lower() == 'roll':
                return 'roll'
            elif action.lower() == 'hold':
                return 'hold'
            else:
                print("Invalid input. Please enter 'roll' or 'hold'.")

class ComputerPlayer:
    def __init__(self):
        self.score = 0
        
    def turn(self, current_score, roll):
        if self.score < min(25, 100 - self.score):
            return 'roll'
        else:
            return 'hold'

class PlayerFactory:
    def create_player(self, player_type):
        if player_type.lower() == 'human':
            return HumanPlayer()
        elif player_type.lower() == 'computer':
            return ComputerPlayer()

class Game:
    def __init__(self, player1_type, player2_type):
        self.player_factory = PlayerFactory()
        self.player1 = self.player_factory.create_player(player1_type)
        self.player2 = self.player_factory.create_player(player2_type)
        self.current_player = self.player1
        self.current_score = 0
        
    def roll_dice(self):
        roll = random.randint(1, 6)
        if roll == 1:
            self.current_score = 0
            print(f"You rolled a {roll}. Your turn is over.")
        else:
            print(f"You rolled a {roll}.")
        return roll

    def play(self):
        while True:
            action = self.current_player.turn(self.current_score, self.roll_dice())
            
            if action == 'roll':
                self.current_score += self.roll_dice()
                
                if self.current_player.score + self.current_score >= 100:
                    self.current_player.score += self.current_score
                    print(f"{self.current_player.__class__.__name__} wins with a score of {self.current_player.score}!")
                    break
                
            elif action == 'hold':
                self.current_player.score += self.current_score
                
                if self.current_player.score >= 100:
                    print(f"{self.current_player.__class__.__name__} wins with a score of {self.current_player.score}!")
                    break
                
            self.current_player = self.player1 if self.current_player == self.player2 else self.player2

import time

class TimedGameProxy:
    def __init__(self, player1_type, player2_type, time_limit):
        self.game = Game(player1_type, player2_type)
        self.time_limit = time_limit
        self.start_time = time.time()
    
    def play(self):
        while True:
            if time.time() - self.start_time > self.time_limit:
                winner = self.game.player1 if self.game.player1

