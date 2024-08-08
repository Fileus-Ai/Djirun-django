from setuptools import setup, find_packages

setup(
    name='djirun',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',
        'django',
    ],
    entry_points={
        'console_scripts': [
            'djirun = djirun.cli:main',
        ],
    },
    author='Fildouindé Ariel Shadrac OUEDRAOGO',
    author_email='arielshadrac@gmail.com',
    description='Un outil pour générer des projets Django personnalisés.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/arielshadrac/djirun',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)