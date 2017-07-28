import pytest

from vim_turing_machine.constants import BLANK_CHARACTER
from vim_turing_machine.machines.merge_business_hours.encode_hours import encode_hours
from vim_turing_machine.machines.merge_business_hours.encode_hours import encode_in_x_bits


@pytest.mark.parametrize('number, encoded', [
    (0, '00000'),
    (10, '01010'),
    (31, '11111'),
])
def test_encode_in_x_bits(number, encoded):
    assert encode_in_x_bits(number) == '{}{}'.format(BLANK_CHARACTER, encoded)


def test_encode_hours():
    assert encode_hours([(10, 31)]) == '{}{}'.format('01010', '11111')
