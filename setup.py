from distutils.core import setup


__version__ = '0.0.1'

short_description = 'Exponential Fuckoff decorator'

setup(
    name='expoff',
    version=__version__,
    description=short_description,
    long_description=short_description,
    author='Alexander Zhebrak',
    author_email='fata2ex@gmail.com',
    license='MIT',
    url='https://github.com/zhebrak/expoff',
    keywords=['exponential backoff', 'exponential fuckoff', 'python'],
    classifiers=[],
    py_modules=['expoff']
)
