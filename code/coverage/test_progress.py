from progress import calculate_progress


def test_progress():
    total = 50
    for i in range(total + 1):
        expected = i / total
        actual = calculate_progress(i, total, False)
        assert actual == expected


def test_progress_percentage():
    total = 50
    for i in range(total + 1):
        expected = i / total * 100
        actual = calculate_progress(i, total, True)
        assert actual == expected
