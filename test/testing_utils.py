def assert_count(expected, actual):
    print(f"Expected: {len(expected)}; Actual: {actual}\n")
    assert len(expected) == actual
