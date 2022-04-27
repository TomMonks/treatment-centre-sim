# 5 Implementation

## 5.1 Software or programming language

The simulation model was developed using python 3.8 and simpy 4.0.  Simpy details are here: [https://simpy.readthedocs.io/en/latest/](https://simpy.readthedocs.io/en/latest/)

The exact software versions are:

```
joblib=0.15.1
jupyterlab=3.0.9
matplotlib=3.3.4
numpy=1.19.2
pandas=1.2.3
pip=21.0.1
python=3.8.12
scipy=1.6.1
simpy=4.0.1
```

A [conda virtual environment](https://github.com/TomMonks/treatment-centre-sim/blob/main/binder/environment.yml) is provided to manage versions on a local machine.

## 5.2 Random sampling 

All sampling uses [`numpy.random.Generator`](https://numpy.org/doc/stable/reference/random/generator.html).  A `numpy` generator object implements the Permuted Congruential Generator 64-bit (PCG64; period = $2^{128}$).

Common random number streams are used in the model.  These are created by through seed vectors (one seed for each activity in each replication).

## 5.3 Model execution

Simpy implements a process based simulation worldview.

## 5.4 System Specification

The model was coded and run on Intel i9-9900K CPU with 64GB RAM running the Pop!_OS 20.04 Linux.