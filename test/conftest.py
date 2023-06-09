import os
from dotenv import load_dotenv
import pytest
from test.utils import get_all_files_from_folder

load_dotenv()

# directory = os.getenv("SUT_PETERSON_DIR")
directory = os.getenv("SUT_TEPUK_DIR")
location = directory.replace("\\test", "")

linked_service = "linkedService"
dataset = "dataset"
pipeline = "pipeline"
factory = "factory"
trigger = "trigger"
integration_runtime = "integrationRuntime"
managed_virtual_network = "managedVirtualNetwork"

folders = [
    location + "\\" + linked_service,
    location + "\\" + dataset,
    location + "\\" + pipeline,
    location + "\\" + factory,
    location + "\\" + integration_runtime,
    location + "\\" + trigger,
    location + "\\" + managed_virtual_network,
]


@pytest.fixture
def managed_virtual_network_files():
    managed_virtual_network_files = get_all_files_from_folder(
        location + "\\" + managed_virtual_network
    )
    return managed_virtual_network_files


@pytest.fixture
def integration_runtime_files():
    integration_runtime_files = get_all_files_from_folder(
        location + "\\" + integration_runtime
    )
    return integration_runtime_files


@pytest.fixture
def factory_files():
    factory_files = get_all_files_from_folder(location + "\\" + factory)
    return factory_files


@pytest.fixture
def trigger_files():
    trigger_files = get_all_files_from_folder(location + "\\" + trigger)
    return trigger_files


@pytest.fixture
def pipeline_files():
    pipeline_files = get_all_files_from_folder(location + "\\" + pipeline)
    return pipeline_files


@pytest.fixture
def dataset_files():
    dataset_files = get_all_files_from_folder(location + "\\" + dataset)
    return dataset_files


@pytest.fixture
def linked_service_files():
    linked_service_files = get_all_files_from_folder(location + "\\" + linked_service)
    return linked_service_files


@pytest.fixture
def tepuk_sut():
    return "SUT_TEPUK_DIR"


@pytest.fixture
def peterson_sut():
    return "SUT_PETERSON_DIR"
