with open("recipesbook.txt", "r", encoding="utf-8") as file:
    cook_book_dict = {}
    # cook_book_keys = []
    for line in file:
        dish_name = line.strip()
        counter = int(file.readline())
        dish_ingr_list = []
        for _ in range(counter):
            ingr = file.readline().strip()
            ingredient_name, quantity, measure = ingr.split(" | ")
            dish_ingr_list.append({"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure})
        cook_book_dict[dish_name] = dish_ingr_list
        file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ing in cook_book_dict[dish]:
            ing_name = ing["ingredient_name"]
            if ing_name not in shop_list:
                shop_list[ing_name] = {"quantity": int(ing["quantity"]) * person_count, "measure": ing["measure"]}
            else:
                shop_list[ing_name]["quantity"] += int(ing["quantity"]) * person_count
    return shop_list


from pprint import pprint

pprint(cook_book_dict, sort_dicts=False)
print(get_shop_list_by_dishes(["Омлет", "Фахитос"], 3))
