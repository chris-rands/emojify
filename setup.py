import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="emojify",
    version="0.5",
    license="MIT",
    scripts=["emojify", "emojify.py", "test_emojify"],
    author="Chris Rands",
    author_email="c_rands100@hotmail.com",
    description="Obfuscate your python script by converting it to emoji icons",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chris-rands/emojify",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
