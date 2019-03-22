import reprlib
import enum


def onlyElementOf(collection):
    if len(collection) > 1:
        raise ValueError('Expected 1 matching item but found %s'
                         % reprlib.repr([str(item) for item in collection]))
    if len(collection) == 0:
        return None

    return collection[0]


def enum_super(name):
    def add_enum(self, *args):
        cls.enum_values[self.name] = self

    cls = type(name, (), {
        '__init__': add_enum,
    })
    cls.of = lambda x: x if isinstance(x, cls) else cls.enum_values[x]
    cls.enum_values = {}
    return cls
