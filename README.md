# ColumnShiftMethod
This method randomises the Sobol' sequence to break the inner-determinism. Additional test results and details can be found in https://doi.org/10.1016/j.ress.2021.107499

The code is written to use the Sobol' sequence generator from SALib library, but it can be simply changed to other Sobol' sequence generators; however, the output sequences are designed to use Saltelli's method to create sample Matrix A and Matrix B. 
