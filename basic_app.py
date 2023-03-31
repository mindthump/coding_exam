import logging
import pytest


def test_one():
    assert 1 == 1


class App:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)
        logging.debug("A debug message")

    def main(self):
        print("Executing.")
        return 0


if __name__ == "__main__":
    pytest.main()
    # app = App()
    # sys.exit(app.main())
