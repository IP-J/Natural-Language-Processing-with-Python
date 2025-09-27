import pickle

unique_cases_file = 'unique_cases_dict.pickle'

with open(unique_cases_file, 'rb') as handle:
    unique_cases_folders = pickle.load(handle)
