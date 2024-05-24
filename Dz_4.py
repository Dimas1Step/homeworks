class  memory:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.memory = 256
        self.model = model
    def calculate(self):
       print("calculating...")

class display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resolution = '4k'
    def Display(self):
        print('I display the image on the screen..')

class charge:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.time = '1 hour'
    def charge(self):
        print('I charge youre phone for work')

class phone(memory, display, charge):
    def print_info(self):
        print(f'memory - {self.memory}')
        print(f'resolution - {self.resolution}')
        print(f'model - {self.model}')
        print(f'charge time - {self.time}')

Smartphone = phone(model = 'Iphone 15 Pro Max')
Smartphone.print_info()