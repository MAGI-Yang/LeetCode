# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Cal(object):
	def getNumber(self, l):
		rate = 1
		number = 0
		while l != None:
			number = l.val * rate + number
			rate = rate * 10
			l = l.next
		return number

	def getList(self, n):
		ans = []
		for i in range(0, len(str(n))):
			ans.append(n%10)
			n = n / 10
		return ans

class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		calculator = Cal()
		sum = calculator.getNumber(l1) + calculator.getNumber(l2)
		ans = calculator.getList(sum)
		return ans

