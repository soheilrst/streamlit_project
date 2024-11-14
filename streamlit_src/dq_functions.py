import pandas as pd
import math
import numpy as np
import re


regex_pattern = r'([a-zA-Z\u00e4\u00f6\u00fc\u00df\s\.\-]+)\s*(\d+[A-Za-z]?[\s\-\/\+]*\d*[A-Za-z]?)'

def extract_house_number(street, regex_pattern :str = regex_pattern):
    if not isinstance(street, str) or pd.isna(street):  
        return None
    match = re.search(regex_pattern, street)
    return match.group(2) if match else None


def extract_street_name(street, regex_pattern: str =regex_pattern) :
    if not isinstance(street, str) or pd.isna(street):  
        return None  
    match = re.search(regex_pattern, street)
    return match.group(1) if match else street

