from setuptools import setup, find_packages

setup(
    name='specflow-cli',
    version='0.1',
    packages=find_packages(),
    py_modules=['spec_cli'],
    install_requires=[
        'antlr4-python3-runtime',
    ],
    entry_points={
        'console_scripts': [
            'spec=spec_cli:main',
        ],
    },
    include_package_data=True,
    package_data={'spec_grammar': ['*.py']},
)