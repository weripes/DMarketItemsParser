import time
import json

from src.dmarket import PyDmarket
from src.parameters import DmarketParametersModel


def example1():
    """
    This script collects all items from the game csgo with
    the title 'Operation Breakout Weapon Case' at an
    ascending price and saves it to a .py file as a variable
    """

    test1_parameters = DmarketParametersModel(
        gameTitle='csgo',
        orderBy='price',
        orderDir='asc', # Order by ascending price
        title='Operation Breakout Weapon Case',
        types='dmarket',
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
        items = Dmarket.parse_items(Parameters=test1_parameters)

        if 'error' in items:
            raise Exception(items['error'])

        for i in items['objects']:
            result.append(i)
        # if the items are less than the limit, then this is the last page
        if len(items['objects']) < test1_parameters.limit:
            break
        # The value of the cursor is taken and inserted
        # into the model with which items was parsed
        test1_parameters.cursor = items['cursor']
        time.sleep(2) # To avoid throttling

    return result


if __name__ == '__main__':

    test1_all_pages_items = example1()
    # Save the result as a variable in the .py file
    with open('test1_all_pages_items.json', 'w') as file:
        json.dump(test1_all_pages_items, file)
        file.close()
