import pytest
import os
from src.domain.interaction_state import InteractionState

print(os.getcwd())


def test_can_create_interaction_state():
    # Note: the test method name must start by "test_".
    _is = InteractionState()
    assert isinstance(_is, InteractionState)


if __name__ == "__main__":
    pytest.main(__file__)
