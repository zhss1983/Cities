"""
    Все возможные алгоритмы поиска пути из одной точки в другую через
    проимежуточные точки. Есть варианты оптимизированные, есть не оптимальные.

    one_way(cities=cities, start='A', finish='D') - возвращает один любой путь,
    в виде списка исходных направлений (точка старта + точка финиша для каждого
    отрезка в форме неизменяемых списков). Движение одностороннее.
    multiway - возвращает все возможные пути аналогично one_way.
    any_way - возвращает один любой путь, но движение рассматривается как
    двухстороннее. Нет разници от старта к финишу двигаться или от финиша к
    старту.
    any_multiway - все возможные пути аналогичные any_way.

    one_way_optimal(cities=cities, start='A', finish='D') - возвращает один
    любой путь, в виде списка точек: старта, промежуточные точки, финиша.
    Движение одностороннее, промежуточные точки не повторяются.
    multiway_optimal - возвращает все возможные пути аналогично one_way_optimal
    any_way_optimal - возвращает один любой путь, но движение рассматривается
    как двухстороннее. Нет разницы от старта к финишу двигаться или от финиша к
    старту. Возвращает список из стартовой точки, промежуточных точек и
    конечной точки, промежуточные точки не повторяются.
    any_multiway_optimal - все возможные пути аналогично any_way_optimal.
"""


cities = [
    ('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'C'), ('D', 'B'), ('F', 'G'),
    ('A', 'D'), ('E', 'C'), ('B', 'E'), ('F', 'C'), ('D', 'F'), ('F', 'A'),
]


def one_way(cities, start, finish):
    queue = [[[], start, cities.copy()]]
    while queue:
        (way, start, steps) = queue.pop(0)
        for step_pos in range(len(steps)):
            if start == steps[step_pos][0]:
                new_way = way.copy()
                new_way.append(steps[step_pos])
                queue.append([
                    new_way,
                    steps[step_pos][1],
                    steps[:step_pos] + steps[step_pos + 1:]
                ])
                if steps[step_pos][1] == finish:
                    return new_way
    return [None]


def multiway(cities, start, finish):
    #out = []
    queue = [[[], start, cities.copy()]]
    while queue:
        (way, start, steps) = queue.pop(0)
        for step_pos in range(len(steps)):
            if start == steps[step_pos][0]:
                new_way = way.copy()
                new_way.append(steps[step_pos])
                queue.append([
                    new_way,
                    steps[step_pos][1],
                    steps[:step_pos] + steps[step_pos + 1:]
                ])
                if steps[step_pos][1] == finish:
                    #out.append(new_way)
                    yield new_way
    #return out or [None]


def any_way(cities, start, finish):
    def check_step(pos_start, target, pos_finish, step_pos, way):
        if target == steps[step_pos][pos_start]:
            new_way = way.copy()
            new_way.append(steps[step_pos][::pos_finish - pos_start])
            queue.append([
                new_way,
                steps[step_pos][pos_finish],
                steps[:step_pos] + steps[step_pos + 1:]
            ])
            if steps[step_pos][pos_finish] == finish:
                return new_way

    queue = [[[], start, cities.copy()]]
    while queue:
        (way, start, steps) = queue.pop(0)
        for step_pos in range(len(steps)):
            new_way_f = check_step(0, start, 1, step_pos, way)
            if new_way_f:
                return new_way_f
            new_way_b = check_step(1, start, 0, step_pos, way)
            if new_way_b:
                return new_way_b
    return [None]


def any_multiway(cities, start, finish):
    def check_step(pos_start, target, pos_finish, step_pos, way):
        if target == steps[step_pos][pos_start]:
            new_way = way.copy()
            new_way.append(steps[step_pos][::pos_finish - pos_start])
            queue.append([
                new_way,
                steps[step_pos][pos_finish],
                steps[:step_pos] + steps[step_pos + 1:]
            ])
            if steps[step_pos][pos_finish] == finish:
                return new_way

    #out = []
    queue = [[[], start, cities.copy()]]
    while queue:
        (way, start, steps) = queue.pop(0)
        #(way, start, steps) = queue.pop()
        for step_pos in range(len(steps)):
            new_way = check_step(0, start, 1, step_pos, way)
            if new_way:
                #out.append(new_way)
                yield new_way
            new_way = check_step(1, start, 0, step_pos, way)
            if new_way:
                #out.append(new_way)
                yield new_way
    #return out or [None]


def one_way_optimal(cities, start, finish):
    queue = [[[], start, cities.copy()]]
    while queue:
        (way, start, steps) = queue.pop(0)
        for step_pos in range(len(steps)):
            if (start not in way) and (start == steps[step_pos][0]):
                new_way = way.copy()
                new_way.append(start)
                queue.append([
                    new_way,
                    steps[step_pos][1],
                    steps[:step_pos] + steps[step_pos + 1:]
                ])
                if steps[step_pos][1] == finish:
                    new_way.append(finish)
                    return new_way
    return [None]


def multiway_optimal(cities, start, finish):
    #out = []
    queue = [[[], start, cities.copy()]]
    while queue:
        (way, start, steps) = queue.pop(0)
        for step_pos in range(len(steps)):
            if (start not in way) and (start == steps[step_pos][0]):
                new_way = way.copy()
                new_way.append(start)
                queue.append([
                    new_way,
                    steps[step_pos][1],
                    steps[:step_pos] + steps[step_pos + 1:]
                ])
                if steps[step_pos][1] == finish:
                    new_way.append(finish)
                    #out.append(new_way)
                    yield new_way
    #return out or [None]


def any_way_optimal(cities, start, finish):
    def check_step(pos_start, target, pos_finish, step_pos, way):
        if (target not in way) and (target == steps[step_pos][pos_start]):
            new_way = way.copy()
            new_way.append(target)
            queue.append([
                new_way,
                steps[step_pos][pos_finish],
                steps[:step_pos] + steps[step_pos + 1:]
            ])
            if steps[step_pos][pos_finish] == finish:
                return new_way

    queue = [[[], start, cities.copy()]]
    while queue:
        (way, start, steps) = queue.pop(0)
        for step_pos in range(len(steps)):
            new_way = check_step(0, start, 1, step_pos, way)
            if new_way:
                new_way.append(finish)
                return new_way
            new_way = check_step(1, start, 0, step_pos, way)
            if new_way:
                new_way.append(finish)
                return new_way
    return [None]


def any_multiway_optimal(cities, start, finish):
    def check_step(pos_start, target, pos_finish, step_pos, way):
        if (target not in way) and (target == steps[step_pos][pos_start]):
            new_way = way.copy()
            new_way.append(target)
            queue.append([
                new_way,
                steps[step_pos][pos_finish],
                steps[:step_pos] + steps[step_pos + 1:]
            ])
            if steps[step_pos][pos_finish] == finish:
                return new_way

    #out = []
    queue = [[[], start, cities.copy()]]
    while queue:
        (way, start, steps) = queue.pop(0)
        for step_pos in range(len(steps)):
            new_way = check_step(0, start, 1, step_pos, way)
            if new_way:
                new_way.append(finish)
                #out.append(new_way)
                yield new_way
            new_way = check_step(1, start, 0, step_pos, way)
            if new_way:
                new_way.append(finish)
                #out.append(new_way)
                yield new_way
    #return out or [None]


if __name__ == '__main__':
    print('==================================================================')
    print('start = A, finish = D', *one_way(cities, 'A', 'D'), sep=', ')
    print()
    print('start = A, finish = F', *one_way(cities, 'A', 'F'), sep=', ')
    print()
    print('start = D, finish = D', *one_way(cities, 'D', 'D'), sep=', ')
    print()
    print('start = G, finish = E', *one_way(cities, 'G', 'E'), sep=', ')
    print('==================================================================')
    print('start = A, finish = D', *multiway(cities, 'A', 'D'), sep='\n')
    print()
    print('start = A, finish = F', *multiway(cities, 'A', 'F'), sep='\n')
    print()
    print('start = D, finish = D', *multiway(cities, 'D', 'D'), sep='\n')
    print()
    print('start = G, finish = E', *multiway(cities, 'G', 'E'), sep='\n')
    print('==================================================================')
    print('start = A, finish = D', *any_way(cities, 'A', 'D'), sep=', ')
    print()
    print('start = A, finish = F', *any_way(cities, 'A', 'F'), sep=', ')
    print()
    print('start = D, finish = D', *any_way(cities, 'D', 'D'), sep=', ')
    print()
    print('start = G, finish = E', *any_way(cities, 'G', 'E'), sep=', ')
    print('==================================================================')
    print('start = A, finish = D', *any_multiway(cities, 'A', 'D'), sep='\n')
    print()
    print('start = A, finish = F', *any_multiway(cities, 'A', 'F'), sep='\n')
    print()
    print('start = D, finish = D', *any_multiway(cities, 'D', 'D'), sep='\n')
    print()
    print('start = G, finish = E', *any_multiway(cities, 'G', 'E'), sep='\n')
    print('==================================================================')

    print('==================================================================')
    print('start = A, finish = D', one_way_optimal(cities, 'A', 'D'), sep=', ')
    print()
    print('start = A, finish = F', one_way_optimal(cities, 'A', 'F'), sep=', ')
    print()
    print('start = D, finish = D', one_way_optimal(cities, 'D', 'D'), sep=', ')
    print()
    print('start = G, finish = E', one_way_optimal(cities, 'G', 'E'), sep=', ')
    print('==================================================================')
    print(
        'start = A, finish = D', *multiway_optimal(cities, 'A', 'D'), sep='\n')
    print()
    print(
        'start = A, finish = F', *multiway_optimal(cities, 'A', 'F'), sep='\n')
    print()
    print(
        'start = D, finish = D', *multiway_optimal(cities, 'D', 'D'), sep='\n')
    print()
    print(
        'start = G, finish = E', *multiway_optimal(cities, 'G', 'E'), sep='\n')
    print('==================================================================')
    print('start = A, finish = D', any_way_optimal(cities, 'A', 'D'), sep=', ')
    print()
    print('start = A, finish = F', any_way_optimal(cities, 'A', 'F'), sep=', ')
    print()
    print('start = D, finish = D', any_way_optimal(cities, 'D', 'D'), sep=', ')
    print()
    print('start = G, finish = E', any_way_optimal(cities, 'G', 'E'), sep=', ')
    print('==================================================================')
    print(
        'start = A, finish = D',
        *any_multiway_optimal(cities, 'A', 'D'), sep='\n')
    print()
    print(
        'start = A, finish = F',
        *any_multiway_optimal(cities, 'A', 'F'), sep='\n')
    print()
    print(
        'start = D, finish = D',
        *any_multiway_optimal(cities, 'D', 'D'), sep='\n')
    print()
    print(
        'start = G, finish = E',
        *any_multiway_optimal(cities, 'G', 'E'), sep='\n')
    print('==================================================================')
