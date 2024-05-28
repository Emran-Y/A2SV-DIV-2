# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append([i, j, distance])
        
        adj_list = {i: [] for i in range(len(points))}
        for start, end, weight in edges:
            adj_list[start].append([end, weight])
            adj_list[end].append([start, weight])
        
        min_heap = []
        for neighbor, weight in adj_list[0]:
            heapq.heappush(min_heap, [weight, 0, neighbor])
        
        visited = set()
        visited.add(0)
        total_cost = 0

        while min_heap:
            weight, start, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            total_cost += weight

            for neighbor, weight in adj_list[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, [weight, node, neighbor])

        return total_cost
