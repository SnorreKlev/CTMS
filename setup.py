from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A QOL package/service'
LONG_DESCRIPTION = 'A package that makes it easy to make large and advanced programs'

setup(
    name="MultiLib",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Snorre Klev",
    author_email="eksplosivt@gmail.com",
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords='easy, qol, advanced, simple, libs, libary, package',
    classifiers= [
        "Development Status :: 1 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ],
    install_requires=["pyperclip", "tqdm", "messagebox"]
    
)
