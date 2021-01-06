

class Abstract_Batch_Manager():
	def __init__(self,net):
		self.net = net


	def request_prediction(self,state):
		#does not batch right now
		return self.net.predict(state[0])