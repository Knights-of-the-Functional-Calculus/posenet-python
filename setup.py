from distutils.core import setup

setup(
    name='posenet-tf',
    version='0.0.3',
    packages=['posenet','posenet.converter'],
    package_data={'': ['converter/config.yaml']},
	include_package_data=True,
)