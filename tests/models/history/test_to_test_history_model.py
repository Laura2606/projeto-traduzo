from typing import Callable
from unittest.mock import patch

import pytest
from pytest_dependency import (
    assert_fails_with_broken_asset,
    get_skip_markers,
    get_test_assessment_configs,
    run_pytest_quietly,
)

try:
    from src.models.history_model import HistoryModel  # specific
    from tests.models.history import mocks  # specific
except ImportError as error:
    raise NotImplementedError(error)
from tests.models.history import test_history_model  # specific

TA_CFG = get_test_assessment_configs(
    HistoryModel,
    mocks,
    test_history_model,
)

pytestmark = get_skip_markers(TA_CFG)


@pytest.mark.dependency()
def test_students_sanity_check():
    return_code = run_pytest_quietly([TA_CFG.STUDENT_TEST_FILE_PATH])

    if return_code != pytest.ExitCode.OK:
        pytest.skip(
            f"Seus testes em {TA_CFG.STUDENT_TEST_FILE_PATH} "
            "ainda não estão passando! "
            "Verifique-os e tente novamente."
        )


@pytest.mark.dependency(depends=["test_students_sanity_check"])
@pytest.mark.parametrize(
    "broken_asset",
    TA_CFG.BROKEN_ASSETS_LIST,
)
def test_assess_students_history_model(broken_asset: Callable):
    with patch(TA_CFG.PATCH_TARGET, broken_asset):
        return_code = run_pytest_quietly([TA_CFG.STUDENT_TEST_FILE_PATH])

    if return_code == pytest.ExitCode.TESTS_FAILED:
        assert_fails_with_broken_asset(
            broken_asset, pytest.ExitCode.TESTS_FAILED, TA_CFG
        )

    assert_fails_with_broken_asset(broken_asset, return_code, TA_CFG)


@pytest.mark.dependency(
    depends=["test_assess_students_history_model"], include_all_instances=True
)
def test_assess_students_history_model_final():
    pass
