
from pprint import pprint


rfile_name = "recipes.txt"

cook_book = dict()

def main():

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
                                {"ingredient_name" : ringredient.strip()}, 
                                {"quantity" : rammount.strip()}, 
                                {"measure", rquantity.strip()}]
                        except Exception as e:
                            print("Error unpacking ingredients data.", cook_book_key, receipes_counter, recipe_curcnt)
                            break
                else:
                    print("Error unpacking ingredients data.", cook_book_key, receipes_counter)
                    break
            else:
                print("Error unpacking ingredients data.", cook_book_key)
                break
            cfile.readline().strip("\n")
    
    pprint(cook_book)


if __name__ == "__main__":
    main()
