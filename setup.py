from distutils.core import setup

setup(
    name='CodeFoo 2020',
    version='0.1dev',
    packages=[open('requirements.txt').read()],
    license='MIT License',
    long_description=open('README.txt').read(),
)