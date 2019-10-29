from traitlets import (
    Unicode, Enum, Instance, Union, Float, Int, List, Tuple, Dict,
    Undefined, Bool, Any
)

from .ReactWidget import ReactWidget
from ipywidgets import DOMWidget
from ipywidgets.widgets.widget import widget_serialization


class ExpansionPanel(ReactWidget):

    _model_name = Unicode('ExpansionPanelModel').tag(sync=True)

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

    default_expanded = Bool(None, allow_none=True).tag(sync=True)

    disabled = Bool(None, allow_none=True).tag(sync=True)

    expanded = Bool(None, allow_none=True).tag(sync=True)

    square = Bool(None, allow_none=True).tag(sync=True)

    Transition_component = Unicode(None, allow_none=True).tag(sync=True)

    Transition_props = Dict(default_value=None, allow_none=True).tag(sync=True)

    component = Unicode(None, allow_none=True).tag(sync=True)

    elevation = Float(None, allow_none=True).tag(sync=True)


__all__ = ['ExpansionPanel']
