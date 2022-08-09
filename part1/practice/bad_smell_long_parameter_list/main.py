# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self):
        self.field = None
        self.x_coord = None
        self.y_coord = None
        self.direction = None
        self.crawl = None
        self.speed = None

    def move(self, field, x_coord, y_coord, direction, is_fly, crawl, speed = 1):

        match is_fly:
            case 'UP':
                new_y = y_coord + speed
                new_x = x_coord
            elif direction == 'DOWN':
                new_y = y_coord - speed
                new_x = x_coord
            elif direction == 'LEFT':
                new_y = y_coord
                new_x = x_coord - speed
            elif direction == 'RIGTH':
                new_y = y_coord
                new_x = x_coord + speed


            field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
