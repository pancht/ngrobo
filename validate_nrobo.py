import subprocess
from nrobo import set_environment, Environment, EnvKeys
set_environment()
subprocess.check_call(['pytest', 'nrobo_framework_tests', '--noconftest'])
