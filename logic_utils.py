def get_range_for_difficulty(difficulty: str):
    # FIXED: ranges were inverted (Hard was narrower than Normal). Range now
    # widens with difficulty: Easy 1-20, Normal 1-50, Hard 1-100.
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 50


def parse_guess(raw: str, low: int = None, high: int = None):
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    # FIXED: out-of-range guesses were accepted. Now rejects values outside the
    # (low, high) bounds for the current difficulty.
    if low is not None and high is not None:
        if value < low or value > high:
            return False, None, f"Enter a number between {low} and {high}."

    return True, value, None


def check_guess(guess, secret):
    # FIXED: hint messages were backwards, and a string secret caused a bad
    # comparison. Now coerces both to int and points toward the secret.
    guess = int(guess)
    secret = int(secret)

    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"

    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
