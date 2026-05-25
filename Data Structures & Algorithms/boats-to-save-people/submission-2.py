class Solution:
	def numRescueBoats(self, people: List[int], limit: int) -> int:
		ans = 0 
		people.sort()

		if people[-1] > limit:
			return -1

		l, r = 0, len(people) - 1
		while l <= r:
			if l != r and people[r] + people[l] <= limit:
				l += 1
			
			ans += 1
			r -= 1

		return ans