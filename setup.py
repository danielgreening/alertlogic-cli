import re
import ast
from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('alertlogic/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='alertlogic-cli',
    version=version,
    url='https://github.com/alertlogic/alertlogic-cli',
    license='MIT',
    author='Alert Logic Inc.',
    author_email='support@alertlogic.com',
    description='Command Line Client for Alertlogic Services.',
    entry_points = {
        'console_scripts': ['alertlogic-cli=alertlogiccli.alertlogic_console:main']
    },
    packages=find_packages(exclude=['contrib', 'docs', 'tests*', 'troubleshooting']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    python_requires='>=2.7, <3',
    install_requires=[
        'requests>=2.18'
    ],
    extras_require={
        'dev': [
            'pytest>=3',
            'mock>=2.0.0',
            'httpretty>=0.8.14',
            'pycodestyle>=2.3.1'
        ],
    },
    keywords=['cli', 'alertlogic']
)
