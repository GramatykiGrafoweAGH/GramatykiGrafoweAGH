import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='GramatykiGrafoweAGH',
    version='0.1.0',
    author='',
    author_email='',
    description='Gramatyka grafowa do rekurencyjnej adaptacji siatek czworokątnych',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/matix522/GramatykiGrafoweAGH',
    project_urls={
        'Bug Tracker': 'https://github.com/matix522/GramatykiGrafoweAGH/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_requires='>=3.9',
    install_requires=['networkx', 'matplotlib'],
    tests_require=['pytest']
)
