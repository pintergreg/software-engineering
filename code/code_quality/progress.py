def calculate_progress(finished: int, total: int, as_percentage: bool) -> float:
    progress = finished / total

    if as_percentage:
        return progress * 100
    else:
        return progress


def calculate_progress_2(
    finished: int, total: int, as_percentage: bool, foo: bool
) -> float:
    progress = finished / total

    if as_percentage and foo:
        return progress * 100
    else:
        return progress
