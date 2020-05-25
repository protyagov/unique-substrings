class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        buckets = {k: 0 for k in 'abcdefghijklmnopqrstuvwxyz'}  # create all possible buckets
        i, n = 0, p.__len__()

        while i < n:
            prev_ord = ord(p[i])
            k = 1
            # find largest sequence
            for j in range(i, n):
                if i == j:
                    continue
                next_ord = ord(p[j])
                diff = prev_ord - next_ord
                if diff == -1 or diff == 25:
                    prev_ord = next_ord
                else:
                    k = 0
                    break
            # assign count to each subsequence between i and j
            for x in range(i, j + 1):
                buckets[p[x]] = max(buckets[p[x]], j - x + k)
            # no need to process very next element, can skip all chars in above sequence
            i = j + k
        return sum(buckets.values())


s = Solution()
assert 1 == s.findSubstringInWraproundString('a')
assert 3 == s.findSubstringInWraproundString('ab')
assert 6 == s.findSubstringInWraproundString('abc')  # a,b,c,ab,bc,abc
assert 6 == s.findSubstringInWraproundString("zaba")  # a,b,z,ab,za,zab
assert 6 == s.findSubstringInWraproundString('ababc')
assert 2 == s.findSubstringInWraproundString('cac')
assert 6 == s.findSubstringInWraproundString('zab')
assert 10 == s.findSubstringInWraproundString('yzab')
assert 10 == s.findSubstringInWraproundString('abcd')  # a,b,c,d,ab,bc,cd,abc,bcd,abcd
