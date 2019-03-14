from hashlib import sha1


def make_asset_hash(*values):
    return sha1(':'.join(values).encode('utf-8')).hexdigest()
