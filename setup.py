from setuptools import setup


setup(
    name='ext4scanner',
    version='0.1.1',
    author='INCENDOS',
    author_email='kommander.al@gmail.com',
    description='A useful module',
    license='MIT',
    url='https://github.com/AlanLeinhard/incident',
    packages=['ext4scanner'],
    install_requires=[
        'packaging==21.3',
        'pyparsing==3.0.7',
        'PyQt5==5.15.6',
        'PyQt5-Qt5==5.15.2',
        'PyQt5-sip==12.9.1',
        'sip==6.5.1',
        'toml==0.10.2'],
    entry_points = {
        'console_scripts' : ['ext4scanner = ext4scanner.ext4scanner:main']
    },
    data_files = [
        ('share/applications/', ['vxlabs-ext4scanner.desktop'])
        ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
    long_description=open('README.md').read(),
)