# Advanced Process Mining Team Project
## University of Mannheim

This repository forms part of an advanced course on process mining at the University of Mannheim, focusing on replicating the findings of the paper ["Can I Trust My Simulation Model? Measuring the Quality of Business Process Simulation Models"](https://link.springer.com/chapter/10.1007/978-3-031-41620-0_2#Bib1).

### Repository Overview

- `additional_research/`: folder containing the code, results and models from additional researches that have been conducted in regards to the paper.
- `cloned_project/`: folder with the cloned repository from the paper. These are the files we worked with during the replication, therefore also fixed files can be found in there.
- `results/`: folder containing the distance values of each measure reported in the **paper** as well as **our** results from the code replication.
- `time_format_correction.ipynb`: pyhton script for correction the time format error for the files of `BPIC_2012_test` and`BPIC_2012_train`. The corrected files can also be found `cloned_project/original-event-logs/`.

#### additonal_research
- `log_replication/`:
- `new_logs/`:

#### cloned_project
- `BPS-models/`: folder containing the BPS models used in the evaluation (the BPS models discovered by ServiceMiner are not included due to privacy reasons).
  - The BPS models discovered by SIMOD are composed of _i)_ a BPMN file with the process model structure, and _ii)_ a JSON file with the parameters of the simulation. These files correspond to the format of Prosimos simulation engine (https://prosimos.cloud.ut.ee/).
  - The BPS models of the Loan Application process are composed of a BPMN file with both the process model structure and parameters, corresponding to the format of the BIMP simulator used in APROMORE (https://apromore.com/).
- `original-event-logs/`: folder containing the (train and test) event logs used in the evaluation.
- `ComputeLogDistance.py`: pyhton script to compute the distance measures proposed in the paper.
- `simulated-logs/`: first folder containing the simulated logs evaluated in the paper (synthetic, SIMOD, and ServiceMiner).

### Usage Instructions

To calculate all distance measures as per the paper's methods, execute for example:

```bash
python ComputeLogDistance.py -cfld cloned_project/original-event-logs/AcademicCredentials_test.csv.gz cloned_project/simulated-logs/AcademicCredentials_SIMOD.csv.gz
```

Switch the `original-event-logs` and `simulated-logs` accordingly to what you want to run (either train or test, either SIMOD or ServiceMiner). 

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

### System Information

The replication experiments were run on these machines:

- Macbook Air M2 8-core CPU 8GB RAM
- Windows 10 Home (64-bit) (10.0, Build 19045), AMD Ryzen 7 2700X Eight-Core Processor (16 CPUs) 3.7GHz, 32GB RAM
-
- HP 15s
- 16GB RAM, 12 core CPU intel i5-12Gen 1.30GHz, Windows 11
-

### Resources
The scripts to reproduce the experiments, the datasets, and the results are publicly available [here](https://zenodo.org/records/7761252).<br>
The GitHub Repository of the full code from the paper can be found [here](https://github.com/AutomatedProcessImprovement/log-distance-measures).

In case a .csv to .gz converter should be needed for replication, we used this one [here](https://gzip.swimburger.net/).
