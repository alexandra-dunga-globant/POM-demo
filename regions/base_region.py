__author__ = 'Alexandra Dunga'


class BaseRegion:
    """
    This class is the parent of all regions. It contains the generic methods and utilities for all regions.
    """
    _root_locator = None

    def __init__(self, page, root_element=None):
        self.page = page
        self.root_element = root_element

        if self._root_locator:
            self.wait_for_region_to_load()

    @property
    def root(self):
        if self.root_element is None and self._root_locator:
            return self.page.find_element(*self._root_locator)
        return self.root_element

    def wait_for_region_to_load(self):
        return self.page.find_element(self._root_locator)
