class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		ans = 0
		left = 0 # left margin of the substring
		position = {} # position of each char
		for i in range(len(s)):
			# if current char exists in the current longest substring, 
			# if yes, move the margin to next.
			if s[i] in position and position[s[i]] >= left:
				left = position[s[i]] +1
			position[s[i]] = i
			ans = max(ans, i-left+1)
		return ans

