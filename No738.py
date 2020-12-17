class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        num_list = list(map(int, str(n)))
        sort_list = num_list.copy()
        sort_list.sort(reverse=False)
        if num_list == sort_list:
            return n
        else:
            num = self.monotoneIncreasingDigits(int(n/10) - 1)
            return num*10 + 9


if __name__ == '__main__':
    solution = Solution()
    print(solution.monotoneIncreasingDigits(603253281))
