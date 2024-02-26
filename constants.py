"""ARED - Iván Belenky 2024"""
from enum import Enum

class CurrencyType(Enum):
    USD = 1
    ARS = 2

class OperationType(Enum):
    ''' BUY, RENT, and RENT Temporal operations are the
    most common operations in the real estate market.
    More even so, renting (and tmp renting) in recent history
    has been a known as a depleted market due to the nature
    and pressence of the unregistered market in Argentina.
    
    ARED contains mostly BUY operations ~ 92% of the total
    whereas RENT is ~5 and the rest assigned to temporal.
    '''
    BUY = 1
    RENT = 2
    RENT_TMP = 3


class ConditionType(Enum):
    '''Conditions types are traits selected by the real estate
    market agents so it is a vairable to be taken with a grain 
    of salt. There is no detrimental category such as BAD, so 
    the subjectivity for this field should be taken into account
    when utilizing the dataset.
    '''
    BRAND_NEW = 1
    TO_REFACTOR = 2
    STILL_CONSTRUCTING = 3
    REFACTORED = 4
    EXCELENT = 5
    VERY_GOOD = 6
    GOOD = 7
    REGULAR = 8


class PropertyType(Enum):
    '''Most property types correspond to some form of 
    apartment or houses. Nevertheless grouping may be done
    for non typical property types such as commercial use or 
    storage, or plainly disregard it from the usual applications
    of real estate data analysis and prediction objectives.
    '''
    DUPLEX_APARTMENT = 1
    STANDARD_APARTMENT = 2
    LOFT_APARTMENT = 3
    SINGLE_ROOM_APARTMENT = 4
    PENTHOUSE_APARTMENT = 5
    FLOOR_APARTMENT = 6
    SEMI_FLOOR_APARTMENT = 7
    TRIPLEX_APARTMENT = 8
    HOUSE = 9
    DUPLEX_HOUSE = 10
    TRIPLEX_HOUSE = 11
    PH = 12
    HOTEL = 13
    BUILDING = 14
    OTHERS = 15
    OFFICE = 16
    STORE_LIKE = 17
    LAND1 = 18
    FARM = 19
    COMMERCIAL1 = 20
    GARAGE = 21
    STORAGE1 = 22
    LAND2 = 23
    LAND3 = 26
    COMMERCIAL2 = 27
    STORAGE2 = 28
