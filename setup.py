import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="evi",
    version="0.0.1",
    author="ken",
    author_email="457361577@qq.com",
    description="Implemntation of DS theory (D-S evidence theory)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/qiaokuoyuan/evi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
