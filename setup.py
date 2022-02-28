from setuptools import setup, find_packages

import versioneer


setup(
    name='canvascli',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),

    description='A CLI to reformat and review Canvas grades',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    author='Joel Ostblom',
    author_email='joelostblom@protonmail.com',
    url='https://github.com/joelostblom/canvascli',

    python_requires='>=3.6',
    py_modules=['canvascli'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'altair>=4.1.0',
        'canvasapi>=2.1.0',
        'click>=8.0.0',
        'pandas>=1.1.0',
        'tabulate>=0.8.3',
        'dataclassy>=0.10',
        'luddite>=1.0',
        'appdirs>=1.0'
    ],
    entry_points={
        'console_scripts': [
            'canvascli = canvascli.main:cli',
        ],
    },
)
