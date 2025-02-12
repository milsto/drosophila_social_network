"""Protocol to run all necessary stages of the pipeline in a single step.

TODO: Currently executed directly when importing, should implement main or encapsualte in functions.
TODO: File names of the protocol stages start with number, so they can not be variables.
"""
import importlib

importlib.import_module("0_0_preproc_data")
importlib.import_module("0_1_get_path_features")
importlib.import_module("0_2_distances_between_flies_matrix")
importlib.import_module("1_0_undirected_singleedge_graph")
importlib.import_module("2_0_get_graph_measures_table")
importlib.import_module("2_1_get_fly_distance_traveled")
importlib.import_module("3_1_distance_traveled_plots")
importlib.import_module("3_2_population_retention_heatmap")
