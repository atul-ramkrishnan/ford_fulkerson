import csv
import os
from datetime import datetime
from definitions import RESULTS_DIR


class Logger():
    def __init__(self, log_file):
        self.log_file = os.path.join(RESULTS_DIR, log_file)
        if not os.path.exists(RESULTS_DIR):
                os.mkdir(RESULTS_DIR)
        if not os.path.isfile(self.log_file):
            with open(self.log_file, 'x', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['Timestamp', 'File', 'source', 'sink', 'strategy', 'max_flow', 'longest_acyclic_path', 'number_paths', 'mean_length', 'MPL', 'total_edges'])
   

    def write_to_log(self, *, source, sink, strategy, max_flow, longest_acyclic_path_length, number_paths, mean_length, mpl, total_edges, graph_name=None, n=None, r=None, upperCap=None):
        with open(self.log_file, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            row = []
            row.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            row.append('N/A' if graph_name is None else graph_name)
            row.append(source)
            row.append(sink)
            row.append(strategy)
            row.append(max_flow)
            row.append(longest_acyclic_path_length)
            row.append(number_paths)
            row.append(round(mean_length, 3))
            row.append(round(mpl, 3))
            row.append(total_edges)

            writer.writerow(row)
