from setuptools import setup, find_packages


setup(
    name='lookout',
    version='0.1.5',
    description='A simple outbound notification service for Sprint.ly.',
    long_description='',
    keywords='sprintly, services',
    author='Joseph C. Stump',
    author_email='joe@sprint.ly',
    url='https://github.com/sprintly/sprint.ly-services',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['Django', 'pinder', 'simplejson', 'requests'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment",
    ]
)
