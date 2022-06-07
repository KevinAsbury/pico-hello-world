set(ProgramName "hello")
set(Executable "${ProgramName}.cpp")
cmake_minimum_required(VERSION 3.23)
include($ENV{PICO_SDK_PATH}/external/pico_sdk_import.cmake)
project(blink LANGUAGES C CXX ASM)
set(CMAKE_C_STANDARD 11)
set(CMAKE_CXX_STANDARD 17)
pico_sdk_init()
add_executable(${ProgramName} ${Executable})
target_link_libraries(${ProgramName} pico_stdlib)
pico_add_extra_outputs(${ProgramName})
# 
# Change the destination for stdio out from UART to USB
# (the default is UART)
# if (TARGET tinyusb_device)
  # pico_enable_stdio_usb(${ProgramName} 1)
  # pico_enable_stdio_uart(${ProgramName} 0)
# endif()
#