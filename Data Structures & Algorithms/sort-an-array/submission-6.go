func sortArray(nums []int) []int {
    var mergeSort func(nums []int) []int

    merge := func(a, b []int) []int {
        merged := make([]int, len(a) + len(b))

        i, j := 0, 0
        curr := 0

        for i < len(a) && j < len(b) {
            if a[i] <= b[j] {
                merged[curr] = a[i]
                i++
                
            } else {
                merged[curr] = b[j]
                j++
            }

            curr++
        }

        for i < len(a) {
            merged[curr] = a[i]
            i++
            curr++
        }

        for j < len(b) {
            merged[curr] = b[j]
            j++
            curr++
        }

        return merged
    }

    mergeSort = func(nums []int) []int {
        if len(nums) == 1 {
            return nums
        }

        mid := len(nums) / 2
        left := mergeSort(nums[:mid])
        right := mergeSort(nums[mid:])

        return merge(left, right)
    }

    return mergeSort(nums)
}
