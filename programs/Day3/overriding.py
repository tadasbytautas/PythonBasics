class animal:
    babies = 0

    def reproduce(self):
        self.babies += 1


class dog(animal):
    def reproduce(self):
        self.babies += 6


john = dog()
john.reproduce()
print(john.babies)
