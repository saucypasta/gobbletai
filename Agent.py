import config

class Agent():
	def __init__(self,net,GameManager):
		self.temp = config.TURNS_UNTIL_TAU0
		self.cpuct = config.CPUCT 
		self.epsilon = config.EPSILON 
		self.alpha = config.ALPHA 

		self.training_epochs = config.EPOCHS 
		self.mini_batch_size = config.BATCH_SIZE 

		#memory buffer params
		self.window_low = config.WINDOW_LOW
		self.window_high = config.WINDOW_HIGH 
		self.window = self.window_low
		self.mem = []

		self.net = net
		self.GameManager = GameManager

	def play_optimally(self,state):
		pass

	def self_play(self,games_per_epoch,mcts_per_game):
		pass

	def train_on_memories(self):
		pass