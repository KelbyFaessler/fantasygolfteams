from distutils.core import setup

from Cython.Build import cythonize

setup(ext_modules=cythonize("bbmajors_compute/compute_engine/engine/compute_cpp.pyx"))