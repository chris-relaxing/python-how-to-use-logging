#-------------------------------------------------------------------------------
# Name:         how_to_use_logging.py
# Purpose:      How to use the logging module to send print statements to both
#               the console and a log file at the same time. This code example
#               was created for the logging tutorial on the Python Portal.
#               Created with Python 2.7.5
#
# Author:       Chris Nielsen (chris.relaxing@gmail.com)
# Created:      Feb. 6, 2015
#-------------------------------------------------------------------------------

import logging
import inspect
import datetime

# ---------------------------------

def log_handlers(file_level, console_level = None):
    function_name = inspect.stack()[1][3]
    logger = logging.getLogger(function_name)
    logger.setLevel(logging.DEBUG) #By default, DEBUG logs all messages

    #log_name = 'Output_log_' + getDate() + '.log'
    log_name = 'Output_log_' + getDate() + '_' + getTime() + '.txt'

    # Clear out existing handlers to avoid duplicated data
    logger.handlers = []

    if not logger.handlers:
        if console_level != None:
            ch = logging.StreamHandler() #StreamHandler logs to console
            ch.setLevel(console_level)
            ch_format = logging.Formatter('%(message)s')
            ch.setFormatter(ch_format)
            logger.addHandler(ch)

        #FileHandler logs to log file. mode='w' is optional for overwrite
        fh = logging.FileHandler(log_name.format(function_name), mode='w')
        fh.setLevel(file_level)
        fh_format = logging.Formatter('%(message)s')
        fh.setFormatter(fh_format)
        logger.addHandler(fh)

    return logger

# ---------------------------------

def getDate():
    now = datetime.datetime.now()
    m = now.month
    d = now.day
    y = str(now.year)
    if m < 10:
        m = "0"+str(m)
    else:
        m = str(m)
    if d < 10:
        d = "0"+str(d)
    else:
        d = str(d)
    y = y[2:]
    formatted_date = m+d+y
    return formatted_date

# ---------------------------------

def getTime():
    now = datetime.datetime.now()
    #print now.month, now.day, now.year
    h = now.hour
    m = now.minute
    if h < 10:
        h = "0"+str(h)
    else:
        h = str(h)
    if m < 10:
        m = "0"+str(m)
    else:
        m = str(m)
    formatted_time = h+m
    return formatted_time

# ---------------------------------

def f1():
    global logger
    year = '2015'
    xldate = 41000
    pvid_list = ["19615056", "15612770", "15612771"]

    logger.info("The year is: %s" % (year))
    logger.info("%s %s %s" % (year, xldate, pvid_list))

# ---------------------------------

def main():

    global logger
    logger = log_handlers(logging.INFO, logging.INFO)

    # print a raw string to both the console and the log
    logger.info('Print this string...')
    logger.info('This print statement is going to both the console and the log')

    f1()
    logging.shutdown()

# ---------------------------------
if __name__ == '__main__':
    main()


