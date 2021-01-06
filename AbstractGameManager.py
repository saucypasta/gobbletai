class Abstract_Game_Manager():
	def is_valid(self,state,action):
		pass

	def is_terminal(self,state):
		#returns True,w is state a terminal state
		#w = 1 if win, -1 if loss
		pass

	def take_action(self,curr_state,action):
		#returns the new state following the action taken from curr_state
		pass