from setuptools import setup, find_packages

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    name='django-xlsx',
    version='0.0.3',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='Django import/export to Excel files',
    url='https://github.com/depaolim/django-xlsx',
    author="Marco De Paoli",
    author_email="depaolim@gmail.com",
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
)
