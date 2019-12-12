from distutils.core import setup

setup(
    name='django_access_logger_middleware',
    version='0.0.1',
    description='Access logging package for Django',
    url='https://github.com/sharafjaffri/django-access-logger.git',
    author='Sharaf Ali',
    author_email='sharafjaffri@live.com',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    packages=['django_access_logger_middleware'],
    zip_safe=False,
    install_requires=['Django'],
    python_requires=">=3.5",
)
