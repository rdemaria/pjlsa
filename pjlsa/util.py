import reprlib


def onlyElementOf(collection):
    if len(collection) > 1:
        raise ValueError('Expected 1 matching item but found %s'
                         % reprlib.repr([str(item) for item in collection]))
    if len(collection) == 0:
        return None

    return collection[0]
