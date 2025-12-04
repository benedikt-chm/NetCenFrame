"""evaluate the specific centrality that shall be used for computation"""
from enum import Enum

class Centrality(Enum):
    """A list of centrality algorithms."""

    # BETWEENNESS = "betweenness_centrality"
    BETWEENNESS = "betweenness"
    CLOSENESS = "closeness"
    DEGREE = "degree"
    # CLOSENESS = "closeness_centrality"
