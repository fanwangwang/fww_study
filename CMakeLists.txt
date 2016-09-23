cmake_minimum_required(VERSION 2.8)

project(fww_study)
include_directories(${PROJECT_SOURCE_DIR}/src)
link_directories (${PROJECT_BINARY_DIR}/lib)
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)

#Add subdiretory
add_subdirectory(src)
add_subdirectory(test)

