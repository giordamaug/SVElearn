from setuptools import setup

setup(
   name='SVElearn',
   version='1.0',
   author='Maurizio Giordano and Ilaria Granata',
   author_email='maurizio.giordano@cnr.it',
   packages=['svelearn', 'svelearn.ensemble', 'svelearn.validation'],
   license='LICENSE.txt',
   description='Voting Ensembling Classifiers with Dataset Splitting to Address Unbalancing',
   long_description=open('README.md').read(),
   install_requires=[
       "numpy",
       "tqdm",
       "typing",
       "pandas",
       "matplotlib",
       "scikit-learn",
       "scipy",
       "lightgbm"
   ],
)