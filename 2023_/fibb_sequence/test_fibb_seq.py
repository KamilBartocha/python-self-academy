from fibb_sequence_4_methods import *

def test_results_for_initial_conditions():
    assert calculate_fibb(1) == 0
    assert calculate_fibb(2) == 1
    assert calculate_fibb_for(1) == 0
    assert calculate_fibb_for(2) == 1

def test_two_numbers_medium_range():
    assert calculate_fibb(10) == 34
    assert calculate_fibb(100) == 218922995834555169026
    assert calculate_fibb_for(10) == 34
    assert calculate_fibb_for(100) == 218922995834555169026
