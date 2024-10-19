import subprocess
import os

# List of packages to install
packages = [
    "discord.py-self",
    "requests",
    "pynacl",
    "python-dateutil",
    "instaloader"
]

# Function to install packages
def install_package(package):
    try:
        print(f"Installing {package}...")
        subprocess.check_call([f"pip", "install", package])
        print(f"{package} installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package}: {e}")

# Function to install all packages
def install_all_packages(packages):
    for package in packages:
        install_package(package)

# Function to run the fedded.py script
def run_fedded():
    try:
        print("Running fedded.py...")
        subprocess.check_call(["python", "fedded.py"])
        print("fedded.py executed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error running fedded.py: {e}")

# Main function
def main():
    # Install all packages
    install_all_packages(packages)
    
    # Run the fedded.py script
    run_fedded()

if __name__ == "__main__":
    main()
