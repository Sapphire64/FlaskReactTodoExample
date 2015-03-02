from setuptools import setup, find_packages


setup(
    name='tictail todo',
    version='0.4',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['flask', 'flask-restful', 'setuptools-bower'],
    tests_require=['mock', 'nose'],
    test_suite="nose.collector",
)