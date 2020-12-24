
import torchtext.data as data

class Dataset(data.Dataset):

    @staticmethod
    def sort_key(ex):
        return len(ex.text)