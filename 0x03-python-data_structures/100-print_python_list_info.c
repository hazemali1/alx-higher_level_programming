#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info
 * @p: parameter
*/
void print_python_list_info(PyObject *p)
{
	int s, a, d;
	PyObject *e;

	s = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", s);
	a = ((PyListObject*)p)->allocated;
	printf("[*] Allocated = %d\n", a);
	for (d = 0; d < s; d++)
	{
		e = PyList_GetItem(p, d);
		printf("Element %d: %s\n", d, Py_TYPE(e)->tp_name);
	}
}
