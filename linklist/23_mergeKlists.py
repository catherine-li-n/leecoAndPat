# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import heapify, heappop

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = []
        for node in lists:
        	while node:
        		h.append(node.val)
        		node = node.next
        # 构造一个最小堆
        heapify(h)   # 转换成最小堆

        # 构造链表
        root = ListNode(heappop(h))
        cur = root
        while h:
        	cur.next = ListNode(heappop(h))
        	cur = cur.next
        return root