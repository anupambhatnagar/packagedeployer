import json
import setuptools


def find_version(version_file_path):
    with open(version_file_path) as version_file:
        data = json.load(version_file)
        assert len(data.keys()) > 0
        if "version" in data.keys():
            version_str = data.get("version")
            return version_str
        raise KeyError('Key "version" not found in version.json')

if __name__ == "__main__":
    setuptools.setup(
        name="package-deployer2",
        version=find_version("version.json"),
        include_package_data=True,
        setup_requires=["ninja"],  # ninja is required to build extensions
        packages=setuptools.find_packages(exclude=("tests", "tests.*")),

    )

