from setuptools import setup

setup(
   name='StocksBar',
   version='1.0',
   description='Bar where drinks follow supply/demand',
   author='Lucas Hehl',
   author_email='lucas@hehl.com.br',
   packages=['StocksBar'],
   install_requires=['flask', 'blessed', 'requests'],
   scripts=[
        'scripts/server',
        'scripts/client',
    ]
)