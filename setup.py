from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="equivocal",
    version="0.1.0",
    author="Max Albsmeyer",
    author_email="malbsmeyer@gmail.com",  
    description="Semantic audio understanding without rendering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/malbsmeyer/equivocal",   
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Sound/Audio :: Analysis",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20.0",
        "librosa>=0.10.0",
        "soundfile>=0.12.0",
        "scikit-learn>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "jupyter>=1.0.0",
            "matplotlib>=3.5.0",
        ],
    },
)