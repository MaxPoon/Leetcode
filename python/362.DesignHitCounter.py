class HitCounter(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.queue = [1]
		self.p1 = 0
		self.past5min = {1:0}
		self.p2 = 0
		self.numOfHits = {1:0}

	def hit(self, timestamp):
		"""
		Record a hit.
		@param timestamp - The current timestamp (in seconds granularity).
		:type timestamp: int
		:rtype: void
		"""
		if self.p1>=len(self.queue):
			self.queue.append(timestamp)
			self.past5min[timestamp] = 1
			self.numOfHits[timestamp] = 1
		
		elif self.queue[self.p2] == timestamp:
			lastTime = self.queue[self.p2]
			self.numOfHits[lastTime] += 1
			self.past5min[lastTime] += 1
		else:
			lastTime = self.queue[self.p2]
			self.past5min[timestamp] = self.past5min[lastTime] + 1
			self.numOfHits[timestamp] = 1
			self.queue.append(timestamp)
			while timestamp - self.queue[self.p1]>=300:
				self.past5min[timestamp] -= self.numOfHits[self.queue[self.p1]]
				self.p1 += 1
			self.p2+=1
			if self.p2<self.p1: self.p2 = self.p1
			

	def getHits(self, timestamp):
		"""
		Return the number of hits in the past 5 minutes.
		@param timestamp - The current timestamp (in seconds granularity).
		:type timestamp: int
		:rtype: int
		"""
		if self.p1>=len(self.queue): return 0
		lastTime = self.queue[self.p2]
		while  self.p1<len(self.queue) and timestamp - self.queue[self.p1]>=300 and self.p1<len(self.queue):
			self.past5min[lastTime] -= self.numOfHits[self.queue[self.p1]]
			self.p1+=1
		if self.p2<self.p1: self.p2 = self.p1
		return self.past5min[lastTime]
			
# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)