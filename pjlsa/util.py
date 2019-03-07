from .jpype_lsa import *
import typing
from datetime import datetime
import reprlib


def setupLog4j(logLevel):
    log4j = org.apache.log4j
    if log4j.BasicConfigurator is not None and callable(log4j.BasicConfigurator.configure):
        log4j.BasicConfigurator.configure()
    if logLevel is not None:
        log4j.Logger.getRootLogger().setLevel(log4j.Level.toLevel(logLevel))
    else:
        log4j.Logger.getRootLogger().setLevel(log4j.Level.WARN)


def onlyElementOf(collection):
    if len(collection) > 1:
        raise ValueError('Expected 1 matching item but found %s'
                         % reprlib.repr([str(item) for item in collection]))
    if len(collection) == 0:
        return None

    return collection[0]

def toJavaDate(value):
    Date = java.util.Date
    if isinstance(value, str):
        return java.sql.Timestamp.valueOf(value)
    elif isinstance(value, datetime):
        return java.sql.Timestamp.valueOf(value.strftime('%Y-%m-%d %H:%M:%S.%f'))
    elif value is None:
        return None
    elif isinstance(value, Date):
        return value
    else:
        return Date(int(value * 1000))


def toJavaList(value):
    res = java.util.ArrayList()
    if isinstance(value, typing.List) or isinstance(value, typing.Set) or isinstance(value, typing.Tuple):
        for item in value:
            res.add(item)
    elif isinstance(value, java.util.Collection):
        res.addAll(value)
    else:
        res.add(value)
    return res


def toAccelerator(value):
    Accelerator = cern.accsoft.commons.domain.Accelerator
    CernAccelerator = cern.accsoft.commons.domain.CernAccelerator
    if isinstance(value, Accelerator):
        return value
    else:
        return toEnum(value, CernAccelerator)


def toEnum(value, enumClass):
    if isinstance(value, enumClass):
        return value
    else:
        try:
            return enumClass.valueOf(value.upper())
        except jpype.JavaException:
            validItems = [str(a) for a in enumClass.values()]
            raise ValueError('"%s" is not a valid %s. Available: [%s]'
                             % (value, enumClass.__javaclass__.getName().split('.')[-1], ', '.join(validItems)))
