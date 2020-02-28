# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

setup(
    name="speechmetrics",
    version="1.0",
    packages=find_packages(),

    install_requires=[
        'numpy',
        'scipy',
        'tqdm',
        'resampy',
        'pystoi',
        'museval',
        'gammatone @ git+https://github.com/detly/gammatone',
        'srmrpy @ git+https://github.com/jfsantos/SRMRpy',
    ],
    extras_require={
        'cpu': ['tensorflow==2.0.0', 'librosa'],
        'gpu': ['tensorflow-gpu==2.0.0', 'librosa'],
    },
    include_package_data=True
)
