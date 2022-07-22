from typing import Literal

from pydantic import BaseModel, Field, validator, root_validator


class DmarketParametersModel(BaseModel):
    gameTitle: Literal['csgo', 'dota2', 'teamfortress2', 'rust']
    orderBy: Literal['best_deals', 'best_discount', 'updated', 'price']
    orderDir: Literal['asc', 'desc'] # order directory, asc - ascending, desc - descending
    title: str = str() # search string
    priceFrom: float = Field(default=0, ge=0)
    priceTo: float = Field(default=0, ge=0)
    types: Literal['all', 'dmarket', 'p2p'] #p2p = f2f
    cursor: str = str()
    limit: int = Field(default=100, gt=0, le=100) # 0 > n >= 100 (count of items per page)
    currency: Literal['USD'] = 'USD' # There are no other currencies, on the site is just a currency transfer

    # Using this constant will be possible
    # to create a gameId by its name
    __gameIds = {
        'csgo': 'a8db',
        'dota2': '9a92',
        'teamfortress2': 'tf2',
        'rust': 'rust'
    }

    # For api, only int values ​​are valid, and in order to be guaranteed to be
    # able to convert dollars to cents, needed to have less than two decimals
    @validator('priceFrom', 'priceTo', always=True)
    def less_than_two_decimals(cls, v):
        if len(str(v).split('.')[1]) > 1:
            raise AttributeError('Must be less than two decimals')

        return v

    # Here, dollars are converted to cents
    @validator('priceFrom', 'priceTo', always=True)
    def convert_usd_to_cent(cls, v):
        return int(v * 100)

    # Here is created gameId, it is possibility to
    # avoid entering the id and get it just by name of game
    @root_validator
    def create_gameId(cls, values):
        values['gameId'] = cls.__gameIds[values['gameTitle']]
        return values
