from distutils.core import setup
from distutils.extension import Extension

from Cython.Build import cythonize

extensions = [
    Extension("bbmajors_compute.compute_engine.engine.compute_cpp",
        ["bbmajors_compute/compute_engine/engine/compute_cpp.pyx"],
        language='c++',
        include_dirs=['bbmajors_compute/compute_engine/engine/']
    )
]

setup(ext_modules=cythonize(extensions))
#setup(ext_modules=cythonize("bbmajors_compute/compute_engine/engine/compute_cpp.pyx"))