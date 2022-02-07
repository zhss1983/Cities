"""
    Решение задачи поиска самого короткого пути из одной точки в другую.
    Алгоритм просматривает все промежуточные точки и параллельно прописывает
    все самые короткие пути из всех доступных в данной точки маршрутов.
    Алгоритм сначала со сложностью не более O(N^2) строит вспомогательную
    структуру данных, тратит на это не более O(N^2) памяти. Затем за O(N) шагов
    находит требуемый путь, если требуется выписать абсолютно все пути, то
    получится O(N^3) итераций. Реально работает гораздо быстрее. В среднем
    построение структуры занимает O(N*M) шагов где M - количество реально хоть
    как-то связанных между собой городов. Памяти так же требуется O(N*M).
    А скорость поиска соответствует среднему пути от одного пункта до другого и
    приближается к O(N/2) для одного любого маршрута.

    Ограничения: ищет только самый короткий маршрут, выбирает любой доступный
    из равнозначных, не может искать длинные маршруты.
"""

cities = [
    ('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A'), # Цикл
    ('F', 'G'), ('G', 'H'), ('G', 'I'), ('G', 'J'), ('J', 'K'), ('H', 'K'),
    ('K', 'L'),  # Ветвление с циклом
    ('M', 'N'), ('N', 'M'),  # В любую сторону
    ('O', 'P'), ('Q', 'R'), ('S', 'S'), # Обособленные

]


def citys_ways(cities, back=0, forward=0):
    """ Создаёт структуру данных и заранее просчитывает все пути. """
    def way_prolongation(start, finish, ckey):
        changed = 0
        for key in start:
            steps = start[key]['steps'] + 1  # Шагов до key через start
            temp = finish.get(key)  # Уже есть запись
            # Назад
            #print(
            # f'Путь в {key} через {city[0]} из {city[1]} за {steps} шагов.')
            # Впрёд
            #print(
            # f'Путь в {key} через {city[1]} из {city[0]} за {steps} шагов.')
            if temp is None:  # Нет, не было
                # Создаю
                finish[key] = {
                    'through': start, 'steps': steps, 'key': ckey}
                changed = 1
            elif temp['steps'] > steps:  # Было
                # Обновляю
                temp['through'] = start
                temp['steps'] = steps
                temp['key'] = ckey
                changed = 1
        return changed

    tree = {}
    for city in cities:
        start = tree.setdefault(city[0], {})
        finish = tree.setdefault(city[1], {})
        # Я не захотел применять конструкции типа
        # mydict.keys()[mydict.values().index(16)]
        # для получения ключа в будущем. Поэтому сохраняю отдельно ключ "key".
        if back:  # Движение назад
            finish[city[0]] = {
                'through': start, 'steps': 1, 'key': city[0]}
        # f'Путь в {city[0]} через {city[0]} из {city[1]} за 1 шагов'
        if forward:  # Движение вперёд
            start[city[1]] = {
                'through': finish, 'steps': 1, 'key': city[1]}
        #print(f'Путь в {city[1]} через {city[1]} из {city[0]} за 1 шагов')
        #finish[city[1]] = {'through': finish, 'steps': 0}  # Стою на месте
        #start[city[0]] = {'through': start, 'steps': 0}  # Стою на месте
    changed = 1
    while changed:
        changed = 0
        for city in cities:
            if back:
                changed |= way_prolongation(
                    tree.get(city[0]), tree.get(city[1]), city[0])
            if forward:
                changed |= way_prolongation(
                    tree.get(city[1]), tree.get(city[0]), city[1])
    return tree


def find_best_way(tree, start, finish):
    if finish not in tree:
        return
    out = [finish]
    target = tree[finish].get(start)
    if target is None:
        return
    while target['steps'] > 1:
        out.append(target['key'])
        target = target['through'][start]
    out.append(start)
    return out[::-1]


if __name__ == '__main__':
    print('Forward')
    tree = citys_ways(cities, 1, 0)
    print('==================================================================')
    print('start = A, finish = A', find_best_way(tree, 'A', 'A'), sep=', ')
    print()
    print('start = A, finish = E', find_best_way(tree, 'A', 'E'), sep=', ')
    print()
    print('start = E, finish = A', find_best_way(tree, 'E', 'A'), sep=', ')
    print()
    print('start = F, finish = L', find_best_way(tree, 'F', 'L'), sep=', ')
    print()
    print('start = L, finish = F', find_best_way(tree, 'L', 'F'), sep=', ')
    print()
    print('start = N, finish = M', find_best_way(tree, 'N', 'M'), sep=', ')
    print()
    print('start = O, finish = S', find_best_way(tree, 'O', 'S'), sep=', ')
    print('==================================================================')
    print('Backword')
    tree = citys_ways(cities, 0, 1)
    print('==================================================================')
    print('start = A, finish = A', find_best_way(tree, 'A', 'A'), sep=', ')
    print()
    print('start = A, finish = E', find_best_way(tree, 'A', 'E'), sep=', ')
    print()
    print('start = E, finish = A', find_best_way(tree, 'E', 'A'), sep=', ')
    print()
    print('start = F, finish = L', find_best_way(tree, 'F', 'L'), sep=', ')
    print()
    print('start = L, finish = F', find_best_way(tree, 'L', 'F'), sep=', ')
    print()
    print('start = N, finish = M', find_best_way(tree, 'N', 'M'), sep=', ')
    print()
    print('start = O, finish = S', find_best_way(tree, 'O', 'S'), sep=', ')
    print('==================================================================')
    print('Any')
    tree = citys_ways(cities, 1, 1)
    print('==================================================================')
    print('start = A, finish = A', find_best_way(tree, 'A', 'A'), sep=', ')
    print()
    print('start = A, finish = E', find_best_way(tree, 'A', 'E'), sep=', ')
    print()
    print('start = E, finish = A', find_best_way(tree, 'E', 'A'), sep=', ')
    print()
    print('start = F, finish = L', find_best_way(tree, 'F', 'L'), sep=', ')
    print()
    print('start = L, finish = F', find_best_way(tree, 'L', 'F'), sep=', ')
    print()
    print('start = N, finish = M', find_best_way(tree, 'N', 'M'), sep=', ')
    print()
    print('start = O, finish = S', find_best_way(tree, 'O', 'S'), sep=', ')
    print('==================================================================')
