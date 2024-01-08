#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints some basic info about python lists
 * @p: python object
 **/
void print_python_list_info(PyObject *p)
{
	long in size = PyList_Size(p);
	int i;
	PyListObject *obj = (PyListOject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for(i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i]->tp_name);
}

