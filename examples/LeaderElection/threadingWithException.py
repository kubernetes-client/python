import threading
import ctypes
import time


# Based on https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/
class thread(threading.Thread):
    def __init__(self, function):
        threading.Thread.__init__(self, daemon=True)
        self.function = function

    def run(self):
        try:
            self.function()
        finally:
            pass

    def get_id(self):
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def stop(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
                                                         ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Thread could not be killed - Exception raise failure')
