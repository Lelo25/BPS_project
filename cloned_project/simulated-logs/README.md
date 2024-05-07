Datasets and files used in the evaluation of the paper "Can I Trust My Simulation Model? Measuring the Quality of Business Process Simulation Models", where:
- `BPS-models/`: folder containing the BPS models used in the evaluation (the BPS models discovered by ServiceMiner are not included due to privacy reasons).
  - The BPS models discovered by SIMOD are composed of _i)_ a BPMN file with the process model structure, and _ii)_ a JSON file with the parameters of the simulation. These files correspond to the format of Prosimos simulation engine (https://prosimos.cloud.ut.ee/).
  - The BPS models of the Loan Application process are composed of a BPMN file with both the process model structure and parameters, corresponding to the format of the BIMP simulator used in APROMORE (https://apromore.com/).
- `measures/`: folder containing the distance values of each measure reported in the paper.
- `original-event-logs/`: folder containing the (train and test) event logs used in the evaluation.
- `simulated-logs/`: folder containing the simulated logs evaluated in the paper (synthetic, SIMOD, and ServiceMiner).
- `ComputeLogDistance.py`: script to compute the distance measures proposed in the paper.

`ComputeLogDistance.py` example of use:

Run `python ComputeLogDistance.py -cfld test_event_log.csv.gz simulated_logs/` to compute all distance measures proposed in the publication.

The flag `-cfld` is optional, due to the high computational complexity of the CFLD measure.

*WARNING*: set the column names of each log accordingly (where `log_1_ids` are the IDs of the test log, and `log_2_ids` the IDs of the simulated logs). Examples:

```python
# Column IDs for the (train/test) real-life logs, and the SIMOD simulated logs.
EventLogIDs(
    case='case_id',
    activity='activity',
    start_time='start_time',
    end_time='end_time',
    resource='resource'
)

# Column IDs for the Loan Application simulated logs.
EventLogIDs(
    case='case_id',
    activity='activity',
    start_time='Start_Time',
    end_time='End_Time',
    resource='resource'
)

# Column IDs for the ServiceMiner simulated logs.
EventLogIDs(
    case='case_id',
    activity='Activity',
    start_time='start_time',
    end_time='end_time',
    resource='Resource'
)
```