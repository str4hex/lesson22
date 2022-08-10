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

    def get_list(self):
        data = self._read(self.csv)
        data_sort = self._sort(data)
        return self._filter(data_sort)

    def _read(self, csv):
        return [x.split(';') for x in csv.split('\n')]

    def _sort(self, sort_csv):
        return sorted(sort_csv, key=lambda x: x[1])

    def _filter(self, data_filtes):
        return [x for x in data_filtes if int(x[1]) > 10]

    def __repr__(self):
        return str(self.get_list())


if __name__ == '__main__':
    user_list = GetUsersList(csv)
    print(user_list)
