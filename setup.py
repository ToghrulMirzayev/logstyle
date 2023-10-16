from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='logstyle',
    version='1.0.3',
    author='Toghrul Mirzayev',
    author_email='togrul.mirzoev@gmail.com',
    description='Logstyle is simply lightweight, colorful and customizable logging library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Topic :: Software Development",
    ],
    install_requires=[
        'PyYAML',
        'colorama'
    ],
    keywords=[
        'log',
        'logging',
        'logs',
        'logger',
        'python-log'
    ],
    python_requires='>=3.7',
)
