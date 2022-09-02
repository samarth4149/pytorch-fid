__version__ = '0.2.1'
from .fid_score import compute_statistics_of_dataset, compute_statistics_of_path, get_model, calculate_frechet_distance
__all__ = ['compute_statistics_of_dataset', 'compute_statistics_of_path', 'get_model', 'calculate_frechet_distance']