import subprocess
from nrobo import set_environment, Environment, EnvKeys
set_environment()
# pytest nrobo_framework_tests --noconftest --confcutdir nrobo_framework_tests
subprocess.check_call(['pytest', 'nrobo_framework_tests', '--noconftest', '--noconftest', 'nrobo_framework_tests', '-n', '10'])
