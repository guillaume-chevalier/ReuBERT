import pytest

from src.domain.interaction.interaction_state import InteractionState


def test_can_create_interaction_state():
    # Note: the test method name must start by "test_".
    _is = InteractionState()
    assert isinstance(_is, InteractionState)


if __name__ == "__main__":
    pytest.main(__file__)
