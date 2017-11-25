import string

import random


def get_str(len):
    return ''.join(random.sample(string.ascii_letters + string.digits, len))