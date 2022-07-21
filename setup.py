from distutils.core import setup, Extension
import numpy
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['RelaxedIK'],
    scripts=[''],
    package_dir={'': 'src'},
    ext_modules=[Extension(
        'src/RelaxedIK/Utils/_transformations',
        ['src/RelaxedIK/Utils/transformations.c'],
        include_dirs=[numpy.get_include()]
        )]
    )

setup(**d)
