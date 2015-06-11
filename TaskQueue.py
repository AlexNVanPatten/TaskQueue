from collections import deque
from Task import Task

#Class that holds tasks that have yet to be executed
class TaskQueue:

  #Uses a deque as the holding area
  def __init__(self):
    self.tasks = deque()
    self.num_tasks = 0

  #Appends new items to left of the queue, will only accept tasks.
  def push(self, task):
    if (isinstance(task, Task)):
      self.num_tasks += 1
      self.tasks.appendleft(task)
    else:
      raise TypeError("Only Tasks are allowed in the TaskQueue, non-Task was pushed.")        

  #Pops task off right of queue, returns None if there is nothing left
  def pop(self):
    if self.num_tasks == 0:
      return None
    else:
      self.num_tasks -=1
      return self.tasks.pop()

  #Returns list of all tasks in queue.
  def peek_all(self):
    return list(self.tasks)

  #Pops and then replaces task on right of queue, returns none if there is nothing left
  def peek_next(self):
    if self.num_tasks == 0:
      return None
    else:
      next_task = self.tasks.pop()
      self.tasks.append(next_task)
      return next_task

  #Returns number of tasks left in queue
  def count(self):
    return self.num_tasks
