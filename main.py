import os
import random
from augmentation_strategy.strategy_factory import strategy_factory
from augmentation_strategy.BFS import BFS
from graph.Graph import Graph
from graph.GraphGenerator import GraphGenerator
from definitions import DATA_DIR, RESULTS_FILE, SIMULATION1_DIR, SIMULATION2_DIR
from FordFulkerson import FordFulkerson
from utilities.Metrics import Metrics
from utilities.Logger import Logger
import argparse


def print_metrics(max_flow, length_longest_acyclic_path, metrics):
    print("METRICS")
    print("-------")
    print(f"Max flow: {max_flow}")
    print(f"Longest acyclic path length: {length_longest_acyclic_path}")
    print(f"Number paths: {metrics.get_number_paths()}")
    print(f"Mean length: {metrics.get_mean_length()}")
    print(f"MPL: {metrics.get_mean_proportional_length()}")
    print(f"Total edges: {metrics.get_total_edges()}")
    print("\n")


def main():
    ford_fulkerson_header = """
    ------------------------------------
    Ford-Fulkerson Algorithm
    ------------------------------------
    """

    print(ford_fulkerson_header)

    parser = argparse.ArgumentParser(description='Find the max flow using the Ford-Fulkerson algorithm.')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--file', type=str, help='Path to the file containing the graph data.')
    group.add_argument('--generate', action='store_true', help='Generate a new random graph.')
    group.add_argument('--run_simulation1', action='store_true', help='Run predefined simulation 1.')
    group.add_argument('--run_simulation2', action='store_true', help='Run predefined simulation 2.')

    parser.add_argument('--strategy', choices=['bfs', 'sap', 'dfslike', 'maxcap', 'random'], required=False, type=str.lower, help='Strategy to be used.')

    # Arguments for graph generation
    parser.add_argument('--n', type=int, help='Number of vertices, required if --generate is used.')
    parser.add_argument('--r', type=float, help='Distance, required if --generate is used.')
    parser.add_argument('--upperCap', type=int, help='Upper capacity, required if --generate is used.')

    # Arguments for graph source and sink
    parser.add_argument('--source', type=str, help='Source vertex, required if --file is used.')
    parser.add_argument('--sink', type=str, help='Sink vertex, required if --file is used.')

    parser.add_argument('--result_file', type=str, default=RESULTS_FILE, help='File to store results. Default is "results/results.csv".')

    # Parse arguments
    args = parser.parse_args()

    logger = Logger(args.result_file)
    
    # Handle different modes
    if args.run_simulation1 or args.run_simulation2:
        graph_dir = None
        if args.run_simulation1:
            graph_dir = SIMULATION1_DIR
            print("RUNNING SIMULATION 1")
        else:
            graph_dir = SIMULATION2_DIR
            print("RUNNING SIMULATION 2")
        print("\n")
        
        strategies = ["sap", "dfslike", "maxcap", "random"]
        # Code for running simulation 1
        for filename in os.listdir(graph_dir):
            file_path = os.path.join(graph_dir, filename)
            if os.path.isfile(file_path) and filename.endswith('.csv'):
                graph = Graph()
                graph.load_from_csv(file_path)
                if not graph:
                    raise RuntimeError(f"Graph could not be loaded from the file {filename}")
                print("------------------------------------------------------------------")
                print(f"Loading graph from file: {file_path}")
                print("------------------------------------------------------------------")
                source = "0"
                bfs = BFS()
                longest_acyclic_path = bfs.get_longest_acyclic_path(graph, source)
                sink = longest_acyclic_path[-1]
                
                length_longest_acyclic_path = len(longest_acyclic_path)
                total_edges = len(graph.get_edges())
                metrics = Metrics(length_longest_acyclic_path, total_edges)

                for s in strategies:
                    print(f"Selected strategy: {s}")
                    print("--------------------------")
                    strategy = strategy_factory(s)
                    ff = FordFulkerson(strategy=strategy)
                    max_flow = ff.get_flow(graph, source, sink, metrics)
                    print_metrics(max_flow, length_longest_acyclic_path, metrics)

                    logger.write_to_log(graph_name=filename,
                                        source=source,
                                        sink=sink,
                                        strategy=s,
                                        max_flow=max_flow,
                                        longest_acyclic_path_length=length_longest_acyclic_path,
                                        number_paths=metrics.get_number_paths(),
                                        mean_length=metrics.get_mean_length(),
                                        mpl=metrics.get_mean_proportional_length(),
                                        total_edges=total_edges
                                        )
                    metrics.reset()

    elif args.generate or args.file:
        if args.strategy is None:
            parser.error("--generate requires a strategy to be specified.")

        graph = None
        strategy = None
        source = None
        sink = None
        metrics = None

        if args.generate:
            if args.n is None or args.r is None or args.upperCap is None:
                parser.error("--generate requires --n, --r, and --upperCap.")
        
            print(f"Generating a random graph with n={args.n}, r={args.r}, upperCap={args.upperCap}")
            graphGenerator = GraphGenerator(args.n, args.r, args.upperCap)
            graph = graphGenerator.generate()

            source = str(random.randint(0, args.n))
            bfs = BFS()
            longest_acyclic_path = bfs.get_longest_acyclic_path(graph, source)
            sink = longest_acyclic_path[-1]
            length_longest_acyclic_path = len(longest_acyclic_path)
            total_edges = len(graph.get_edges())
            metrics = Metrics(length_longest_acyclic_path, total_edges)

        elif args.file:
            if args.source is None or args.sink is None:
                parser.error("--file requires --source and --sink.")

            print(f"Loading graph from file: {args.file}")
            
            graph = Graph()
            graph.load_from_csv(os.path.join(DATA_DIR, args.file))
            if not graph:
                raise RuntimeError(f"Graph could not be loaded from the file {args.file}")
            
            source = args.source
            bfs = BFS()
            sink = args.sink
            longest_acyclic_path = bfs.get_longest_acyclic_path(graph, source)
            if sink is None:
                sink = longest_acyclic_path[-1]
            
            length_longest_acyclic_path = len(longest_acyclic_path)
            total_edges = len(graph.get_edges())
            metrics = Metrics(length_longest_acyclic_path, total_edges)
        
        print(f"Selected strategy: {args.strategy}")
        strategy = strategy_factory(args.strategy)

        ff = FordFulkerson(strategy=strategy)
        max_flow = ff.get_flow(graph, source, sink, metrics)
        print_metrics(max_flow, length_longest_acyclic_path, metrics)

        logger.write_to_log(graph_name=args.file,
                            source=source,
                            sink=sink,
                            strategy=args.strategy,
                            max_flow=max_flow,
                            longest_acyclic_path_length=length_longest_acyclic_path,
                            number_paths=metrics.get_number_paths(),
                            mean_length=metrics.get_mean_length(),
                            mpl=metrics.get_mean_proportional_length(),
                            total_edges=total_edges
                            )
    

if __name__ == "__main__":
    main()
