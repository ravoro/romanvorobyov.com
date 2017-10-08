from app.utils import list_without_nones
from tests import BaseCase


class Test(BaseCase):
    def test_remove_nones(self):
        """Return a list with Nones removed."""
        lst = [2, None, 3, 5, None, None, 7, 8]
        assert list_without_nones(lst) == [2, 3, 5, 7, 8]

    def test_no_nones(self):
        """Return the same list when given a list with no Nones."""
        lst = [2, 3, 5, 7, 8]
        assert list_without_nones(lst) == lst

    def test_only_nones(self):
        """Return an empty list when given a list of only Nones."""
        lst = [None, None, None]
        assert list_without_nones(lst) == []

    def test_empty(self):
        """Return the same empty list when given an empty list."""
        lst = []
        assert list_without_nones(lst) == []
