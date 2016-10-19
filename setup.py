from setuptools import setup, find_packages


setup(
    name='screenblot',
    version='0.0.1',
    author='Cyril Robert',
    author_email='cyril@67labs.com',
    url='https://github.com/67labs/screenblot-api',
    install_requires=[
        'setuptools',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'screenblot = screenblot.main:main',
        ]},
)
