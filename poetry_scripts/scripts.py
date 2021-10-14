import subprocess

def freeze_requirements():
    subprocess.run(['poetry', 'export', '-f', 'requirements.txt', '--output', 'requirements.txt'])
