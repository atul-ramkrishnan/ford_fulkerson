import os
import argparse
from graph.GraphGenerator import GraphGenerator
from definitions import DATA_DIR


parser = argparse.ArgumentParser(description='Generate random graphs given values of n, r and upperCap.')
parser.add_argument('--n', type=int, required=True, help='Number of vertices')
parser.add_argument('--r', type=float,required=True, help='Distance')
parser.add_argument('--upperCap', type=int, required=True, help='Upper capacity')
parser.add_argument("--file", type=str, required=True, help="File name")

args = parser.parse_args()

graphGenerator = GraphGenerator(args.n, args.r, args.upperCap)
graph = graphGenerator.generate()
graph.save_as_csv(os.path.join(DATA_DIR, args.file))