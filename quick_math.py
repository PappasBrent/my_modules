#!/usr/bin/python3
'''
A class for analzying statistical data and
for performing quick calculations
'''


class StatAnalyzer:
    '''
    A class for performing various forms of
    statistical analysis on a list of numbers
    '''

    def __init__(self, values):
        if not values:
            raise ValueError('List must not be empty')
        self._values = values

    def mean(self):
        '''
        Calculates and returns the mean value of the dataset
        '''
        mean = 0
        for val in self._values:
            mean += val
        mean /= len(self._values)
        return mean

    def median(self):
        '''
        Calculates and returns the median value of the dataset
        '''
        # Ensures _values is a list and not a generator (e.g. range())
        if not isinstance(self._values, list):
            self._values = list(self._values)

        self._values.sort()
        if len(self._values) % 2 != 0:
            return self._values[int(len(self._values) / 2)]
        else:
            return (self._values[int(len(self._values) / 2) - 1] +
                    self._values[int(len(self._values) / 2)]) / 2

    def mode(self):
        '''
        Calculates and returns the mode value of the datataset
        '''
        # Ensures _values is a list and not a generator (e.g. range())
        if not isinstance(self._values, list):
            self._values = list(self._values)

        mode = self._values[0]
        mode_count = self._values.count(self._values[mode])
        for val in self._values:
            if self._values.count(val) > mode_count:
                mode = val
                mode_count = self._values.count(val)

        return mode

    def range(self):
        '''
        Calculates and returns the range of
        the dataset
        '''
        return max(self._values) - min(self._values)


def sum_of_range(num):
    '''
    Returns the sum of all numbers from 0 to num, inclusive
    '''
    return ((num**2) / 2) + num / 2


def main():
    '''
    Executes script
    '''
    numbers = [14, 14, 11, 11, 11, 11, 11, 3, 7, 7, 7, 7, 4, 8]
    num_stats = StatAnalyzer(numbers)
    print(num_stats.range())

    print(sum_of_range(100))


if __name__ == "__main__":
    main()
