#!usr/bin/python3
'''
Converts a given time to its equivalent in words
'''


class SpeakTime:
    '''
    A simple function class to
    return the time as words
    '''

    def __init__(self, **kwargs):
        self.vals = kwargs

        self._words_1_12 = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
                            6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
                            11: "eleven", 12: "twelve"}
        self._words_10_19 = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
                             15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
                             19: "nineteen"}
        self._words_tens = {
            1: "ten", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
        }

        if self.vals.get("ampm") is not None:
            self.ampm = self.vals.get("ampm")
        else:
            if self.hour <= 12:
                self.ampm = "morning"
            elif 12 < self.hour <= 15:
                self.ampm = "afternoon"
            else:
                self.ampm = "evening"

    @property
    def hour(self):
        '''
        Returns the hour in militay time
        '''
        return self.vals.get("hour")

    @property
    def minute(self):
        '''
        Returns the minute
        '''
        return self.vals.get("minute")

    @property
    def _hour_word(self):
        return self._words_1_12.get(self.hour) if self.hour <= 12 \
            else self._words_1_12.get(self.hour % 12)

    @property
    def _minute_word(self):
        if self.minute == 0:
            return "o'clock"
        elif self.minute < 10:
            return "oh {}".format(self._words_1_12.get(self.minute))
        elif self.minute == 10:
            return self._words_1_12.get(self.minute)
        elif 10 <= self.minute <= 19:
            return self._words_10_19.get(self.minute)
        else:
            tens_digit = int(str(self.minute)[0])
            ones_digit = int(str(self.minute)[1])

            if ones_digit == 0:
                return self._words_tens.get(tens_digit)
            else:
                return ("{}-{}".format(self._words_tens.get(tens_digit),
                                       self._words_1_12.get(ones_digit)))

    def __str__(self):
        return "{} {} in the {}".format(self._hour_word, self._minute_word, self.ampm)


def main():
    '''
    Executes script
    '''
    for hour in range(1, 24):
        for minute in range(1, 60):
            print(SpeakTime(hour=hour, minute=minute))

    from datetime import datetime

    now = datetime.now()
    print('Current time:\t', SpeakTime(hour=now.hour, minute=now.minute))


if __name__ == "__main__":
    main()
