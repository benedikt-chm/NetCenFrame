# Python package for the analysis of complex networks

is it a fork? is it a re-implementation?
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
- parallel_active:  default is True; to deactivate nx-parallel
  - can be used if you've got your own parallel settings using joblib (only 
available for some of the NetworkX 
    algorithms)
- n_jobs: default is 3; 

### usage
is then a function call similar to 
```python
netcenframe.compute_centrality(\$graph, BETWEENNESS, True, 7)
```
which will then compute the graph measure betweenness centrality
via the library NetworkX and return a pandas DataFrame which is 
already sorted and the computed centrality values are (for this specific
call) re-scaled. At the same time the returned dataframe is also saved as
in CSV format for later usage, for example in other programs.
