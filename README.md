# Python package for the analysis of complex networks

Is it a fork? Is it a re-implementation?
I don't know!
What I do know is that this project uses for the implementations
the algorithms from the projects [NetCenLib](https://github.com/damianfraszczak/netcenlib) and [NetworkX](https://github.com/networkx/networkx).
This project also attempts to have the for NetworkX configurable
speed-up options pre-configured.

This project is for the most part an extension to NetCenLib
and therefore uses the same structure

The aim is to simplify the analysis step by returning an optionally
sorted and/or with the computed values re-scaled pandas DataFrame.

### Installation
```pip install netcenframe```

### parameters


### configuration
To configure the library, there is a `netcenframe.centrality.configure()` functionality
where settings can be passed to for the duration of the program's runtime
- sort: default is True
    - sorts the returned dataframe from highest to lowest centrality value
The default settings need to be applied with a call to `netcenframe.centrality.configure()`
 - They aren't automatically applied because some people would like to use their own parallel settings.



Calls to compute centralities looks like the examples below, in which the
graph measure betweenness centrality will be computed
via the library NetworkX and return a pandas DataFrame which is
already sorted. Before a dataframe is returned, the data is saved
as a file in CSV format for later usage, for example in other programs.



### Two ways of calling functionalities in the library
#### example usage with imports and configuration:
```python
# imports for netcenframe to make it easier to use
from netcenframe.centrality import compute_centrality as compute
from netcenframe.centrality import configure
from netcenframe.taxonomies.Centrality import BETWEENNESS, CLOSENESS, DEGREE

configure()
sorted_df = compute(/$graph, BETWEENNESS)
```

#### example without imports
```python
import netcenframe
# apply config:
netcenframe.centrality.configure()
# run centrality
sorted_df = netcenframe.centrality.compute_centrality(/$graph, netcenframe.taxonomies.Centrality.BETWEENNESS)
```
