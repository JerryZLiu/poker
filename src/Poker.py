from Player import Player
from Hand import Hand
from Deck import Deck
from Pot import Pot
from random import choice, randint

'''
Function used by both classes. Return the object of the next player to bid.
'''
def get_next_player(prev_player, players):


class Poker:

	# Sets up the game. Creates list of players and dealer. Sets starting money.
	def __init__(self):


	'''
	Initialize game by setting up player objects and dealing cards.
	'''
	def initialize(self):
		# generate players

	# Takes in id and returns the player object with that id
	def get_player_from_id(self, id_):

	'''
	Calculate which players have bankrupted and removes them from the list of players
	'''
	def remove_bankrupt_players(self):

	'''
	Calls the initialize function to set up the game and keeps running rounds until there's only one player left.
	Then we print out the winner!
	'''
	def play(self):


			

############################################################################


'''
A round ends when all 5 cards have been dealt and all hands scored.
'''
class Round:

	'''
	Initialize game information. Players assumed to sit by increasing player number clockwise.
	'''
	def __init__(self, game, players):


	'''
	Get order of players from the game.
	'''
	def set_player_order(self):


	'''
	Big and little blind are forced to make bids.
	Players are assumed to sit in number order clockwise.
	Play starts to the left of the dealer.
	(i.e., if 5 players are playing and player 2 is the dealer, player 1 = the small blind, player 5 = the big blind)
	'''
	def do_blinds(self):

	'''
	Cards are dealt to each player.
	'''
	def pre_flop(self):

	'''
	Conducts 1 round of betting until all players have checked or folded (aka pot is balanced).
	Takes in prev_player, the most recent player to have bid.
	'''
	def betting(self, pot_balanced):


	'''
	Deal 3 cards face-up from the deck and show to players.
	'''
	def flop(self):

	'''
	Flip over a new card and show it to players.
	'''
	def show_card(self):
	
	'''
	Returns players who have not folded in the round.
	'''
	@property
	def active_players(self):

	'''
	Remove player object from lists of players still in the round.
	'''
	def add_folded_player(self, player, remove_from_game = False):


	'''
	Check where or not there is a winner (i.e., just one player who has not folded)
	'''
	def winner(self): 


	'''
	Score players' hands and returns the winner.
	'''
	def score_player_hands(self):

    '''
    Prints out winner, gives money to winner and then prints out everyone's balance after the round ends.
    '''
	def give_out_winnings(self, winner):


	'''
    Runs through a whole round of poker play, blinds, betting, scoring hands and distributing winnings.
	'''
	def play(self):


#################################################################

game = Poker()
game.play()


