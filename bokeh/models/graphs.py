from .sources import DataSource, ColumnDataSource

from ..core.has_props import abstract
from ..core.properties import Any, Instance, Seq
from ..model import Model

_DEFAULT_NODE_SOURCE = lambda: ColumnDataSource(data=dict(index=[]))

_DEFAULT_EDGE_SOURCE = lambda: ColumnDataSource(data=dict(start=[], end=[]))

class GraphDataSource(DataSource):
    '''

    '''

    nodes = Instance(ColumnDataSource, default=_DEFAULT_NODE_SOURCE, help="""
    Stuff and things
    """)

    edges = Instance(ColumnDataSource, default=_DEFAULT_EDGE_SOURCE, help="""
    Stuff and things
    """)

@abstract
class LayoutProvider(Model):
    '''

    '''
    pass

class StaticLayoutProvider(LayoutProvider):

    node_x = Seq(Any, default=[], help="""
    stuff and things
    """)

    node_y = Seq(Any, default=[], help="""
    stuff and things
    """)

    edge_xs = Seq(Any, default=[[]], help=""")
    stuff and things
    """)

    edge_ys = Seq(Any, default=[[]], help="""
    stuff and things
    """)
