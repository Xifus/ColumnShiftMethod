# Column Shift Method
This method randomises the Sobol' sequence to break the sequence's inner-determinism. Additional test results and details can be found in https://doi.org/10.1016/j.ress.2021.107499.

The code is written to use the Sobol' sequence generator from SALib library [1], but it can be simply changed to other Sobol' sequence generators; however, the output sequences are designed to use Saltelli's method [2] to create sample Matrices A and B. 

To use the Column Shift method, please cite

```
@article{Sun2021,
author = {Sun, Xifu and Croke, Barry and Roberts, Stephen and Jakeman, Anthony},
doi = {10.1016/j.ress.2021.107499},
issn = {09518320},
journal = {Reliability Engineering {\&} System Safety},
keywords = {Quasi-Monte Carlo,Randomized Sobol′ sequence,Sensitivity analysis,Standard error,Uncertainty estimation,randomized sobol,sequence},
month = {jun},
number = {February},
pages = {107499},
publisher = {Elsevier Ltd},
title = {{Comparing methods of randomizing Sobol′ sequences for improving uncertainty of metrics in variance-based global sensitivity estimation}},
url = {https://linkinghub.elsevier.com/retrieve/pii/S0951832021000636},
volume = {210},
year = {2021}
}
```

##### Reference

[1] Herman, J. and Usher, W. (2017) SALib: An open-source Python library for sensitivity analysis. Journal of Open Source Software, 2(9). doi:10.21105/joss.00097

[2] Saltelli, A. (2002) Making best use of model evaluations to compute sensitivity indices. Computer Physics Communications 145, 280–297. doi.org/10.1016/S0010-4655(02)00280-1
