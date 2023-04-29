from dataclasses import dataclass


@dataclass
class AddressesDTO:
    street_id: int
    home_number: int
    postcode: int
    user_id: int
