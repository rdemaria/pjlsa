from .jpype_lsa import *
import typing

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
        return Date(int(t*1000))

def toJavaList(list):
    res = java.util.ArrayList()
    if isinstance(list, typing.List) or isinstance(list, typing.Set) or isinstance(list, typing.Tuple):
        for item in list:
            res.add(item)
    elif isinstance(list, java.util.Collection):
        res.addAll(list)
    else:
        res.add(list)
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