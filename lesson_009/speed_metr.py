from datetime import datetime


class SpeedMetrics:
    def __init__(self, name_process=''):
        self.time_start = None
        self.time_finish = None
        self.interval = None
        self.name_process = name_process

    def start(self, name_process=''):
        self.name_process = name_process
        self.time_start = datetime.now()

    def finish(self):
        self.time_finish = datetime.now()

    def get_interval(self):
        self.finish()
        result = self.time_finish - self.time_start
        print(self.name_process, result)
