__author__ = 'Alexandra Dunga'

import pytest


@pytest.mark.usefixtures("browser")
class BaseTest:
    pass
