from queue import Queue


class QueueManager:

    def __init__(self):

        self.queue = Queue()


    def add(self, job):

        self.queue.put(job)


    def get(self):

        if self.queue.empty():
            return None

        return self.queue.get()


    def empty(self):

        return self.queue.empty()


    def size(self):

        return self.queue.qsize()