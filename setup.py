import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="asyncnab",
    version="0.0.1",
    author="jersobh",
    author_email="jersobh@gmail.com",
    description="Biblioteca para geração de boletos bancários e arquivos de remessa/registro e integrações a webservices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jersobh/asyncnab",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)