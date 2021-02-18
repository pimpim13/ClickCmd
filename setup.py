from setuptools import setup

setup(
    name="FileUtil",
    version='0.1',
    py_modules=['function'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        ExtractZip=functions:extract_zip
        InFolder=functions:infolder
    ''',
)
