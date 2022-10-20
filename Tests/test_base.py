__author__ = 'Alexandra Dunga'

import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

