
# COMP 6651 Project
## Ford Fulkerson algorithm

The Maximum flow problem involves finding the maximum amount of "flow" that can be transported from a designated source vertex to a designated sink vertex without violating any capacity constraints. The Ford-Fulkerson algorithm is a greedy algorithm for tackling the maximum flow problem.



## How to run the main script

To run any script, first you need to go the project directory

```bash
  cd ford_fulkerson
```

The graph files for simulation 1 and simulation 2 are present in the `data/simulation1` and `data/simulation2` folders respectively.
For convenience, the results in the project report can be replicated by running a single command. Running the below script iterates over all the files pertinent to the simulation and prints out the results in the terminal along with generating a csv file in the results folder.

### Running Simulation 1

```bash
  python -m main --run_simulation1 --result_file RESULT_SIMULATION1.csv
```

### Running Simulation 2

```bash
  python -m main --run_simulation2 --result_file RESULT_SIMULATION2.csv
```

### Running the algorithm on a particular file

Add the csv file of the graph to the data folder.

```bash
  python -m main --file FILENAME --source SOURCE --sink SINK --strategy STRATEGY --result_file RESULT.csv
```

The `--sink` option is optional. If excluded, the program uses BFS to find a longest acyclic path and defines the end node of this longest path as the sink.
The STRATEGY can be one of 5 options -- (bfs, sap, dfslike, maxcap, random)

### Running the algorithm on a randomly created graph

```bash
  python -m main --generate --n N --r R --upperCap UPPERCAP --strategy STRATEGY --result_file RESULT.csv
```

In this case, the source node is selected randomly. The sink node is automatically chosen using BFS like in the previous section. 

### Help

At any time, help on how to run the script can be obtained by running the following command
```bash
  python -m main --help
```

### Note

In all the commands, the option `--result_file` is optional. It can be used to specify the name of the csv file where the results are to be saved. By default it is saved in `results/results.csv`. If the same file is used for multiple runs, the results are appended to the end of the csv file. The file is not overwritten.

## Additional

The project also includes additional scripts for generating and saving a random graph, and to test the augmenting path algorithms. They are not required to test the results of the project.

### Generate a random graph

```bash
  python generate_graph.py --n N --r R --upperCap UPPERCAP --file FILENAME.csv
```

### Test the correctness of the augmenting path algorithms
 The file used for testing is test_graph.csv. Note that this test not include all the graphs and tests that were used for testing but is just presented here for clarity.

```bash
  python test_strategy.py
```
