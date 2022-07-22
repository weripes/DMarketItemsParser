import time
import json

from src.dmarket import PyDmarket
from src.parameters import DmarketParametersModel


def example2():
    """
    This script collects all items from the game
    dota 2 from $10 to $50 with a discount of more
    than 30% and saves it to a .py file as a variable
    """

    test2_parameters = DmarketParametersModel(
        gameTitle='dota2',
        orderBy='best_discount',
        orderDir='desc', # Order by descending discount
        priceFrom=10,
        priceTo=50,
        types='all', # F2F and dmarket bots
        limit=100 # 100 items per page
    )
    Dmarket = PyDmarket()
    result = []
    while True:
        """
        Roughly speaking, the cursor contained in the api response is a
        link to the next page and if pasting it into the parameters without
        changing anything except the cursor, the new result will be the next page
        * Request without cursor return first page
        """
        items = Dmarket.parse_items(Parameters=test2_parameters)

        if 'error' in items:
            raise Exception(items['error'])

        for i in items['objects']:
            # if the item has a discount of less than 30% then finish parsing
            if i['discount'] < 30:
                break

            result.append(i)

        # if the items are less than the limit, then this is the last page
        if len(items['objects']) < test2_parameters.limit:
            break
        # The value of the cursor is taken and inserted
        # into the model with which items was parsed
        test2_parameters.cursor = items['cursor']
        time.sleep(2) # To avoid throttling

    return result


if __name__ == '__main__':
    # Save the result as a variable in the .py file
    test2_best_discount_items = example2()

    with open('test2_best_discount_items.json', 'w') as file:
        json.dump(test2_best_discount_items, file)
        file.close()
