import numpy as np
import config

class Abstract_UCB_Node():

	def __init__(self,parent,parent_action_idx,state,BatchManager,GameManager,turns_until_tau):
		self.parent = parent  #parent node
		self.parent_action_idx = parent_action_idx #index of parent action
		self.state = state

		self.GameManager = GameManager #follows AbstractGameManager class
		self.BatchManager = BatchManager #follows AbstractBatchManager class

		self.action_size = config.ACTION_SIZE
		self.c_puct = config.CPUCT
		self.turns_until_tau = turns_until_tau
		self.epsilon = config.EPSILON
		self.alpha = config.ALPHA 

		self.N_s = 1 #total states explored (plus one)
		self.N_s_a = np.zeros(action_size) #num nodes explored stemming from each state,action pair

		self.children = [None for _ in range(self.action_size)]

		#Q = sum of values predicted by net of all nodes stemming from self
		self.Q = np.zeros(action_size)

		self.pred_v,self.pred_action = self.request_prediction(state,BatchManager)

		self.fix_actions(GameManager)
		self.add_dirichlet_noise()

		self.backup()

	def add_dirichlet_noise(self):
		#adds dirichlet noise only if UCB_Node is root node
		if self.parent == None:
			pass #add noise to parent


	def fix_actions(self):
		#set probability of illegal actions to zero
		pass

	def act(self):
		#calculate UCB and determine best action
		#if never taken
			#initialize child node corresponding to best action
			#set self.children[action_idx] to child
		#else
			#child.act()
		pass

	def backup(self):
		# recursively adds self.pred_v to parent.Q[self.parent_action_idx] until root is reached
			#negative for opposite team
		pass

	def terminal_node(self):
		#returns True,w is state a terminal state
		#w = 1 if win, -1 if loss
		return self.GameManager.is_terminal()

	def valid_action(self,action_idx):
		return self.GameManager.valid_action(self.state,action_idx)

	def calculate_U(self):
		return self.c_puct*self.pred_action*np.sqrt(self.N_s)/(self.N_s_a+np.ones(action_size))

	def calculate_Q(self):
		#average predicted value
		return np.nan_to_num(self.Q/self.N_s_a)

	def calculate_Z(self):
		#average terminal state value
		t,w = self.terminal_node()
		if t:
			return w
		return np.nan_to_num(self.Z/self.N_s_a_t)

	def calculate_UCB(self):
		return self.calculate_Q() + self.calculate_U()

	def request_prediction(self,state,BatchManager):
		#call some manager that waits for many requests before doing batch prediction
		pred_v,pred_action = BatchManager.request_prediction(state)

		return pred_v, pred_action
		