# coding=utf-8
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


with open('requirements.txt') as f:
    required = f.read().splitlines()

with open('requirements-test.txt') as f:
    tests_require = f.read().splitlines()[1:]


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name="NewsMonitor Question 1",
    version='0.1',
    license="BSD",
    cmdclass={'test': PyTest},
    install_requires=required,
    packages=find_packages(),
    tests_require=tests_require + required,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
