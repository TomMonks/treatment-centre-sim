# Simulaton Software Overview

The model is written in `python3` and `simpy`.  The simulation libary `simpy` uses a **process based model worldview**.  Given its simplicity it is a highly flexible discrete-event simulation package.

One of the benefits of a package like `simpy` is that it is written in standard python and is free and open for others to use.  
* For research this is highly beneficial:
    * models and methods tested against them can be shared without concerns for commerical licensing.  
    * experimental results (either from model or method) can be recreated by other research teams.
    
* The version of `simpy` in use can also be controlled.  This avoids backwards compatibility problems if models are returned to after several years.

> Detailed documentation for `simpy` and additional models can be found here: https://simpy.readthedocs.io/en/latest/