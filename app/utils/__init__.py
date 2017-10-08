from typing import List, Optional, TypeVar

import re

slug_regex = re.compile(r'^[a-zA-Z0-9-]{1,64}$')

T = TypeVar('T')


def list_without_nones(lst: List[Optional[T]]) -> List[T]:
    """Return a list without any None values."""
    return [i for i in lst if i is not None]
