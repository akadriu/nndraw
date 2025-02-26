from setuptools import setup, find_packages

setup(
    name="NNDraw",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "matplotlib",
        "numpy",
        "networkx"
    ],
    author="Arbana Kadriu",
    author_email="arbana.kadri@gmail.com",
    description="A library to draw neural networks based on user parameters",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/akadriu/nndraw",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
