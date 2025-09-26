from setuptools import setup, find_packages

# Read the README file for long description (optional)
def get_requirements():
    with open('requirements.txt') as obj:
        requirements = [x.replace('\n','') for x in list(obj) if x!='-e .']
    print(requirements)
    return requirements

setup(
    name="mlproject",  # Replace with your project name
    version="0.1.0",   # Initial version
    author="Satyajit Sahoo",
    author_email="suraj.sahoo.333@gmail.com",
    packages=find_packages(),  # Automatically finds packages in your project
    install_requires = get_requirements()
    )

