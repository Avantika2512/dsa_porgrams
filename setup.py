import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='dsa_algos',
    version='1.0.0',
    author='Avantika Sengar',
    description='DSA Algorithms Package',
    long_descriptionx=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/avantika2512/dsa_programs',
    project_urls={
        "Bug Tracker": 'https://github.com/avantika2512/dsa_programs/issues'
    },
    license='MIT',
    packages=['dsa_algos']
)