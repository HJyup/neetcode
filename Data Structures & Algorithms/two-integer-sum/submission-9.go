func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)

    for i, v := range nums {
        prev, ok := seen[target - v]
        if ok {
            return []int{prev, i}
        }

        seen[v] = i
    }

    return []int{-1, -1}
}
