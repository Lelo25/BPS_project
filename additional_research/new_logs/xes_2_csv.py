import pm4py

log = pm4py.read_xes(r'additional_research\new_logs\Hospital_log.xes.gz')
pd = pm4py.convert_to_dataframe(log)
pd.to_csv(r'additional_research\new_logs\Hospital_log.csv')