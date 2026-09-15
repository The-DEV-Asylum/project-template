from dev_asylum_project.core import experiment


def test_experiment_doubles_input() -> None:
    assert experiment(21) == 42


def test_experiment_handles_zero() -> None:
    assert experiment(0) == 0
