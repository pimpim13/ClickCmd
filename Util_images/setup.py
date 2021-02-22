from setuptools import setup

setup(
    name="ImgUtilAZ",
    version='0.1',
    py_modules=['func_img'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        Multisize=func_img:multisize
        Multipixel=func_img:multipixel
    ''',

)
