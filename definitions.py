import os


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, "data")
SIMULATION1_DIR = os.path.join(DATA_DIR, "simulation1")
SIMULATION2_DIR = os.path.join(DATA_DIR, "simulation2")
RESULTS_DIR = os.path.join(ROOT_DIR, "results")
RESULTS_FILE = os.path.join(RESULTS_DIR, "results.csv")