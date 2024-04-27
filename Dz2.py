import random

class Pes:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.satiety = 60
        self.alive = True

        def to_play(self):
            print('i wont to play..')
            self.gladness += 0.5
            self.satiety -= 1

        def to_eat(self):
            print('i wont to eat..')
            self.gladness += 1
            self.satiety += 5

        def to_sleep(self):
            print('i wont to sleep..')
            self.gladness += 0
            self.satiety -= 5

        def end_of_day(self):
            print(f'gladness = {round(self.gladness,2)}')
            print(f'satiety = {round(self.satiety,2)}')

        def live(self, day):
            day = f'Day {day} of {self.name} life'
            print(f'{day:=^50}')
            cube = random.randint(1,3)
            if cube == 1:
                self.to_play()
            elif cube == 2:
                self.to_eat()
            elif cube == 3:
                self.to_sleep()

            self.end_of_day()
            self.is_alive()

luna = Pes(name='Luna')
for day in range(1, 10000):
    if not Luna.alive:
        break
    Luna.live(day)