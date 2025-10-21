"""starts computation of centrality"""

# import netcenframe.algorithms as ncf_algos
import algorithms as ncf_algos
# from netcenframe.taxonomies import Centrality
from taxonomies import Centrality
import networkx as nx
import pandas as pd


def compute_centrality(network: nx.Graph, centrality: Centrality, relativize: bool, parallel_active: bool = True,
                       n_jobs: int = 3, sort: bool = True
                       *args, **kwargs) -> pd.DataFrame:
    """
    Compute centrality measure for a give network

    """
    centrality_function_name: str = f"{centrality.value.lower()}_centrality"
    nxp_config = nx.config.backends.parallel
    nxp_config.active = parallel_active
    nxp_config.n_jobs = n_jobs
    nxp_config.verbose = 50

    # centrality - computation
    network_dict: dict = getattr(ncf_algos, centrality_function_name)(network, *args, **kwargs)
    network_df: pd.DataFrame = pd.DataFrame(list(network_dict.items()), columns=['node', centrality])
    if sort:
        network_df.sort_values(by=[centrality], axis=0, ascending=True, inplace=True)

    if relativize:
        # centrality_df = getattr(ncf_algos, centrality_function_name)(network, *args, **kwargs)
        total = network_df[centrality.value.lower()].sum()
        return network_df.loc[centrality.value.lower()].apply(lambda x: (x * 100) / total)
    return network_df

