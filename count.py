class count:
    def __init__(self, filename='filename'):
        self.stats = {}
        with open(filename, 'rb') as f:
            while True:
                char = f.read(1)
                if char == '':
                    break
                elif char not in self.stats:
                    self.stats[char] = 0
                self.stats[char] += 1

    def stats(self):
        return self.stats.copy()

if __name__ == '__main__':
    print 'filename: \t{}'.format(count('filename').stats)
    print 'count.py:\t{}'.format(count('count.py').stats)
    print 'example_script.py:\t{}'.format(count('example_script.py').stats)
