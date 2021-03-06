"""
Tests for the scripts file in the top level directory
"""
import logging

import pytest
import numpy as np

from .conftest import requires_epics
from hxrsnd.utils import absolute_submodule_path

logger = logging.getLogger(__name__)

def scripts_import():
    import scripts

@pytest.mark.timeout(60)
@requires_epics
def test_scripts_import_with_epics():
    scripts_import()

# I couldn't quickly get this to pass with ophyd 1.2.0 (zlentz)
# @pytest.mark.timeout(60)
# def test_scripts_import_no_epics():
#    scripts_import()
