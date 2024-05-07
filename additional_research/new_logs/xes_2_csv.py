import pm4py

log = pm4py.read_xes('Hospital_log.xes')
pd = pm4py.convert_to_dataframe(log)
pd.to_csv('Hospital_log.csv')