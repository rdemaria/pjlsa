import reprlib
import enum


def only_element(collection):
    if len(collection) > 1:
        raise ValueError('Expected 1 matching item but found %s'
                         % reprlib.repr([str(item) for item in collection]))
    if len(collection) == 0:
        return None

    return collection[0]


def super_enum(name):
    def add_enum(self, *_):
        if not isinstance(self, enum.Enum):
            raise ValueError('Wrong usage of {0}. Use {0}.of(str) to retrieve an element.'.format(name))
        cls.enum_values[self.name] = self

    def retrieve_element(n):
        if isinstance(n, cls):
            return n
        else:
            try:
                return cls.enum_values[n]
            except KeyError:
                raise ValueError('"{0}" is not a valid {1}. Valid values: [{2}]'
                                 .format(n, name, ",".join(cls.enum_values.keys())))

    cls = type(name, (), {
        '__init__': add_enum,
    })
    cls.of = retrieve_element
    cls.enum_values = {}
    return cls
