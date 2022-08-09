# В задании представлена одна большая функция... 
# Делает она всего ничего:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`

# Конечно, вы можете попробовать разобраться как она 
# это делает, но мы бы советовали разнести функционал 
# по более узким функциям и написать их с нуля


csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


class GetUsersList:

    def __init__(self, csv):
        self.csv = csv

    def _read(self):
        return [x.split(';') for x in csv.split('\n')]

    def _sort(self):
        return sorted(self._read(), key=lambda x: x[1])

    def _filter(self):
        return [x for x in self._sort() if int(x[1]) > 10]


if __name__ == '__main__':
    user_list = GetUsersList(csv)
    print(user_list._filter())
