from enum import Enum

class Centrality(Enum):
    """A list of centrality algorithms."""

    BETWEENNESS = "betweenness_centrality"
    CLOSENESS = "closeness_centrality"
    DEGREE = "degree"
