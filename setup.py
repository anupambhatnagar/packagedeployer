import re
import setuptools


def find_version(version_file_path):
    with open(version_file_path) as version_file:
        for line in version_file:
            version_match = re.search("^__version__", line)
            if version_match:
                version_line = version_match.string.strip()
                version_str = version_line.split("=")[1].strip()
                return version_str
        raise RuntimeError("__version__ string not found in %s" % version_file_path)

if __name__ == "__main__":
    setuptools.setup(
        name="package-deployer2",
        version=find_version("src/__init__.py"),
        include_package_data=True,
        setup_requires=["ninja"],  # ninja is required to build extensions
        packages=setuptools.find_packages(exclude=("tests", "tests.*")),
    )
