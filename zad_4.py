import argparse
import json
from typing import Optional
from urllib.parse import urlencode
from urllib.request import Request, urlopen

API_URL = 'https://api.openbrewerydb.org/v1/breweries'


class Brewery:
    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: str,
        address_1: Optional[str],
        address_2: Optional[str],
        address_3: Optional[str],
        city: str,
        state_province: str,
        postal_code: str,
        country: str,
        longitude: Optional[float],
        latitude: Optional[float],
        phone: Optional[str],
        website_url: Optional[str],
        state: str,
        street: Optional[str],
    ) -> None:
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.state = state
        self.street = street

    def __str__(self) -> str:
        return (
            f'{self.name} ({self.brewery_type})\n'
            f'  Adres: {self.street}, {self.postal_code} {self.city}, '
            f'{self.state_province}, {self.country}\n'
            f'  Telefon: {self.phone}\n'
            f'  WWW: {self.website_url}\n'
            f'  Współrzędne: {self.latitude}, {self.longitude}'
        )


def to_float(value) -> Optional[float]:
    return float(value) if value is not None else None


def create_brewery(data: dict) -> Brewery:
    return Brewery(
        id=data.get('id'),
        name=data.get('name'),
        brewery_type=data.get('brewery_type'),
        address_1=data.get('address_1'),
        address_2=data.get('address_2'),
        address_3=data.get('address_3'),
        city=data.get('city'),
        state_province=data.get('state_province'),
        postal_code=data.get('postal_code'),
        country=data.get('country'),
        longitude=to_float(data.get('longitude')),
        latitude=to_float(data.get('latitude')),
        phone=data.get('phone'),
        website_url=data.get('website_url'),
        state=data.get('state'),
        street=data.get('street'),
    )


def fetch_breweries(count: int = 20,
                    city: Optional[str] = None) -> list:
    params = {'per_page': count}
    if city:
        params['by_city'] = city
    request = Request(f'{API_URL}?{urlencode(params)}',
                      headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(request) as response:
        data = json.loads(response.read())
    return [create_brewery(item) for item in data]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Lista browarów z API')
    parser.add_argument('--city', type=str, default=None,
                        help='Miasto, z którego pobrać browary')
    return parser.parse_args()


args = parse_args()
breweries = fetch_breweries(20, args.city)

for brewery in breweries:
    print(brewery)
    print()
