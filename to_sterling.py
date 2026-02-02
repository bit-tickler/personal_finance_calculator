def to_sterling(value: float) -> str:
    if not isinstance(value, (float, int)) or isinstance(value, bool):
        raise ValueError(
            "=========================================================================\n" +
            f"Error: Cannot format provided amount: {value}, amount must be a number.\n" +
            "=========================================================================\n"
        )
    return f"£{value:.2f}"
