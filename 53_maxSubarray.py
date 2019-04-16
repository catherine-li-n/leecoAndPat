class Solution:
	#def maxSubArray(self, nums: List[int]) -> int:
	def DivideAndConquer(self, List, left, right):
		MaxLeftSum = 0
		MaxRightSum = 0
		MaxLeftBorderSum = 0
		MaxRightBorderSum = 0

		if left == right:
			if List[left] > 0:
				return List[left]
			else:
				return 0
		"""分的过程"""
		center = int((left + right) / 2)
		MaxLeftSum = self.DivideAndConquer(List, left, center)
		MaxRightSum = self.DivideAndConquer(List, center + 1, right)

		"""求跨分界线的最大子列和"""
		MaxLeftBorderSum = 0
		LeftBorderSum = 0
		for i in range(center, left-1, -1):
			LeftBorderSum += List[i]
			if LeftBorderSum > MaxLeftBorderSum:
				MaxLeftBorderSum = LeftBorderSum

		MaxRightBorderSum = 0
		RightBorderSum = 0
		for i in range(center + 1, right+1):
			RightBorderSum += List[i]
			if RightBorderSum > MaxRightBorderSum:
				MaxRightBorderSum = RightBorderSum

		return max(MaxLeftSum, MaxRightSum, MaxLeftBorderSum + MaxRightBorderSum)

	def maxSubArray(self, nums: List[int]) -> int:
		res = self.DivideAndConquer(input_list, 0, len(input_list)-1)
		return res
input_list = [-2,1,-3,5,-1,2,1,-5,4]
Solution().maxSubArray(input_list)