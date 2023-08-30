import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="HygeiaTab",
    version="1.0",
    author="Marcus Bello",
    author_email="marcusbello@hygeiatab.com",
    description="The FastAPI backend project of hygeiatab",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marcusbello/hygeiatab",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)