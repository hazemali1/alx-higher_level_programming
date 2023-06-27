#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Byted
 * @p: PArameter
*/
void print_python_bytes(PyObject *p)
{
	long int s, i;
	char *d;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	s = PyBytes_Size(p);
	printf("  size: %ld\n", s);
	d = ((PyBytesObject *)p)->ob_sval;
	printf("  trying string: %s\n", d);
	if (s < 10)
		printf("  first %ld bytes: ", s + 1);
	else
		printf("  first 10 bytes: ");
	if (s > 10)
		s = 9;
	for (i = 0; i <= s; i++)
	{
		printf("%02hhx", d[i]);
		if (i < s)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_list - List
 * @p: Parameter
*/
void print_python_list(PyObject *p)
{
	int s, i;
	const char *d;

	printf("[*] Python list info\n");
	s = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %ld\n", ((PyListObject*)p)->allocated);
	for (i = 0; i < s; i++)
	{
		d = (((PyListObject *)p)->ob_item[i])->ob_type->tp_name;
		printf("Element %d: %s\n", i, d);
		if (!strcmp(d, "bytes"))
			print_python_bytes(((PyListObject *)p)->ob_item[i]);
	}
}
