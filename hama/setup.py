from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(
	name='hama',
	version=version,
	description="hama",
	long_description="""\
	hama""",
	classifiers=[], 
	keywords='hama',
	author='Marcel',
	author_email='mhrdina@hama.co.uk',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	include_package_data=True,
	zip_safe=False,
	
	install_requires=[
		'SQLAlchemy',
		'titlecase'
		],
	
	test_suite= 'nose.collector',
	
	entry_points={
		'console_scripts': [
			'hama-case=hama:hama_case_cli',
			'guppy=hama:guppy',
			'grimble=hama:grimble',
			'jimbo=hama:jimbo',
			'egene=hama:egene',
			'update_e_presenter=hama:update_e_presenter']
		},
	)