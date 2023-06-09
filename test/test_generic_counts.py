from dotenv import load_dotenv

import const.adf
from test.testing_utils import assert_count
from test.utils import fetch_files

load_dotenv()


def test_tepuk_counts(tepuk_sut):
    sut = tepuk_sut
    assert_count(fetch_files(sut, const.adf.LINKED_SERVICE), 2)
    assert_count(fetch_files(sut, const.adf.DATASET), 3)
    assert_count(fetch_files(sut, const.adf.INTEGRATION_RUNTIME), 2)
    assert_count(fetch_files(sut, const.adf.PIPELINE), 8)
    assert_count(fetch_files(sut, const.adf.FACTORY), 1)
    assert_count(fetch_files(sut, const.adf.MAPPED_VIRTUAL_NETWORK), 2)
    assert_count(fetch_files(sut, const.adf.TRIGGER), 2)


def test_peterson_counts(peterson_sut):
    sut = peterson_sut
    assert_count(fetch_files(sut, const.adf.LINKED_SERVICE), 8)
    assert_count(fetch_files(sut, const.adf.DATASET), 43)
    assert_count(fetch_files(sut, const.adf.INTEGRATION_RUNTIME), 2)
    assert_count(fetch_files(sut, const.adf.PIPELINE), 22)
    assert_count(fetch_files(sut, const.adf.FACTORY), 1)
    assert_count(fetch_files(sut, const.adf.MAPPED_VIRTUAL_NETWORK), 2)
    assert_count(fetch_files(sut, const.adf.TRIGGER), 1)
