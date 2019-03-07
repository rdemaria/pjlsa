from .jpype_lsa import *
import typing, datetime


def toJavaDate(t):
    Date = java.util.Date
    if isinstance(t, str):
        return java.sql.Timestamp.valueOf(t)
    elif isinstance(t, datetime.datetime):
        return java.sql.Timestamp.valueOf(t.strftime('%Y-%m-%d %H:%M:%S.%f'))
    elif t is None:
        return None
    elif isinstance(t, Date):
        return t
    else:
        return Date(int(t * 1000))


def toJavaList(lst):
    res = java.util.ArrayList()
    if isinstance(lst, typing.List) or isinstance(lst, typing.Set) or isinstance(lst, typing.Tuple):
        for item in lst:
            res.add(item)
    elif isinstance(lst, java.util.Collection):
        res.addAll(lst)
    else:
        res.add(lst)
    return res


def setupLog4j(logLevel):
    log4j = org.apache.log4j
    if log4j.BasicConfigurator is not None and callable(log4j.BasicConfigurator.configure):
        log4j.BasicConfigurator.configure()
    if logLevel is not None:
        log4j.Logger.getRootLogger().setLevel(log4j.Level.toLevel(logLevel))
    else:
        log4j.Logger.getRootLogger().setLevel(log4j.Level.WARN)


def toAccelerator(accelerator):
    Accelerator = cern.accsoft.commons.domain.Accelerator
    CernAccelerator = cern.accsoft.commons.domain.CernAccelerator
    if isinstance(accelerator, Accelerator):
        return accelerator
    else:
        try:
            return CernAccelerator.valueOf(accelerator.upper())
        except jpype.JavaException:
            cernAccelerators = [str(a) for a in cern.accsoft.commons.domain.CernAccelerator.values()]
            raise ValueError('"%s" is not a valid accelerator. Supported accelerators = [%s]'
                             % (accelerator, ', '.join(cernAccelerators)))
