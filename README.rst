====
Xlsx
====

Xlsx is a simple Django app to import/export xlsx files to models

Detailed documentation is in the "docs" directory.

Quick start
-----------

Suppose you have an xlsx:

+---------------------+------------------+
| CUSTOMER FIRST NAME | CUSTOMER SURNAME |
+=====================+==================+
| John                | Black            |
+---------------------+------------------+
| Jack                | Red              |
+---------------------+------------------+
| Tom                 | Green            |
+---------------------+------------------+

and want to load the data into MyModel

MyModel should have an XLSX_2_FIELDS attribute to remap column-names to field-names

::

    class MyModel(models.Model):
        name = models.CharField(max_length=50)
        surname = models.CharField(max_length=50)

        XLSX_2_FIELDS = {
            "CUSTOMER FIRST NAME": name,
            "CUSTOMER SURNAME": surname,
        }

now you can load...

::

    import openpyxl as pyx
    import xlsx

    wb = pyx.load_workbook("sample.xslsx")
    xlsx.load(MyModel, wb.active.rows)
