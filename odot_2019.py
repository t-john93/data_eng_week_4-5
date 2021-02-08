import pandas as pd
import matplotlib
import urllib3
import math
import csv

filename = '/Users/trevorjohnson/Documents/Portland State/DATA_ENG/lab3/Oregon Hwy 26 Crash Data for 2019 - Crashes on Hwy 26 during 2019.csv'

df = pd.read_csv(filename, low_memory=False)

# ERROR LIST TO WRITE TO LOGFILE/CSV
errorList = {
    'cID_DNE_except': [],
    'vID_DNE_except': [],
    'pID_DNE_except': [],
    'invalid_year_except': [],
    'invalid_month_except': [],
    'invalid_weekday_except': [],
    'crashid_ooo_except': []
}

# TEMP SORTED LIST FOR STORING OUT OF ORDER RECORDS BY CRASH ID
crashIDSortedList = []

# TEMP PREV ROW FOR CHECKING OUT OF ORDER RECORDS BY CRASH ID
prev_crash_ID = -1

# this is my first draft solution. I understand that pandas has functions that can iterate over columns and run
# assertions that way, however in order to validate and resolve in a single iteration, while also being able to
# a log file I thought writing an explicit loop would be a better solution. Otherwise we would loop through the
# dataframe for each validation.

for index, row in df.iterrows():
    # CRASH ID DNE ERR
    try:
        assert(not pd.isnull(row['Crash ID']))
    except (AssertionError, TypeError):
        err = '***CRASH ID DNE EXCEPTION AT ROW %s ***' % index
        err_ctx = { 'index': index, 'error': err, 'row': row }
        errorList['cID_DNE_except'].append(err_ctx)
        pass
    # VEHICLE ID DNE ERR
    try:
        assert(not pd.isnull(row['Vehicle ID']))
    except (AssertionError, TypeError):
        err = '***VEHICLE ID DNE EXCEPTION AT CRASH ID: %s ***' % row['Crash ID']
        err_ctx = { 'index': index, 'error': err, 'row': row }
        errorList['vID_DNE_except'].append(err_ctx)
        pass
    # PARTICIPANT ID DNE ERR
    try:
        assert(not pd.isnull(row['Participant ID']))
    except (AssertionError, TypeError):
        err = '***PARTICIPANT ID DNE EXCEPTION AT CRASH ID: %s ***' % row['Crash ID']
        err_ctx = { 'index': index, 'error': err, 'row': row }
        errorList['pID_DNE_except'].append(err_ctx)
        pass
    # INVALID YEAR ERR
    try:
        assert(row['Crash Year'] == 2019)
    except AssertionError:
        err = '***INVALID CRASH YEAR EXCEPTION AT CRASH ID: %s ***' % row['Crash ID']
        err_ctx = { 'index': index, 'error': err, 'row': row }
        errorList['invalid_year_except'].append(err_ctx)
        pass
    # INVALID MONTH ERR
    try:
        assert(row['Crash Month'] >= 1 and row['Crash Month'] <= 12)
    except AssertionError:
        err = '***INVALID CRASH MONTH EXCEPTION AT CRASH ID: %s ***' % row['Crash ID']
        err_ctx = { 'index': index, 'error': err, 'row': row }
        errorList['invalid_month_except'].append(err_ctx)
        pass
    # INVALID WEEKDAYCODE ERR
    try:
        assert(row['Week Day Code'] >= 1 and row['Week Day Code'] <= 7)
    except AssertionError:
        err = '***INVALID WEEK DAY CODE EXCEPTION AT CRASH ID: %s ***' % row['Crash ID']
        err_ctx = { 'index': index, 'error': err, 'row': row }
        errorList['invalid_weekday_except'].append(err_ctx)
        pass
    # CRASH ID OUT OF ORDER
    try:
        assert(row['Crash ID'] < prev_crash_ID)
    except AssertionError:
        err = '***CRASH ID OUT OF ORDER EXCEPTION AT CRASH ID: %s ***' % row['Crash ID']
        err_ctx = { 'index': index, 'error': err, 'row': row }
        errorList['crashid_ooo_except'].append(err_ctx)
        pass

    prev_crash_ID = row['Crash ID']

# DEBUG
# print(df)
# print(errorList)

print('\n\n\n********    CRASH ID DOES NOT EXIST ERROR    ********\n')
err_records = errorList['cID_DNE_except']
for err in err_records:
    print(err)
    # can write to logfile or csv here

print('\n\n\n********    VEHICLE ID DOES NOT EXIST ERROR    ********\n')
err_records = errorList['vID_DNE_except']
for err in err_records:
    print(err)
    # can write to logfile or csv here

print('\n\n\n********    PARTICIPAND ID DOES NOT EXIST ERROR    ********\n')
err_records = errorList['pID_DNE_except']
for err in err_records:
    print(err)
    # can write to logfile or csv here