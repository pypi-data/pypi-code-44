from traitlets import (
    Unicode, Enum, Instance, Union, Float, Int, List, Tuple, Dict,
    Undefined, Bool, Any
)

from .ReactWidget import ReactWidget
from ipywidgets import DOMWidget
from ipywidgets.widgets.widget import widget_serialization


class FormGroup(ReactWidget):

    _model_name = Unicode('FormGroupModel').tag(sync=True)

    children = Union([
        Union([
        Unicode(),
        Instance(DOMWidget)
    ], default_value=None),
        List(Union([
        Unicode(),
        Instance(DOMWidget)
    ], default_value=None))
    ], default_value=None, allow_none=True).tag(sync=True, **widget_serialization)

    classes = Dict(default_value=None, allow_none=True).tag(sync=True)

    class_name = Unicode(None, allow_none=True).tag(sync=True)

    row = Bool(None, allow_none=True).tag(sync=True)


__all__ = ['FormGroup']
