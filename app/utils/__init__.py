import re
from typing import List, Optional, TypeVar

slug_regex = re.compile(r'^[a-zA-Z0-9-]{1,64}$')

T = TypeVar('T')


def list_without_nones(l: List[Optional[T]]) -> List[T]:
    """Return a list without any None values."""
    return list(filter(lambda x: x is not None, l))
