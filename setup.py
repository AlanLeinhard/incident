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
    # install_requires=[
    #     'packaging',
    #     'pyparsing',
    #     'PyQt5',
    #     'PyQt5-Qt5',
    #     'PyQt5-sip',
    #     'sip',
    #     'toml'],
    entry_points={
        'gui_scripts': ['ext4scanner = ext4scanner.ext4scanner:main']
    },
    data_files=[
        ('share/applications/', ['ext4scanner.desktop']),
        ('share/applications/', ['eye.png']),
        ('share/applications/', ['./ext4scanner/background.jpg'])
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment :: GPU',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
    long_description=open('README.md').read(),
)
