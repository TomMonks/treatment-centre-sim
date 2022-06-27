# Problem description

## FirstTreatment: A health clinic based in the US.

**This example is based on exercise 13 from Nelson (2013) page 170.**

> *Nelson. B.L. (2013). [Foundations and methods of stochastic simulation](https://www.amazon.co.uk/Foundations-Methods-Stochastic-Simulation-International/dp/1461461596/ref=sr_1_1?dchild=1&keywords=foundations+and+methods+of+stochastic+simulation&qid=1617050801&sr=8-1). Springer.* 

Patients arrive to the health clinic between 6am and 12am following a non-stationary poisson process. After 12am arriving patients are diverted elsewhere and remaining WIP is completed.  On arrival, all patients quickly sign-in and are **triaged**.   

The health clinic expects two types of patient arrivals: 

**Trauma arrivals:**
* patients with severe illness and trauma that must first be stablised in a **trauma room**.
* these patients then undergo **treatment** in a cubicle before being discharged.

**Non-trauma arrivals**
* patients with minor illness and no trauma go through **registration** and **examination** activities
* a proportion of non-trauma patients require **treatment** in a cubicle before being dicharged. 

> In this model treatment of trauma and non-trauma patients is modelled seperately.  