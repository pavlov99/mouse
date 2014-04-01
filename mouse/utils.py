import collections
import string


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(
                *args, **kwargs)
        return cls._instances[cls]


class FrozenDict(collections.Mapping):

    """ Immutable dict."""

    def __init__(self, *args, **kwargs):
        self._d = dict(*args, **kwargs)
        self._hash = None

    def __iter__(self):
        return iter(self._d)

    def __len__(self):
        return len(self._d)

    def __getitem__(self, key):
        return self._d[key]

    def __hash__(self):
        if self._hash is None:
            self._hash = 0
            for key, value in self.iteritems():
                self._hash ^= hash(key)
                self._hash ^= hash(value)
        return self._hash

    def __str__(self):
        return str(dict(self.iteritems()))

    def __repr__(self):
        return "<FrozenDict: %s>" % repr(dict(self.iteritems()))


def get_string_variables(s):
    """ Return variables to be substituted from string.

    :param str: s
    :return generator:

    """
    return (x[1] for x in string.Formatter().parse(s) if x[1])


def get_string_kwargs(s):
    """ Return kwargs variables from string."""
    return (x for x in get_string_variables(s) if not x.isdigit())


def get_partly_formated_string(s, kwargs):
    """ Format string partly."""
    return s.format(**{
        kw: kwargs.get(kw) if kw in kwargs else "{" + str(kw) + "}"
        for kw in get_string_kwargs(s)
    })


def namedtuple_as_dict(obj):
    return {
        k: [namedtuple_as_dict(x) for x in v]
        if isinstance(v, list) else v for k, v in obj._asdict().items()
    }


class classproperty(property):
    def __get__(self, obj, type_):
        return self.fget.__get__(None, type_)()
