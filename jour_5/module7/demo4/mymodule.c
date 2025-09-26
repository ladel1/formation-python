// transformer une fonction Python add(a,b) en fonction C intégrée dans un module Python.
#define PY_SSIZE_T_CLEAN
#include <Python.h>

// Fonction fast_add(a, b)
static PyObject* fast_add(PyObject* self, PyObject* args) {
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) return NULL;
    return PyLong_FromLong(a + b);
}

// Table des fonctions
static PyMethodDef Methods[] = {
    {"fast_add", fast_add, METH_VARARGS, "Add two integers."},
    {NULL, NULL, 0, NULL}
};

// Déclaration du module
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT, "mymodule", NULL, -1, Methods
};

PyMODINIT_FUNC PyInit_mymodule(void) {
    return PyModule_Create(&moduledef);
}

