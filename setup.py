from setuptools import setup, find_packages

setup(
    name="ds1",
    version="0.1.2",
    author="peritissimus",
    description="Dubverse SDK for Python",
    packages=find_packages(),  # Automatically discover and include all packages
    install_requires=["requests>=2.0", "cachetools"],
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
        "License :: OSI Approved :: MIT License",  # Adjust the license as needed
    ],
    project_urls={
        "Source": "https://github.com/dubverse-ai/ds1",
    },
)
