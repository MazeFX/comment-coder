import pytest

from comment_coder.extraction.base import BaseExtractor


@pytest.fixture
def default_base_extractor():
    '''Returns a Base extractor without any settings or prepared values'''
    return BaseExtractor()


def test_base_extractor_creation(default_base_extractor):
    base_extractor = default_base_extractor

    assert isinstance(base_extractor, BaseExtractor)