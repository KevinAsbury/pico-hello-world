import os
import subprocess

# Set the file name below and type python build.py in the command line
file_name = "hello.elf"

# Get the current working directory
pwd = subprocess.run(["pwd"], stdout=subprocess.PIPE, text=True)
# Run cmake and save output to the build directory
cmake_run = subprocess.Popen(["cmake", pwd.stdout.removesuffix("\n")+'/build'])
cmake_run.wait()
# Run make in the build directory
make_run = subprocess.Popen(
    ["make", "-C", pwd.stdout.removesuffix("\n")+'/build'])
make_run.wait()
# Build and execute the openocd command to transfer elf file to pico board
# Pico SDK config for use with a pico probe debugger
interface = "interface/picoprobe.cfg"
target = "target/rp2040.cfg"  # the pico chipset from Pico SDK
# transfer commands
program = f'-c "program {pwd.stdout[:-1]}/build/{file_name} verify reset exit"'
cmd = f'-f {interface} -f {target} {program}'  # combine
os.system(f'openocd {cmd}')  # run
