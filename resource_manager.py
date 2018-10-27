# Multi-threading
from multiprocessing    import Queue
from threading          import Thread, Event

class resource_manager(Thread):

    def __init__(self):

        # Class Name
        self.name = 'master'
        print('Thread [{:^10}] - Initializing ... '.format(self.name), end='')

        super(resource_manager, self).__init__()
        print('Done')
