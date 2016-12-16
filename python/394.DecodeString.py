class Solution(object):
	def decodeString(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		k = 0
		parts = [""]
		digits = []
		for c in s:
			if c.isdigit():
				if k >= len(digits): 
					digits.append(0)
					parts.append("")
				digits[k] = digits[k] * 10 + int(c)
			elif c == '[':
				k += 1
			elif c == ']':
				parts[k - 1] += digits[k - 1] * parts[k]
				digits[k - 1] = 0
				parts[k] = ''
				k -= 1
			else:
				parts[k] += c
		return parts[0]