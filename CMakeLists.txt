cmake_minimum_required(VERSION 3.18 FATAL_ERROR)
project(vpex_backend)

find_package(Python3 COMPONENTS Interpreter Development)
find_package(Torch 2.4 REQUIRED)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} ${TORCH_CXX_FLAGS}")
set(CMAKE_CXX_STANDARD 17)

include_directories(${Python3_INCLUDE_DIRS})
include_directories(${TORCH_INCLUDE_DIRS})

message("  Pytorch install at ${TORCH_INSTALL_PREFIX}")
message("  Pytorch libraries ${TORCH_LIBRARIES}")
message("  Python include ${Python3_INCLUDE_DIRS}")


# Define our library target
add_library(vpex SHARED 
  src/extension.cpp
)

set(TORCH_PYTHON_LIBRARY "${TORCH_INSTALL_PREFIX}/lib/libtorch_python.so")

# Link against LibTorch
target_link_libraries(vpex ${TORCH_LIBRARIES} ${TORCH_PYTHON_LIBRARY})

set_target_properties(vpex PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${PROJECT_SOURCE_DIR}/python/torch_vpu/_C/")
