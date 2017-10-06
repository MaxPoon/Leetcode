from collections import deque
class SnakeGame(object):

	def __init__(self, width,height,food):
		"""
		Initialize your data structure here.
		@param width - screen width
		@param height - screen height 
		@param food - A list of food positions
		E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
		:type width: int
		:type height: int
		:type food: List[List[int]]
		"""
		self.head = (0,0)
		self.width = width
		self.height = height
		self.directions = {'U': (-1,0), 'L':(0,-1), 'R': (0,1), 'D':(1,0)}
		self.score = 0
		self.foods = food
		self.i = 0
		self.body = deque()
		self.body.append((0,0))
		self.blocks = set([(0,0)])

	def move(self, direction):
		"""
		Moves the snake.
		@param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
		@return The game's score after the move. Return -1 if game over. 
		Game over when snake crosses the screen boundary or bites its body.
		:type direction: str
		:rtype: int
		"""
		direction = self.directions[direction]
		nextHead = (self.head[0]+direction[0], self.head[1]+direction[1])
		if nextHead[0] < 0 or nextHead[0] >= self.height or nextHead[1] < 0 or nextHead[1] >= self.width:
			return -1
		food = self.foods[self.i] if self.i < len(self.foods) else None
		if food and nextHead == tuple(food):
			self.head = nextHead
			self.blocks.add(self.head)
			self.body.append(self.head)
			self.i += 1
			self.score += 1
			return self.score
		tail = self.body.popleft()
		self.blocks.remove(tail)
		if nextHead in self.blocks:
			return -1
		else:
			self.body.append(nextHead)
			self.blocks.add(nextHead)
			self.head = nextHead
			return self.score

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)