"""ARED - Iván Belenky 2024"""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class ARED:
    id: str
    created_dt: datetime
    last_seen_dt: datetime

    # description of the property, it is a free text field
    # used mainly to describe the property and its features.
    description: str
    # property type & condition type are categorical variables 
    # check constants for more info
    property_type: int
    condition_type: int
    year_built: int

    # buy rent or rent temporarily, check constants for more info
    operation_type: int
    price: float
    currency: int # either USD or ARS

    lat: float
    lon: float
    province: str # l2 administrative division

    # habitable listings traits
    rooms: int
    bedrooms: int
    bathrooms: int
    m2_total: float
    m2_covered: float
    # land listings traits
    m2_land: float


def download_ARED(): pass