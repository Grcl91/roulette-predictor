import os
import subprocess
import sys

# Configuration
REPO_URL = 'https://github.com/Grcl91/roulette-predictor'
BRANCH_NAME = 'master'

def fork_repo():
    # This requires GitHub CLI to be installed and authenticated
    subprocess.run(['gh', 'repo', 'fork', REPO_URL], check=True)

def clone_repo():
    # Clone the forked repository
    forked_url = f'https://github.com/Grcl91/roulette-predictor.git'
    subprocess.run(['git', 'clone', forked_url], check=True)

def install_dependencies():
    # Change directory to the cloned repo
    os.chdir('roulette-predictor')
    # Install dependencies
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True)

if __name__ == '__main__':
    try:
        print('Forking the repository...')
        fork_repo()
        print('Cloning the repository...')
        clone_repo()
        print('Installing dependencies...')
        install_dependencies()
        print('Setup completed successfully!')
    except Exception as e:
        print(f'An error occurred: {e}')