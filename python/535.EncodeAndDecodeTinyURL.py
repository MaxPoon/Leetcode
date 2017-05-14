class Codec:
	
	def __init__(self):
		self.mapping = dict()
		self.next = 0
	
	def encode(self, longUrl):
		"""Encodes a URL to a shortened URL.
		
		:type longUrl: str
		:rtype: str
		"""
		identifier = "%06d" % self.next
		self.next += 1
		shortUrl = "http://tinyurl.com/" + identifier
		self.mapping[shortUrl] = longUrl
		return shortUrl

	def decode(self, shortUrl):
		"""Decodes a shortened URL to its original URL.
		
		:type shortUrl: str
		:rtype: str
		"""
		return self.mapping[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))