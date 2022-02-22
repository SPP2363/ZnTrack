import pytest

from zntrack import utils, zn
from zntrack.core import ZnTrackOption


def test_zn_outs_error():
    with pytest.raises(ValueError):

        class ExampleOutsDefault:
            node_name = "test"
            parameter = zn.outs(default_value="Lorem Ipsum")


class CustomZnTrackOption(ZnTrackOption):
    def get_data_from_files(self, instance):
        return "Lorem Ipsum"


class ExampleParams:
    node_name = "test"
    is_loaded = True  # here we want to test the load from file
    parameter = CustomZnTrackOption()


class ExampleParamsDefault:
    node_name = "test"
    is_loaded = False  # here we test load from default
    parameter = zn.params(default_value="Lorem Ipsum")


@pytest.mark.parametrize("cls", [ExampleParams, ExampleParamsDefault])
def test_ExampleParamsDefault(cls):
    obj = cls()
    with pytest.raises(KeyError):
        _ = obj.__dict__["parameter"]
    assert obj.parameter == "Lorem Ipsum"
    assert obj.__dict__["parameter"] == "Lorem Ipsum"


class ExampleMethod:
    def run(self):
        return 42


class ExampleNode:
    node_name = None
    module = "module"
    method = zn.Method(ExampleMethod())


def test_method_filename():
    assert ExampleNode.method.get_filename(ExampleNode()) == (
        utils.Files.params,
        utils.Files.zntrack,
    )