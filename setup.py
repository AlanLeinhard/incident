from setuptools import setup


setup(
    name='EXT4_SCANNER',
    version='0.1',
    author='INCENDOS',
    author_email='kommander.al@gmail.com',
    description='A useful module',
    license='MIT',
    url='https://github.com/AlanLeinhard/incident',
    packages=['EXT4_SCANNER'],
    install_requires=[
        'packaging==21.3',
        'pyparsing==3.0.7',
        'PyQt5==5.15.6',
        'PyQt5-Qt5==5.15.2',
        'PyQt5-sip==12.9.1',
        'sip==6.5.1',
        'toml==0.10.2'],
    entry_points = {
        'console_scripts' : ['EXT4_SCANNER = EXT4_SCANNER.script2']
    },
    long_description=open('README.md').read(),
)