# 7'43

# pravit cemo iterator ala klase range
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
    def __iter__(self):             # zbog iter()-a kako bi vratio iteratora
        return self
    def __next__(self):             # zbog next()-a kako bi izbacivao iteme
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration

for x in Counter(7,77):
    print(x)                # 7,8,9,...75,76 jedno ispod drugog