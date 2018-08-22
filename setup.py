from setuptools import find_packages, setup

setup(
    name='nselec',
    version='2.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'requests',
        'tinydb',
        'tinydb-serialization',
    ],
)
