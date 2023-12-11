
# COMP 6651 Project
## Ford Fulkerson algorithm

The Maximum flow problem involves finding the maximum amount of "flow" that can be transported from a designated source vertex to a designated sink vertex without violating any capacity constraints. The Ford-Fulkerson algorithm is a greedy algorithm for tackling the maximum flow problem.



## How to run the main script

To run any script, first you need to go the project directory

```bash
  cd ford_fulkerson
```

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
In all the commands, the option `--result_file` is optional. It can be used to specify the name of the csv file where the results are to be saved. By default it is saved in `results/results.csv`

## Additional
The project also includes additional scripts for generating and saving a random graph. It is not required to test the results of the project.

```bash
  python generate_graph.py --n N --r R --upperCap UPPERCAP --file FILENAME.csv
```