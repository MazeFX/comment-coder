import pytest

from comment_coder.extraction import PythonExtractor


@pytest.fixture
def default_python_extractor():
    '''Returns a Python extractor without any settings or prepared values'''
    return PythonExtractor()


def test_python_extractor_creation(default_python_extractor):
    python_extractor = default_python_extractor

    assert isinstance(python_extractor, PythonExtractor)
#
#
# @pytest.mark.asyncio
# @pytest.mark.parametrize("round_id,angle,result", [
#     (None, -1, None),
#     (None, 21, None),
#     (None, 189, None),
#     (None, 359, None),
#     (0, 0, -4),
#     (0, 22, 17),
#     (0, 189, 185),
#     (0, 256, 248),
#     (0, 356, -4),
# ])
# async def test_get_correct_slice(default_cone_with_dummy_history, round_id, angle, result):
#     slice = await default_cone_with_dummy_history.get_slice(round_id=round_id, angle=angle)
#     assert slice == result
#
#
# @pytest.mark.parametrize("orig_value,new_value,perc,result", [
#     (100, 105, 5, True),
#     (100, 106, 5, False),
#     (100, 106, 10, True),
#     (100, 111, 10, False),
#     (100, 95, 5, True),
#     (100, 94, 5, False),
#     (100, 94, 10, True),
#     (100, 89, 10, False),
# ])
# def test_is_within_percentage(default_cone, orig_value, new_value, perc, result):
#     within = default_cone._is_within_percentage(orig_value, new_value, perc=perc)
#     assert within == result
#
#
# @pytest.mark.asyncio
# async def test_store_slice_stores_slice_with_defaults(default_cone_with_dummy_history):
#     default_cone_with_dummy_history._round_id = 1
#     default_cone_with_dummy_history.round_history[1] = {}
#     default_cone_with_dummy_history.angle_tracker = 257
#
#     slice = 'slice'
#     await default_cone_with_dummy_history.store_slice(slice)
#     assert default_cone_with_dummy_history.round_history[1][257] == slice
#
#
# @pytest.mark.asyncio
# async def test_store_slice_stores_slice_over_old_slice(default_cone_with_dummy_history):
#     default_cone_with_dummy_history._round_id = 1
#     default_cone_with_dummy_history.round_history[1] = {}
#     default_cone_with_dummy_history.angle_tracker = 257
#     default_cone_with_dummy_history.round_history[1][257] = 'slice'
#
#     slice = 'new_slice'
#     await default_cone_with_dummy_history.store_slice(slice, angle=257)
#     assert default_cone_with_dummy_history.round_history[1][257] == slice