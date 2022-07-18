
from pprint import pprint


rfile_name = "recipes.txt"

cook_book = dict()

def main():

    # задача 1
    with open(rfile_name, encoding="UTF-8") as cfile:
        while True:
            cook_book_key = cfile.readline().strip("\n")
            if len(cook_book_key) > 0 and "|" not in cook_book_key:
                cook_book[cook_book_key] = []
                receipes_counter = cfile.readline().strip("\n")
                receipes_counter = receipes_counter if receipes_counter.isdigit() else 0
                if int(receipes_counter) > 0:
                    for recipe_curcnt in range(int(receipes_counter)):
                        receipe = cfile.readline().strip("\n")
                        try:
                            ringredient, rammount, rquantity = receipe.split("|", maxsplit=3)
                            cook_book[cook_book_key] += [
                                {"ingredient_name" : ringredient.strip(), 
                                "quantity" : rammount.strip(), 
                                "measure" : rquantity.strip()}]
                        except Exception as e:
                            print("Error unpacking ingredients data.", cook_book_key, receipes_counter, recipe_curcnt)
                            break
                else:
                    print("Error unpacking ingredients data.", cook_book_key, receipes_counter)
                    break
            else:
                break
            cfile.readline().strip("\n")
    
    pprint(cook_book)

    # задача 2
    #pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Запеченный картофель', 'Омлет', 'Фахитос'], 2))
    pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


def get_shop_list_by_dishes(dishes, person_count: int) -> dict:
    out_dict = dict()
    for dish in dishes:
        if dish in cook_book:
            for ingredient_item in cook_book[dish]:
                if ingredient_item['ingredient_name'] not in out_dict:
                    out_dict[ingredient_item['ingredient_name']] = {"measure" : ingredient_item['measure'], "quantity" : int(ingredient_item['quantity']) * person_count}
                else:
                    out_dict[ingredient_item['ingredient_name']]["quantity"] +=  int(ingredient_item['quantity']) * person_count
                
        else:
            print(dish, "not found.")
    return out_dict




if __name__ == "__main__":
    main()
