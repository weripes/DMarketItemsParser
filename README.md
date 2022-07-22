# PyDmarket (DMarket API Wrapper)
Allows you to parse data about items listed on the dmarket exchange from games (csgo, dota 2, team fortress 2, rust) according to the specified parameters

# Quick start
Folder `src` contains the `dmarket.py` file, there are class `PyDmarket` with functions for convenient parsing of items and getting them in the form of a dictionary.
This folder also contains the `parameters.py` file, there are dataclass `DmarketParametersModel` which, using pydantic, allows you to conveniently set the necessary filters for parsing items.

* ### About `parameters.py`
  * #### This file contains dataclass `DmarketParametersModel`, which will later act as an argument for the parser class functions. Contains many filters. Validation allows you to avoid any errors and easily correct existing ones.
  * #### Contains filters:
    * `gameTitle`: Must contain one of the values `['csgo', 'dota2', 'teamfortress2', 'rust']`
    * `orderBy`: Must contain one of the values `['best_deals', 'best_discount', 'updated', 'price']`
    * `orderDir`: Must contain one of the values `['asc', 'desc']`
    * `title`: This is the name of the item, must be string
    * `priceFrom`: This is from what price items will be searched for, must be float and greater than 0, to disable filter don't set parameter or set 0, can contain only two numbers after the decimal point
    * `priceTo`: This is from what price items will be searched for. Further as field priceFrom
    * `types`: In this field, you can select the type of items hold: `dmarket` are those that are in the inventory of bots, `p2p` items are held by sellers, `all` - all. Must contains one of the values `['all', 'dmarket', 'p2p']`
    * `cursor`: Read `example1.py`, line 30
    * `limit`: The maximum number of items received from request. Must be less than 100 and greater than 0, default value is 100, must be integer
    * `currency`: Unfortunately, there is no choice yet, only `USD`, the field is added only for convenient formatting to the path for the domain api

* ### About `dmarket.py`
  * #### Function `parse_items`
      This function parse items.
      Accepts as argument class of type `DmarketParametersModel` with the given parameters and return dict with items

  * #### Function `__format_parameters_to_url_path`:
      The function is mostly needed to be used by previous function.
      Like the previous function, accepts as argument class of type `DmarketParametersModel` with the given parameters and return the path for the dmarket API domain
      
 # How to use?
 * ### See `example1.py` and `example2.py`
