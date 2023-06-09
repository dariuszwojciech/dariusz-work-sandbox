import os


def get_all_files_from_folder(folder):
    result = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            result.append(file)
    return result


def get_count(data_object, key):
    result = 0
    try:
        result = len(data_object[key])
    except KeyError:
        return None
    return result


def fetch_files(sut, collection):
    return get_all_files_from_folder(os.getenv(sut) + "\\" + collection)
