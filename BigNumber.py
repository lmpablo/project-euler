class BigNumber(object):
    """A class that lets me deal with arbitrarily big numbers"""
    def __init__(self, initial_value):
        super(BigNumber, self).__init__()
        self.digits = [0] * len(initial_value)
        self.Add(initial_value)

    def Add(self, n):
        if len(n) > len(self.digits):
            additional = len(n) - len(self.digits)
            for i in range(additional):
                self.digits.append(0)

        for i in range(len(n)):
            curr = n[len(n) - i - 1]
            curr_sum = self.digits[i] + int(curr)
            if curr_sum >= 10:
                self.digits[i] = curr_sum - 10
                try:
                    x = self.digits[i + 1]
                except IndexError:
                    self.digits.append(0)

                self.digits[i + 1] += 1
            else:
                self.digits[i] = curr_sum

    def __str__(self):
        num_string = ""
        num_array = self.digits[:]
        for i in range(len(num_array)):
            num_string += str(num_array.pop())

        return num_string