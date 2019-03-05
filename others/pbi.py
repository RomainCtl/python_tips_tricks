class ProgressBarIterator(object):
    """
    Object ProgressBarIterator.

    Object that create progress bar with iteration of iterable object.

    :param iterable: object to be iterated
    :type iterable: list or dict
    """
    def __init__(self, iterable, prefix='', suffix='Complete'):
        self.iterable = iterable
        self.current = 0
        self.length = len(iterable)

        self.prefix = prefix
        self.suffix = suffix

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.length <= self.current: raise StopIteration
        else:
            self.current+=1
            self.progress_bar(self.current)
            if type(self.iterable) is dict:
                return list(self.keys())[self.current-1]
            else:
                return self.iterable[self.current-1]

    def __getitem__(self, key):
        return self.iterable[key]

    def __len__(self,):
        return len(self.iterable)

    def items(self):
        self.current = 0
        if type(self.iterable) is not dict: raise AttributeError("'%s' object has no attribute 'items'" % type(self.iterable))
        for k, v in self.iterable.items():
            self.current+=1
            self.progress_bar(self.current)
            yield k, v

    def keys(self):
        if type(self.iterable) is not dict: raise AttributeError("'%s' object has no attribute 'keys'" % type(self.iterable))
        return self.iterable.keys()

    def values(self):
        if type(self.iterable) is not dict: raise AttributeError("'%s' object has no attribute 'values'" % type(self.iterable))
        return self.iterable.values()

    def progress_bar(self, iteration, length = 50, fill = '█'):
        """
        Function progress_bar.

        Call in a loop to create terminal progress bar.

        :params iteration: [Required] current iteration (Int)
        :params length: [Optional] character length of bar (Int)
        :params fill: [Optional] bar fill character (Str)
        """
        percent = ("{0:.1f}").format(100 * (iteration / float(self.length)))
        filledLength = int(length * iteration // self.length)
        bar = fill * filledLength + '-' * (length - filledLength)
        print('\r%s |%s| %s%% %s' % (self.prefix, bar, percent, self.suffix), end = '\r')
        if iteration >= self.length: print()
