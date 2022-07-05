# Model technical summary

The model is written in the python programming language and uses a simulation package called `simpy`.  The model code is organised in a Jupyter notebook.  The notebook is organised as follows:

**Imports**

The code imports the python libraries needed to run the computer simulation.

**Constants and defaults for modelling as-is**

This allows a user to set the default distribution parameters, time-dependent arrival rate, resource counts, and simulation settings (number of replications, run length etc.)

**Utility functions**

Non-core code that provides utilities for simulation model users.

**Distribution classes**

High level distribution classes built on `numpy` with their own random number stream.

**Model Parameterisation**

A scenario class that is initialised using user set defaults and can be modified to execute different experiments.  The scenario class also controls common random numbers.

**Patient Pathways Process Logic**

This section contains the actual model logic.  It is organised into two classes to mimic the logic for trauma and non-trauma patients.

**Main model**

This section creates the model and generates random patient arrivals to the model.

**Logic to process end of run results**

This section contains code to produce a summary of simulation results 

**Executing a model**

Contains code demonstrating how to perform a base run (and multiple replications) of the model and obtain and display results. 

**Scenario analysis**

Contains full set of experiments performed with the model.  The code creates the different experiments and run each in turn.  A summary of results is provided a the end.

**Script to produce formatted LaTeX table for paper**

Recreates the LaTeX used to report the results as a table in a paper. 