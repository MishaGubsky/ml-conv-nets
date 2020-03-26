from scipy.io import loadmat


DATA_DIRECTORY = f'Datasets/'


def load_data_from_mat_file(filename):
    filepath = f'{DATA_DIRECTORY}{filename}.mat'
    return loadmat(filepath)
