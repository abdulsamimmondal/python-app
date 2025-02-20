from setuptools import setup, find_packages

setup(
    name='flask_app',  # Name of your application
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'requests',
    ],
    test_suite='tests',  # Points to your tests directory
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'flask-app=app:main',  # This is useful if you want to run the app from the CLI
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',  # Minimum required Python version
)
