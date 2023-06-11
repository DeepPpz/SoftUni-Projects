def shop_from_grocery_list(budget, grocery_list, *args):
    bought_items = []
    for (item, price) in args:
        if item in bought_items or item not in grocery_list:
            continue
        if price <= budget:
            budget -= price
            bought_items.append(item)
        else:
            break

    end_result = ''
    if len(bought_items) == len(grocery_list):
        end_result = f'Shopping is successful. Remaining budget: {budget:.2f}.'
    else:
        not_bought = [x for x in grocery_list if x not in bought_items]
        end_result = f'You did not buy all the products. Missing products: {", ".join(not_bought)}.'
    return end_result
