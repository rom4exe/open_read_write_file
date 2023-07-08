def read_recipes():
    cook_book = {}
    with open('recipes.txt') as f:
        for line in f:
            dish = line.strip()
            count = int(f.readline())
            ing_list = []
            for i in range(count):
                ingrs = {'ingredient_name':'', 'quantity':'', 'measure':''}
                ingr_bk = f.readline().strip()
                ingrs['ingredient_name'], ingrs['quantity'], ingrs['measure'] = ingr_bk.split('|')
                ing_list.append(ingrs)
            cook_book[dish] = ing_list
            f.readline()
    return cook_book


cook_book = read_recipes()
print(f'ЗД_1 read recipes \n {cook_book}')