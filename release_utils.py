import argparse
from typing import Tuple
import src
from setup import find_version


def get_next_version(release_type) -> Tuple[str, str]:
    current_ver = find_version("src/__init__.py")
    version_list = [int(x) for x in current_ver.strip("\'").split(".")]
    major, minor, patch = version_list[0], version_list[1], version_list[2]
    if release_type == "patch":
        patch += 1
    elif release_type == "minor":
        minor += 1
        patch = 0
    elif release_type == "major":
        major += 1
        minor = patch = 0
    else:
        raise ValueError("Incorrect release type specified. Acceptable types are major, minor and patch.")

    new_version_tuple = (major, minor, patch)
    new_version_str = ".".join([str(x) for x in new_version_tuple])
    new_tag_str = "v" + new_version_str
    return new_version_str, new_tag_str


def update_version(new_version) -> None:
    """
    given the current version, update the version to the
    next version depending on the type of release.
    """

    current_version = src.__version__

    with open("src/__init__.py", "r") as reader:
        init_file_data = reader.read()

    init_file_data = init_file_data.replace(current_version, new_version)

    with open("src/__init__.py", "w") as writer:
        writer.write(init_file_data)


def main(args):
    if args.release_type in ["major", "minor", "patch"]:
        new_version, new_tag = get_next_version(args.release_type)
    else:
        raise ValueError("Incorrect release type specified")

    if args.update_version:
        update_version(new_version)

    return (new_version, new_tag)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Versioning utils")
    parser.add_argument("--release_type", type=str, required=True, help="type of release = major/minor/patch")
    parser.add_argument(
        "--update_version", action="store_true", required=False, help="updates the version in fairscale/__init__.py"
    )

    args = parser.parse_args()
    new_version, new_tag = main(args)
    print(new_version, new_tag)
