import pytest

from src.domain.interaction_state import InteractionState


def can_create_interaction_state_test():
    # Note: the test method name must end by "_test".
    _is = InteractionState()
    assert isinstance(_is, InteractionState)


if __name__ == "__main__":
    pytest.main(__file__)
