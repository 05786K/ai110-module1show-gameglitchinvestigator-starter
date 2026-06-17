"""Pytest suite for the Game Glitch Investigator logic.

Covers the four bugs that were fixed in logic_utils.py:
  1. Difficulty levels      -> get_range_for_difficulty
  2. Input validation       -> parse_guess
  3. Accurate hints         -> check_guess
  4. Correct attempts/score -> update_score (fewer attempts == higher score)

Run from the starter folder:  pytest
"""

import os
import sys

import pytest

# logic_utils.py lives one directory up from this test file.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
)


# ---------------------------------------------------------------------------
# 1. Difficulty level
# ---------------------------------------------------------------------------
class TestDifficultyLevel:
    @pytest.mark.parametrize(
        "difficulty, expected",
        [
            ("Easy", (1, 20)),
            ("Normal", (1, 50)),
            ("Hard", (1, 100)),
        ],
    )
    def test_known_difficulties(self, difficulty, expected):
        assert get_range_for_difficulty(difficulty) == expected

    def test_range_widens_with_difficulty(self):
        # The bug was that Hard was narrower (easier) than Normal. The high
        # bound must strictly increase as the game gets harder.
        _, easy_high = get_range_for_difficulty("Easy")
        _, normal_high = get_range_for_difficulty("Normal")
        _, hard_high = get_range_for_difficulty("Hard")
        assert easy_high < normal_high < hard_high

    def test_unknown_difficulty_has_default(self):
        low, high = get_range_for_difficulty("Impossible")
        assert (low, high) == (1, 50)


# ---------------------------------------------------------------------------
# 2. Input validation
# ---------------------------------------------------------------------------
class TestInputValidation:
    @pytest.mark.parametrize("raw", [None, ""])
    def test_empty_input_is_rejected(self, raw):
        ok, value, err = parse_guess(raw)
        assert ok is False
        assert value is None
        assert err == "Enter a guess."

    @pytest.mark.parametrize("raw", ["abc", "12a", "ten", " "])
    def test_non_numeric_input_is_rejected(self, raw):
        ok, value, err = parse_guess(raw)
        assert ok is False
        assert value is None
        assert err == "That is not a number."

    def test_valid_integer_is_parsed(self):
        ok, value, err = parse_guess("15", 1, 20)
        assert ok is True
        assert value == 15
        assert err is None

    def test_float_string_is_truncated_to_int(self):
        ok, value, err = parse_guess("3.9", 1, 20)
        assert ok is True
        assert value == 3

    @pytest.mark.parametrize("raw", ["0", "21", "100"])
    def test_out_of_range_guess_is_rejected(self, raw):
        # Easy range is 1-20; anything outside must be refused.
        ok, value, err = parse_guess(raw, 1, 20)
        assert ok is False
        assert value is None
        assert err == "Enter a number between 1 and 20."

    @pytest.mark.parametrize("raw", ["1", "20"])
    def test_range_boundaries_are_inclusive(self, raw):
        ok, value, err = parse_guess(raw, 1, 20)
        assert ok is True
        assert err is None

    def test_no_range_means_no_range_check(self):
        # Without low/high, range validation is skipped.
        ok, value, err = parse_guess("9999")
        assert ok is True
        assert value == 9999


# ---------------------------------------------------------------------------
# 3. Accurate hints
# ---------------------------------------------------------------------------
class TestAccurateHints:
    def test_correct_guess_wins(self):
        outcome, message = check_guess(42, 42)
        assert outcome == "Win"
        assert message == "🎉 Correct!"

    def test_too_high_points_lower(self):
        # Guessing above the secret must tell the player to go LOWER.
        outcome, message = check_guess(80, 50)
        assert outcome == "Too High"
        assert "LOWER" in message

    def test_too_low_points_higher(self):
        # Guessing below the secret must tell the player to go HIGHER.
        outcome, message = check_guess(20, 50)
        assert outcome == "Too Low"
        assert "HIGHER" in message

    def test_string_secret_is_compared_numerically(self):
        # The old glitch passed the secret as a string, breaking the compare.
        # "9" vs "10" must NOT be judged lexicographically.
        assert check_guess(9, "10") == ("Too Low", "📈 Go HIGHER!")
        assert check_guess(10, "9") == ("Too High", "📉 Go LOWER!")
        assert check_guess(50, "50") == ("Win", "🎉 Correct!")


# ---------------------------------------------------------------------------
# 4. Correct attempts (score reflects the attempt number)
# ---------------------------------------------------------------------------
class TestCorrectAttempts:
    def test_winning_sooner_scores_more(self):
        # Fewer attempts should be worth more points.
        win_first = update_score(0, "Win", attempt_number=1)
        win_later = update_score(0, "Win", attempt_number=4)
        assert win_first > win_later

    def test_win_score_has_a_floor(self):
        # Very late wins must not go below the 10-point floor.
        assert update_score(0, "Win", attempt_number=20) == 10

    def test_wrong_low_guess_loses_points(self):
        assert update_score(50, "Too Low", attempt_number=3) == 45

    def test_unknown_outcome_leaves_score_unchanged(self):
        assert update_score(50, "Pending", attempt_number=2) == 50


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))
