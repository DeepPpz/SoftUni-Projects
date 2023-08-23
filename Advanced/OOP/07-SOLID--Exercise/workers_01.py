from abc import ABC, abstractmethod


class BaseWorker(ABC):
    @abstractmethod
    def work(self):
        pass


class Worker(BaseWorker):
    def work(self):
        print("I'm working!!")


class NewWorker(BaseWorker):
    def work(self):
        print("I don't know what I'm doing here!!")


class Manager:
    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, BaseWorker), '`worker` must be of type {}'.format(BaseWorker)

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


class SuperWorker(BaseWorker):
    def work(self):
        print("I work very hard!!!")



worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
new_worker = NewWorker()

try:
    manager.set_worker(super_worker)
    manager.manage()
    
    manager.set_worker(new_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
