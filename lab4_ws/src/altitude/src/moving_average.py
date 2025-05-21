# The MovingAverage implements the concept of window in a set of measurements.
# The window_size is the number of most recent measurements used in average.
# The measurements are continuously added using the method add.
# The get_average method must return the average of the last window_size measurements.

class MovingAverage:
    def __init__(self, window_size):
        #TODO 
        self.size= window_size
        self.measurements = []
        pass

    # add a new measurement
    def add(self, val):
        #TODO
        self.measurements.append(val)
     
    # return the average of the last window_size measurements added 
    # or the average of all measurements if less than window_size were provided
    # if no values have been added, return 0
    def get_average(self):
        #TODO
        num_m = len(self.measurements)
        if num_m == 0:
            return 0
        elif num_m < self.size:
            total = 0
            for i in self.measurements:
                total += i
            return total/num_m
        else:
            total = 0
            for i in range(num_m - self.size, num_m):
                total += self.measurements[i]
            return total/self.size