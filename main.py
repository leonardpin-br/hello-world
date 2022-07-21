#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""Entry point of this script/app.

Last modified in 2022-07-22

Python version 2.7.9 (McNeel Rhinoceros 7)

Example:
    How a shelf button can be written::

        !-RunPythonScript "E:\cloud\Backup\Libraries\scripts\rhinoceros\hello-world\hello_world.py"

References:
    `Your First Python Script in Rhino (Windows)`_

    `Running a Python script in Rhino`_

.. _Your First Python Script in Rhino (Windows):
   https://developer.rhino3d.com/guides/rhinopython/your-first-python-script-in-rhino-windows/
.. _Running a Python script in Rhino:
   https://developer.rhino3d.com/guides/rhinopython/python-running-scripts/

"""

import sys

import rhinoscriptsyntax as rs


def main():
    u"""The main function to execute the entire project/application.
    """
    print("Hello, World!\n\nRunning on Python version:\n" + sys.version)


if __name__ == "__main__":
    main()
