import argparse
import json
from typing import Tuple

from setup import find_version


def get_next_version(release_type) -> Tuple[str, str]:
    current_ver = find_version("version.json")
    first, second, third = list(map(int, current_ver.split(".")))
    if release_type == "patch":
        third += 1
    elif release_type == "minor":
        second += 1
        third = 0
    elif release_type == "major":
        first += 1
        second = third = 0
    else:
        raise ValueError("Incorrect release type specified. Acceptable types are major, minor and patch.")

    new_version_tuple = (first, second, third)
    new_version_str = ".".join([str(x) for x in new_version_tuple])
    new_tag_str = "v" + new_version_str
    return new_version_str, new_tag_str


def bump_version(new_version) -> None:
    """
    given the current version, bump the version to the
    next version depending on the type of release.
    """
    # new_version = get_next_version('patch')

    with open("version.json", "r") as f:
        data = json.load(f)
    print("The current version is: %s" % data["version"])

    data["version"] = new_version
    with open("version.json", "w") as f:
        json.dump(data, f)
    print("The new version is: %s" % new_version)


def main(args):
    if args.release_type in ["major", "minor", "patch"]:
        output = get_next_version(args.release_type)
    else:
        raise ValueError("Incorrect release type specified")

    if args.bump_version:
        bump_version(output[0])

    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Versioning utils")
    parser.add_argument("--release_type", type=str, required=True, help="type of release = major/minor/patch")
    parser.add_argument(
        "--bump_version", action="store_true", required=False, help="updates the version in version.json"
    )

    args = parser.parse_args()
    result = main(args)
    print(result)
