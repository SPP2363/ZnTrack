"""Fields that are used to define Nodes."""
from zntrack.fields import dvc, zn

# Serialized Fields


def outs():
    """Define a Node Output.

    Parameters
    ----------
        data: any
            A data object that is generated by the Node.
            The object is serialized and deserialized by ZnTrack
            and stored in the node working directory.
            see https://dvc.org/doc/command-reference/stage/add#-o
    """
    return zn.outs()


def metrics():
    """Define a Node Metric.

    Parameters
    ----------
        data: dict
            A dictionary that is used by DVC as a metric.
            The object is serialized and deserialized by ZnTrack
            and stored in the node working directory.
            see https://dvc.org/doc/command-reference/stage/add#-M

    """
    return zn.metrics()


def params(*data):
    """Define a Node Parameter.

    Parameters
    ----------
    data: any
        A data object that is used as a parameter.
        Typically, this should be a string or number.
        The object is serialized and deserialized by ZnTrack
        and stored in params.yaml.
        see https://dvc.org/doc/command-reference/stage/add#-p
    """
    return zn.params(*data)


def deps(*data):
    """Define a Node Dependency.

    Parameters
    ----------
    data: any
        A data object that is used as a dependency.
        This can either be a Node or an attribute of a Node.
        It can not be an object that is not part of the Node graph.
        see https://dvc.org/doc/command-reference/stage/add#-d
    """
    return zn.deps(*data)


def plots(*data, **kwargs):
    """Define a Node Plot.

    Parameters
    ----------
    data: pd.DataFrame
        A pandas DataFrame that is used as a plot.
        The object is serialized and deserialized by ZnTrack
        and stored in the node working directory.
        see https://dvc.org/doc/command-reference/stage/add#--plots
    kwargs: dict
        Additional keyword arguments that are used for plotting.

    """
    return zn.plots(*data, **kwargs)


# Path Fields


def outs_path(*path):
    """Define a Node Output.

    Parameters
    ----------
    path: str|Path
        A file or directory that is generated by the Node.
        see https://dvc.org/doc/command-reference/stage/add#-o

    """
    return dvc.outs(*path)


def metrics_path(*path):
    """Define a Node Metric.

    Parameters
    ----------
    path : str|Path
        A file that is used by DVC as a metric, such as *.json
        see https://dvc.org/doc/command-reference/stage/add#-M

    """
    return dvc.metrics(*path)


def params_path(*path):
    """Define a Node Parameter.

    Parameters
    ----------
    path : str|Path
        A file that is used by DVC for reading parameters.
        This includes typically json or yaml files.
        see https://dvc.org/doc/command-reference/stage/add#-p
    """
    return dvc.params(*path)


def deps_path(*path):
    """Define a Node Dependency.

    Parameters
    ----------
    path : str|Path
        A file or directory that is defined as a dependency to the Node.
        see https://dvc.org/doc/command-reference/stage/add#-d

    """
    return dvc.deps(*path)


def plots_path(*path, **kwargs):
    """Define a Node Plot.

    Parameters
    ----------
    path : str|Path
        A file or directory that is defined as a plot to the Node.
        see https://dvc.org/doc/command-reference/stage/add#--plots
    kwargs: dict
        Additional keyword arguments that are used for plotting.
    """
    return dvc.plots(*path, **kwargs)