#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
 * print_python_string - Print string
 * @p: Parameter
*/
void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %zd\n", PyUnicode_GET_LENGTH(p));
	printf("  value: %s\n", PyUnicode_AsUTF8(p));
}
