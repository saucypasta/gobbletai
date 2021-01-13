import config
from UCB import UCB_node

class Agent():
	def __init__(self,net,GameManager):
		self.temp = config.TURNS_UNTIL_TAU0

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

	def self_play_turn(self,games_per_epoch,mcts_per_game,mcts_batch_size):
		batch = []
		leaves = []
		mcts_rollouts_done = 0
		root_nodes = []

		init_state = GameManager.initialize_game()
		pred_v,pred_action = net.predict(init_state)
		for game in range(games_per_epoch):
			UCB = UCB_node(None,None,init_state,GameManager)
			UCB.expand(pred_v,pred_action)
			UCB.add_dirichlet_noise()
			root_nodes.append(UCB)

		while mcts_rollouts_done < mcts_per_game:
			for game in range(games_per_epoch):
				for _ in range(mcts_batch_size):
					leaf = root_nodes[game].select_leaf()
					batch.append(leaf.state)
					leaves.append(leaf)
				mcts_rollouts_done += mcts_batch_size
			batch = np.array(batch)
			preds = self.net.predict(batch)
			for i,leaf in enumerate(leaves):
				leaf.expand(preds[i][0],preds[i][1])

		return root_nodes






	def train_on_memories(self):
		pass