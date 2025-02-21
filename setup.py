from setuptools import setup, find_packages

setup(
    name="Jarvis",
    version="1.0",
    packages=find_packages(),  # Automatically finds packages like 'engine'
    include_package_data=True,  # Includes non-code files specified in MANIFEST.in
    install_requires=[],  # Add dependencies here if needed
)
