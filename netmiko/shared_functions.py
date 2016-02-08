import sys


def write_bytes(out_data):
    '''Write Python2 and Python3 compatible byte stream'''
    if sys.version_info[0] >= 3:
        if isinstance(out_data, type(u'')):
            return out_data.encode('ascii', 'ignore')
        elif isinstance(out_data, type(b'')):
            return out_data
    else:
        if isinstance(out_data, type(u'')):
            return out_data.encode('ascii', 'ignore')
        elif isinstance(out_data, type('')):
            return out_data
    msg = "Invalid value for out_data neither unicode nor byte string: {0}".format(out_data)
    raise ValueError(msg)
