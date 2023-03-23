import sys
import typing
import heapq
from collections import deque


class Task(typing.NamedTuple):
	scheduled_at: int
	queue_num: int
	duration: int


class WorkerPool:
	def __init__(self, size: int):
		self._size = size
		# the min-heap of tuples (busy until time, worker index)
		self._workers = [(0, i) for i in range(size)]
		heapq.heapify(self._workers)
		
	def __repr__(self):
		class_name = self.__class__.__name__
		data = repr(self._workers)
		return f"{class_name}({data})"
		
	def isAvailable(self, at_time: int) -> bool:
		return self.getTimeSlot() <= at_time
		
	def getTimeSlot(self):
		return self._workers[0][0]
		
	def assignTask(self, at_time: int, task: Task) -> int:
		assert(self.isAvailable(at_time))
		_, worker_idx = heapq.heappop(self._workers)
		heapq.heappush(self._workers, (at_time + task.duration, worker_idx))
		return worker_idx


class QueuePool:
	def __init__(self, size: int):
		self._task_cnt = 0
		self._size = size
		self._queues: list[deque] = []
		self._priority: list[tuple[int, int]] = []
		
		for i in range(size):
			self._queues.append(deque())
			# (last pop time, queue index)
			self._priority.append((0, i))
		heapq.heapify(self._priority)
		
	def __repr__(self):
		class_name = self.__class__.__name__
		data = [repr(self._queues), repr(self._priority)]
		data = '\n\t'.join(data)
		return f"{class_name}(\n\t{data}\n)"
		
	def push(self, task: Task):
		self._task_cnt += 1
		self._queues[task.queue_num - 1].append(task)
	
	def pop(self, time_at: int) -> Task:
		assert(self._task_cnt > 0)
		poped_queues = []
		queue = None
		while not queue:
			last_pop_time, idx = heapq.heappop(self._priority)
			queue = self._queues[idx]
			if queue:
				last_pop_time = time_at
			poped_queues.append((last_pop_time, idx))
			
		for pq in poped_queues:
			heapq.heappush(self._priority, pq)
			
		return queue.popleft()
						

def read_input():
	n, m, k = map(int, sys.stdin.readline().split())
	print(f"{n} tasks, {m} workers and {k} queues")
	tasks: list[Task] = []
	for line in sys.stdin.readlines():
		s, q, t = map(int, line.split())
		tasks.append(Task(s, q, t))

	return n, m, k, tasks
