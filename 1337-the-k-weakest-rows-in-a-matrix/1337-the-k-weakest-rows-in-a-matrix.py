class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        pq = []
        for i in range(len(mat)):
            s = sum(mat[i])
            heapq.heappush(pq, (s, i))

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(pq)[1])
        
        return ans
        