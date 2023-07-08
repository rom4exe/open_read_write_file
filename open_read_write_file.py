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


def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingrs in cook_book[dish]:
                meas_quant = {}
                if ingrs['ingredient_name'] not in ingr_list:
                    meas_quant['measure'] = ingrs['measure']
                    meas_quant['quantity'] = int(ingrs['quantity']) * person_count
                    ingr_list[ingrs['ingredient_name']] = meas_quant
                else:
                    ingr_list[ingrs['ingredient_name']]['quantity'] = ingr_list[ingrs['ingredient_name']]['quantity'] + \
                                                                      int(ingrs['quantity']) * person_count
        else:
            print(f'Блюда {dish} нет в книге')
    return ingr_list


cook_book = read_recipes()
print(f'ЗД_1 read recipes \n {cook_book} \n')

print('ЗД_2 посчитать заказ')
print(get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Шашлык'], 2), '\n')