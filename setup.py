from setuptools import find_packages, setup, Extension as _Extension


class Extension(_Extension):
    @property
    def include_dirs(self):
        from numpy import get_include
        return [get_include(), 'src/cpp']

    @include_dirs.setter
    def include_dirs(self, _):
        pass


ext_modules = [Extension(
    'munkres', ['src/munkres.cpp', 'src/cpp/Munkres.cpp'],
    language='c++'
)]
setup(
    name='munkres',
    url='https://github.com/jfrelinger/cython-munkres-wrapper',
    ext_modules=ext_modules,
    version='1.0.6',
    description='Munkres implemented in c++ wrapped by cython',
    author='Jacob Frelinger',
    author_email='jacob.frelinger@duke.edu',
    install_requires=['numpy>=1.3.0'],
    setup_requires=['numpy>=1.3.0'],
    package_data={'src': ['munkres.cpp', 'cpp/Munkres.cpp', 'cpp/Munkres.h']},
    packages=find_packages()
)
