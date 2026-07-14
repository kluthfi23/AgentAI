from core.queue.queue_manager import QueueManager


queue = QueueManager()

queue.add("Job 1")
queue.add("Job 2")
queue.add("Job 3")

while not queue.empty():

    print(queue.get())