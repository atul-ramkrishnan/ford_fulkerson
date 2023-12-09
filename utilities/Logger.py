import csv
import os
from datetime import datetime


class Logger():
    def __init__(self, log_file):
        self.log_file = log_file
        if not os.path.isfile(log_file):
            os.makedirs(os.path.dirname(log_file), exist_ok=True)
            with open(self.log_file, 'x', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Timestamp', 'File', 'n', 'r', 'upperCap', 'source', 'sink', 'strategy', 'max_flow', 'longest_acyclic_path', 'number_paths', 'mean_length', 'MPL', 'total_edges'])
   

    def write_to_log(self, *, source, sink, strategy, max_flow, longest_acyclic_path_length, number_paths, mean_length, mpl, total_edges, graph_name=None, n=None, r=None, upperCap=None):
        with open(self.log_file, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            row = []
            row.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            row.append('N/A' if graph_name is None else graph_name)
            row.append('N/A' if n is None else n)
            row.append('N/A' if r is None else r)
            row.append('N/A' if upperCap is None else upperCap)
            row.append(sink)
            row.append(source)
            row.append(strategy)
            row.append(max_flow)
            row.append(longest_acyclic_path_length)
            row.append(number_paths)
            row.append(mean_length)
            row.append(mpl)
            row.append(total_edges)

            writer.writerow(row)
