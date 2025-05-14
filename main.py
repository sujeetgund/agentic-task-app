def get_requirements(file_path):
    """
    Reads a requirements file and returns a list of packages.
    """
    with open(file_path, "r") as file:
        return [
            line.strip() for line in file if line.strip() and not line.startswith("#")
        ]

if __name__ == "__main__":
    # Example usage
    requirements = get_requirements("requirements.txt")
    print(requirements)