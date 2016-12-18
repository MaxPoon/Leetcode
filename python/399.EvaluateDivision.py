class Solution(object):
	def calcEquation(self, equations, values, queries):
		"""
		:type equations: List[List[str]]
		:type values: List[float]
		:type queries: List[List[str]]
		:rtype: List[float]
		"""
		var = set()
		pairs = {}
		for i, equation in enumerate(equations):
			var.add(equation[0])
			var.add(equation[1])
			pairs[(equation[0],equation[1])] = values[i]
			pairs[(equation[1],equation[0])] = 1 / values[i]
		for x in var:
			pairs[(x,x)] = 1
			for y in var:
				for z in var:
					if (x,y) in pairs and (y,z) in pairs:
						pairs[(x,z)] = pairs[(x,y)]*pairs[(y,z)]
						pairs[(z,x)] = 1/pairs[(x,z)]
		results = []
		for query in queries:
			results.append(float(pairs[(query[0], query[1])]) if (query[0], query[1]) in pairs else -1.0)
		return results