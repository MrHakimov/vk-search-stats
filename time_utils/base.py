from datetime import datetime, timezone


def current_time_in_seconds() -> int:
    return int(datetime.now(tz=timezone.utc).timestamp())  # seconds


def hours_to_seconds(hours: float) -> int:
    return int(hours * 60 * 60)
