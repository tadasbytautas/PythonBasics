class Bird:
    def __init__(self, wingspan):
        self.wingspan = wingspan

Eagle = Bird(104)

len(Eagle)

class Bird:
    def __init__(self, wingspin):
        self.wingspan = wingspan

    def __len__(self):
        return self.wingspan

eagle = Bird(104)

len(eagle)