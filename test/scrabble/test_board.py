import pytest
from scrabble.board import *
from scrabble.location import *


@pytest.fixture
def board():
    yield Board()


def test_bonus_squares_are_properly_laid_out(board):
    assert str(board) == '\n'.join(LAYOUT)


def test_valid_letters_can_be_played_from_hand(board):
    assert board.can_be_drawn_from_hand('cheese', 'eecchse')


def test_hand_tiles_cannot_be_reused_in_same_word(board):
    assert not board.can_be_drawn_from_hand('spouse', 'poseur_')


def test_blanks_can_be_drawn_from_hand(board):
    assert board.can_be_drawn_from_hand('beaST', 'ab_cd_e')


def test_initial_word_can_be_placed(board):
    assert board.can_be_placed_on_board('horn', CENTER, HORIZONTAL)


def test_word_cannot_overlap_tiles_on_board(board):
    board.place_word('horn', CENTER, HORIZONTAL)
    assert not board.can_be_placed_on_board('tank', Location(6, 8), VERTICAL)


def test_word_cannot_contain_gaps(board):
    assert not board.can_be_placed_on_board('p nt', CENTER, HORIZONTAL)


def test_word_can_use_existing_letters(board):
    board.place_word('horn', CENTER, HORIZONTAL)
    assert board.can_be_placed_on_board('fa m', Location(5, 9), VERTICAL)


def test_word_cannot_have_existing_tiles_before_or_after(board):
    board.place_word('horn', CENTER, HORIZONTAL)
    assert not board.can_be_placed_on_board('xx', Location(5, 7), VERTICAL)
    assert not board.can_be_placed_on_board('xx', Location(8, 7), VERTICAL)


def test_word_cannot_extend_beyond_board(board):
    assert not board.can_be_placed_on_board('beyond', Location(2, 10), HORIZONTAL)


def test_initial_word_counts_as_connected(board):
    assert board.would_be_connected('horn', Location(7, 5), HORIZONTAL)


def test_word_using_initial_tile_counts_as_connected(board):
    board.place_word('horn', CENTER, HORIZONTAL)
    assert board.would_be_connected('fa m', Location(5, 9), VERTICAL)


def test_word_next_to_eisting_tile_counts_as_connected(board):
    board.place_word('horn', CENTER, HORIZONTAL)
    assert board.would_be_connected('apple', Location(6, 9), HORIZONTAL)


def test_unconnected_word_does_not_count_as_connected(board):
    board.place_word('horn', CENTER, HORIZONTAL)
    assert not board.would_be_connected('trounce', Location(0, 0), HORIZONTAL)


def test_accept_valid_dictionary_word(board):
    assert board.is_valid_word('horn', CENTER, HORIZONTAL)


def test_rejects_invalid_dictionary_word(board):
    assert not board.is_valid_word('gqnx', CENTER, HORIZONTAL)


def test_accepts_play_that_creates_legal_words(board):
    board.place_word('horn', CENTER, HORIZONTAL)
    assert board.would_create_only_legal_words('pan', Location(6, 6), HORIZONTAL)


def test_rejects_playt_that_creates_illegal_word(board):
    board.place_word('horn', CENTER, HORIZONTAL)
    assert not board.would_create_only_legal_words('and', Location(6, 7), HORIZONTAL)


def test_scores_single_initial_word(board):
    assert board.score('horn', CENTER, HORIZONTAL) == 14


def test_scores_multiple_words(board):
    board.place_word('horn', CENTER, HORIZONTAL)
    assert board.score('an', Location(6, 7), HORIZONTAL) == 11


def test_does_not_score_unmodified_cross_words(board):
    board.place_word('horn', CENTER, HORIZONTAL)
    assert board.score('a ', Location(6, 7), VERTICAL) == 5


def test_scores_bingo(board):
    assert board.score('finalLy', CENTER, HORIZONTAL) == 76


def test_does_not_score_bingo_for_seven_letter_word_using_tiles_on_board(board):
    board.place_word('horn', CENTER, HORIZONTAL)
    assert board.score('Fi ally', Location(5, 10), VERTICAL) == 18


def test_verify_legality_rejects_one_letter_word(board):
    with pytest.raises(ValueError):
        board.verify_legality('a', CENTER, HORIZONTAL, 'a')


def test_verify_legality_rejects_tiles_not_in_hand(board):
    with pytest.raises(ValueError):
        board.verify_legality('cat', CENTER, HORIZONTAL, 'abcdefg')


def test_verify_legality_rejects_word_overlapping_existing_tile(board):
    board.place_word('horn', CENTER, HORIZONTAL)
    with pytest.raises(ValueError):
        board.verify_legality('bag', Location(6, 8), VERTICAL, 'abcdefg')


def test_verify_legality_rejects_gap_in_middle_of_word(board):
    board.place_word('horn', CENTER, HORIZONTAL)
    with pytest.raises(ValueError):
        board.verify_legality('a c', Location(6, 6), HORIZONTAL, 'abcdefg')


def test_verify_legality_rejects_word_abutting_existing_tiles(board):
    board.place_word('horn', CENTER, HORIZONTAL)
    with pytest.raises(ValueError):
        board.verify_legality('bag', Location(7, 9), HORIZONTAL, 'abcdefg')


def test_verify_legality_rejects_word_beyond_edge_of_board(board):
    board.place_word('horn', CENTER, HORIZONTAL)
    with pytest.raises(ValueError):
        board.verify_legality('absolve', Location(6, 10), HORIZONTAL, 'absolve')


def test_verify_legality_rejects_isolated_word(board):
    board.place_word('horn', CENTER, HORIZONTAL)
    with pytest.raises(ValueError):
        board.verify_legality('bag', Location(5, 8), HORIZONTAL, 'abcdefg')


def test_verify_legality_rejects_misspelled_word(board):
    with pytest.raises(ValueError):
        board.verify_legality('drowzEe', Location(6, 7), VERTICAL, 'drowze_')


def test_verify_legality_rejects_all_spaces(board):
    board.place_word('horn', CENTER, HORIZONTAL)
    with pytest.raises(ValueError):
        board.verify_legality('    ', CENTER, HORIZONTAL, 'abcdefg')


def test_verify_legality_accepts_valid_words(board):
    # From traditional rules example
    board.verify_legality('horn', Location(7, 4), HORIZONTAL, 'horn')
    board.place_word('horn', Location(7, 4), HORIZONTAL)
    board.verify_legality('fa m', Location(5, 6), VERTICAL, 'fam')
    board.place_word('fa m', Location(5, 6), VERTICAL)
    board.verify_legality('paste', Location(9, 4), HORIZONTAL, 'paste')
    board.place_word('paste', Location(9, 4), HORIZONTAL)
    board.verify_legality(' ob', Location(8, 6), HORIZONTAL, 'ob')
    board.place_word(' ob', Location(8, 6), HORIZONTAL)
    board.verify_legality('Bit', Location(10, 3), HORIZONTAL, 'it_')
    board.place_word('Bit', Location(10, 3), HORIZONTAL)


def test_remove_tiles_removes_correct_tiles(board):
    hand = list('ca__bda')
    board.remove_tiles('Ba ', hand)
    assert hand == list('c_bda')
