import heapq


class Solution:
   def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Maintain two heaps:
        # 1. One of tasks which are ready (cycle >= task's enqueue time),
        not_yet_ready = [
            # enqueue_time, processing_time, id
            (x[0], x[1], i)
            for (i, x) in enumerate(tasks)
        ]
        heapq.heapify(not_yet_ready)
        # 2. and one of tasks which aren't
        ready = []
        # We also need to count the cycle and the order
        # start at the cycle of the first ready task
        cycle = not_yet_ready[0][0]  # 0
        order = []
        while len(order) < len(tasks):
            # move all tasks that came enqueued at this cycle to the ready heap
            while len(not_yet_ready) > 0 and not_yet_ready[0][0] <= cycle:
                task_to_move = heapq.heappop(not_yet_ready)
                heapq.heappush(
                    ready,
                    # processing_time, id
                    (task_to_move[1], task_to_move[2]),
                )
            # now pick the task from the ready heap to use:
            # shortest processing time, and if multiple tasks have the same SPP, choose the one with the smallest index
            if ready:
                candidates = [heapq.heappop(ready)]
                heapq.heapify(candidates)
                while len(ready) > 0 and ready[0][0] == candidates[0][0]:
                    heapq.heappush(candidates, heapq.heappop(ready))
                task = heapq.heappop(candidates)
                processing_time, id = task[0], task[1]
                order.append(id)
                cycle += processing_time
                while candidates:
                    heapq.heappush(ready, heapq.heappop(candidates))
            else:  # jump to the cycle of the next ready task instead of increasing by one
                # cycle += 1
                cycle = not_yet_ready[0][0]
        return order

