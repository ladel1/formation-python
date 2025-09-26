#include <Python.h>
#include <stdio.h>

int main(){
    Py_Initialize();
    PyRun_SimpleString("print('Hello from embedded Python')");
    Py_Finalize();
    return 0;
}