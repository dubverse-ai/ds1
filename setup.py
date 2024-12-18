from setuptools import find_packages, setup

install_requires = [
    "requests>=2.25.0",
    "cachetools>=4.2.0",
]

extras_require = {
    ":python_version<'3.9'": ["backports.zoneinfo"],
}

setup(
    name="ds1",
    version="0.1.22",
    author="dubverse",
    description="Dubverse SDK for Python",
    packages=find_packages(),  # Automatically discover and include all packages
    install_requires=install_requires,
    extras_require=extras_require,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",  # Adjust the license as needed
    ],
    project_urls={
        "Source": "https://github.com/dubverse-ai/ds1",
    },
)
