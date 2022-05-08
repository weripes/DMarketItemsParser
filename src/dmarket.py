import urllib.parse
import json

import requests

from src.parameters import ParametersModel


class DMarketItemsParser:

    def __init__(self) -> None:
        self.BASE_API_URL = 'https://api.dmarket.com/exchange/v1/market/items?'

    # Creating a url path understandable for api
    def format_parameters_to_url_path(self, Parameters: ParametersModel) -> str:
        parameters_dict = Parameters.dict(exclude={'gameTitle'})
        parameters_list = []
        for key, value in parameters_dict.items():
            parameters_list.append(f'{key}={urllib.parse.quote(str(value))}')

        return '&'.join(parameters_list)

    def parse_items(self, Parameters: ParametersModel) -> dict:
        # Creating a formatted path and merging with the base api url
        formatted_parameters = self.format_parameters_to_url_path(Parameters=Parameters)
        full_url = self.BASE_API_URL + formatted_parameters
        # Sending a get request and returning the result as a dictionary
        response = requests.get(url=full_url)
        return json.loads(response.content.decode('utf-8'))