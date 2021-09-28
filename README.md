# Welcome to `patient_abm`!

A library for generating synthetic electronic health records in FHIR v4 format
using agent-based modeling to simulate patient pathways.

See the redacted final report from the March 2021 project development for an overview of the main components as well as suggested future developments - "REDACTED_C245 ABM Patient Pathways_Final Report_V3_28042021.cleaned.pdf"

# Description

The simulation models a single patient interacting with environments
(hospitals, GPs, etc) which can prompt updates to the patient's record.

Patients and Environments are modelled as agents. They are python class objects
of type `PatientAgent` and `EnvironmentAgent` respectively, and are located
in
```
src/patient_abm/agent
```

The simulation is configured by a configuration script, and the details of
the patient-environment interactions must be implemented in the `intelligence`
layer (see the relevant sections below for more details). We have provided
templates for these elements.

### Project Stucture

- The main code is found in the `src` and `template` folders of the repository (see Usage below for more information)
- The accompanying [report](./reports/report.pdf) is also available in the `reports` folder

# Installation

## `pip` installation

This repository has been tested using [![Python v3.7](https://img.shields.io/badge/python-v3.7-blue.svg)](https://www.python.org/downloads/release/python-370/) and [![Python v3.8](https://img.shields.io/badge/python-v3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)

Use your terminal to `cd` into the directory containing this `README`
(the project root directory) and run:

```
pip install .
```

Alternatively, if you want to develop and edit the library, then run

```
pip install -e ".[dev]"
```

## Environment variables

In the project root directory, run:

```
export PATIENT_ABM_DIR="$(pwd)"
```

# Running a simulation

After installing `patient_abm`, to run a patient pathway simulation, you must:

  (1) Set up the simulation configuration script `config.json`

  (2) Implement the `intelligence` layer, which:

  - governs how the Patient and Environment agents interact;

  - generates new Patient record entries;

  - decides which Environment the patient should visit next and at what time;

  - optionally applies custom updates the Patient and Environment agents.

In the folder `template` we provide templates for the `config.json` and the
`intelligence` layer. The subfolder, also called `template`, contains empty
template files, whereas the subfolder `example` contains example files.

You `config.json` and `intelligence_dir` can be located anywhere - they do not
need to be inside this repo.

After completing this, in the terminal, run:
```
patient_abm simulation run --config_path </path/to/config.json>
```
to run the simulation. Angular brackets <...> here and in the following 
indicate places where the user needs to supply their own values,
or where values are automatically generated by the simulation. For instance,
if you want to run the `config.json` in `template/example` this this is
the command

```
patient_abm simulation run --config_path template/example/config.json
```

Its outputs can be found in `template/example/outputs`.

This will load and validate the `config.json`, load the variables from the
config, and then run the simulation one patient at a time, saving the outputs
after each simulation.

The following folder structure and outputs are created in the `save_dir`
defined in the `config.json`:

```
<simulation_id> /
    agents /
        patient_<patient_id>.tar
	    environment_<environment_0_id>.tar
	    environment_<environment_1_id>.tar
        ...
    fhir /
	    bundle.json
    main.log
    patient.log 
```

where a unique `simulation_id` is automatically generated for every patient
in the `config.json`.

## The configuration file `config.json`

The configuration file `config.json` contains all the information needed to
initialize:

  - All the simulation Patients
  - All the simulation Environments (each Patient's 'universe'), along
  with the names of the interactions that the `intelligence` layer can apply
  when the Patient is present at an Environment
  - Path to the `intelligence` layer directory, `intelligence_dir`
  - Path to the `save_dir` directory in which the simulation outputs will be
  written
  - Any other simulation parameter, such as stopping conditions, logging
  frequency, etc.

The `config.json` is a file with key-value pairs:
```
{
    key_0: <value_0>,
    key_1: <value_1>,
    ...
}
```

Below we provide the definition for each key and what the user is expected to
provide as the corresponding value

### `patients`

The key `patients` refers to data that should be used to initialize patient
agent objects. You can enter its value in one of two ways:
  - Write the patient data directly as a list of dictionaries. Each dictionary
  contains the patient class initialization arguments as key-value pairs.
  - Give a path to a JSON (strongly preferred) or a CSV file that contains the
  same data as the list of dictionaries. The reason a JSON is preferred is
  because correct the datatypes are preserved, and is particularly important
  in the case where the Patient attribute is a nested object (such as the
  Patient's `conditions` attribute.)

Note that each patient must have the following required attributes:
  - patient_id : Union[str, int]: Unique ID for the patient.
  - gender : str: Patient gender, either "male" or "female".
There are many other optional attributes, see the documentation for
the `PatientAgent` class in `patient_abm.agent.patient`.

Two patient can have the same `patient_id`.

Even though multiple patients can be listed here, the simulation only
runs for one patient at a time, they do not interact.

### `environments`

The key `environments` refers to data that should be used to initialize
Environment objects. You can enter its value in one of two ways:
  - Write the environment data directly as a list of dictionaries.
  Each dictionary contains the patient class initialization arguments as
  key-value pairs.
  - Give a path to a JSON (strongly preferred) or a CSV file that contains the
  same data as the list of dictionaries. The reason a JSON is preferred is
  because correct the datatypes are preserved, and is particularly important
  in the case where the Environment attribute is a nested object (such as the
  Environment `interactions` attribute.)

Note that each environment must have the following required attribute:
  - environment_id : Union[str, int]: Unique ID for the environment.
There are many other optional attributes, see the documentation for
the `EnvironmentAgent` class in `patient_abm.agent.environment`.

Each environment in the list must have a unique `environment_id`.

Each environment's
`interactions` attribute is a list of strings referring to functions in the
`intelligence` layer with a specific structure. For example, if the
intelligence layer directory looks like

```
<intelligence_dir> /
    interactions /
        general.py
	    gp.py
    intelligence.py
```

and there are functions in `general.py` called `inpatient_encounter` and
`outpatient_encounter`, and two functions in `gp.py` called `measure_bmi`
and `diagnose_fever`, then suppose we had a GP environments, its `interactions`
list might be

```
interactions = [
    "general.inpatient_encounter",
    "gp.measure_bmi",
    "gp.diagnose_fever"
]
```

Note that default interactions located in
`src/patient_abm/intelligence/interactions/default`
get added to every environment as well. These are currently automatically
added but in future could be amended.

### `intelligence_dir`

The key `intelligence_dir` refers to the directory that contains the
`intelligence` layer. Its value is the path string to that directory.

### `save_dir`

The key `save_dir` refers to the directory in which the simulation outputs
should be saved. Its value is the path string to that directory.

### `initial_environment_ids`

The key `initial_environment_ids` refers to the initial Environment that each
patient should visit, given by the Environment's `environment_id`. Its value
is a dictionary, which can take several formats:
  - `{from_id: <environment_id>}`, all Patients will start from the Environment
  with that `<environment_id>`.
  - `{from_id: [<environment_id_0>, <environment_id_1>, ...]}`, the list of
  environment IDs must be as long as the number of Patients, each Patient
  will start from the Environment given in the corresponding position in the
  list.
  - `{from_probability: [<p_0>, <p_1>,...]}`, the list of
  probabilities `p_i` must be as long as the number of Environments. The
  distribution is sampled for each patient.
   - `{from_probability: [<p_0>, <p_1>,...]}`, the list of
  probabilities `p_i` must be as long as the number of Environments. The
  distribution is sampled for each patient.
  - `{from_json: '</path/to/ids.json>'}`, a JSON file containing initial 
  environment IDs, one for each patient.

### `stopping_condition`

The key `stopping_condition` refers to the condition that should cause
the simulation while loop to terminate. The simulation can always terminate
early if a `death` interaction is applied.
Its value is a dictionary, which can take several formats:
  - `{max_num_steps: <max_num_steps>}`, the maximum number of steps
  (an integer) in the simulation.
  - `{max_real_time: {<unit>: <value>}}`, maximum real time the simulation
  should run for. The subdictionary is `{<unit>: <value>}` is passed into
  python's `datetime.timedelta` function and so should respect the parameter
  values there.
  - `{max_patient_time: {<unit>: <value>}}`, maximum patient time the
  simulation
  should run for. The subdictionary is `{<unit>: <value>}` is passed into
  python's `datetime.timedelta` function and so should respect the parameter
  values there. 

### `hard_stop`

The key `hard_stop` refers to a hard upper bound on the number of simulation
steps. It is there to try and prevent the loop going to infinity for any
reason. An integer value is expected.

### `log_every`

The key `log_every` refers to the number of simulation steps that should 
execute between logging. Its value is an integer, i.e.. if it is `n` then
logging will happen every `n`-th simulation step.

### `log_intermediate`

If `log_every` > 1, then logging of simulation information between `log_every`
steps may be lost. `log_intermediate` is a boolean which, if set to `true`,
will ensure intermediate log information is collected but then actually writes
to the logger in the `log_every` step. If `false`, only the information at
every `log_every`-th simulation steps is written.

### `log_patient_record`

A boolean value which, if set to `true` add the latest patient record entry
to the logger. This should be used mainly for debugging. The full patient
record is always stored in the saved patient agent tar file, and it can be
recovered from there.

### `fhir_server_validate`

At the end of the simulation, the patient record is converted into a FHIR
Bundle resource and validated. Validation can be done using an "offline" method
via the python `fhir.resources` library, or "online" by sending the bundle
to the HAPI FHIR server (http://hapi.fhir.org/baseR4). If
`fhir_server_validate` is `true`, the online method used.

### `patient_record_duplicate_action`

When new patient entries are added to the patient record, a validation step
is performed which checks whether the entry already exists, this is to prevent
duplication. `patient_record_duplicate_action` decides the action to take if a
duplicate is found. If it is set to "add", the new entry is added, whereas if
if it is set to "skip" the entry won't be added.

### Breast cancer pathway config

As an illustration for how a breast cancer pathway might look, we have provided a `config.json` for this in `template/breast_cancer`. This is simply an initial version of how this script could be configured for such a pathway, but this template and the intelligence layer can be configured to facilitate more complex dynamics.


## The `intelligence` layer

The `intelligence` layer is a directory of python scripts. The location of the
directory is given by the field `intelligence_dir` in the `config.json`. The
structured of `intelligence_dir` is as follows:

```
<intelligence_dir> /
    interactions /
        <interactions_0>.py
	    <interactions_1>.py
        ...
    intelligence.py
```

The `intelligence.py` script must contain a function called `intelligence`.
More information about the `intelligence` layer and how it should be
structured are provided inside the respective files in
`template/template/<intelligence_dir>`.

# `nox` and tests

`nox` is used to check code is correctly formatted and runs the test suite.
To use `nox`, `cd` the project root directory and run:

```
nox
```

Tests can also be run from this directory via
```
pytest tests
```

# Notebooks

There are two demo notebooks in the `notebooks` folder.

### `patient-agent.ipynb`

In this notebook we introduce the patient agent and its methods including:

  - initializing with comorbidities
  - adding properties to conditions, such as severity
  - updating the patient record
  - the patient record internal representation and converting to FHIR

### `simulation.ipynb`

In this notebook we walk through how to run a simulation with a very simple intelligence layer and interactions. Please see above for more information about the simulation configuration script and the intelligence layer (we will not go into detail about the intelligence layer in the notebook). Here we will be using the files in template/example, and going through main processes that are called when `patient_abm.simulation.run.simulate` is executed (which is the function called by the CLI command `patient_abm simulation run`)

### Roadmap

See the [open issues](https://github.com/nhsx/SynthVAE/issues) for a list of proposed features (and known issues).

### Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

_See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidance._

### License

Distributed under the MIT License. _See [LICENSE](./LICENSE) for more information._

### Contact

To find out more about the [Analytics Unit](https://www.nhsx.nhs.uk/key-tools-and-info/nhsx-analytics-unit/) visit our [project website](https://nhsx.github.io/AnalyticsUnit/projects.html) or get in touch at [analytics-unit@nhsx.nhs.uk](mailto:analytics-unit@nhsx.nhs.uk).

### Acknowledgements
