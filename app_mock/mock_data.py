def generate_mock_data(count: int):
    return {
        "name": count**2
    }


def generate_and_hit(count: int, output_location: str):
    return {
        'count': count,
        'output_location': output_location
    }
