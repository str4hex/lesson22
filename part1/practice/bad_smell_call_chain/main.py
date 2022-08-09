# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов


class Person:
    def __init__(self, room: int, city_population):
        self.room = room
        self.city_population = city_population

    @property
    def get_person_room(self):
        return self.room

    @property
    def get_city_population(self):
        return self.city_population

# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.

person = Person(42, 'Moscow')

print(person.get_person_room)
print(person.get_city_population)