import timeit


class testtime:
    def start(self):
        self.start_time = timeit.default_timer()

    def finish(self):
        self.terminate_time = timeit.default_timer()
        print("%f초 걸렸습니다." % (self.terminate_time - self.start_time))
