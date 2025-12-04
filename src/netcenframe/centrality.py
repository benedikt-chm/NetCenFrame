"""starts computation of centrality"""
import networkx as nx
import pandas as pd
import netcenframe.algorithms as ncf_algos
from netcenframe.taxonomies import Centrality
import netcenframe.configuration as ncf_cfg


def compute_centrality(network: nx.Graph, centrality: Centrality,
                       *args, **kwargs) -> pd.DataFrame:

    """
    Compute centrality measure for a give network

    """
    centrality_function_name: str = f"{centrality.value.lower()}_centrality"
    nxp_config = nx.config.backends.parallel
    nxp_config.active = ncf_cfg.Config.parallel_active
    nxp_config.n_jobs = ncf_cfg.Config.n_jobs
    nxp_config.verbose = 50

    # centrality - computation
    network_dict: dict = getattr(ncf_algos, centrality_function_name)(network, *args, **kwargs)
    network_df: pd.DataFrame = pd.DataFrame(list(network_dict.items()),
                                            columns=['node', centrality])
    if ncf_cfg.Config.sort:
        network_df.sort_values(by=[centrality], axis=0, ascending=True, inplace=True)
    network_df.to_csv(centrality.value + '.csv')
    return network_df


def configure(parallel_active: bool = True, relativize: bool = True,
              n_jobs: int = 3, sort: bool = True) -> None:
    """function to configure the library"""
    # global ncf_cfg
    ncf_cfg.Config.parallel_active = parallel_active
    ncf_cfg.Config.n_jobs = n_jobs
    ncf_cfg.Config.sort = sort
    ncf_cfg.Config.relativize = relativize

    nxp_config = nx.config.backends.parallel
    nxp_config.active = parallel_active
    nxp_config.n_jobs = n_jobs


def test_config():
    """ testing, whether configuration was importatet (übernommen) successfully """
    # global ncf_cfg
    print("parallel is active?: ", ncf_cfg.Config.parallel_active)
    print("n_jobs in netcenframe: ", ncf_cfg.Config.n_jobs)
    print("parallel in NX: ", nx.config.backends.parallel.active)
    print("number of jobs: ", nx.config.backends.parallel.n_jobs)
    print("will sort df?: ", ncf_cfg.Config.sort)
