cmake_minimum_required(VERSION 2.8)

project(fww_study)

if(NOT CGAL_DIR)
    set(CGAL_DIR "/usr/local")
endif()

set(CGAL_DIR "${CGAL_DIR}/lib/CGAL")
message(STATUS ${CGAL_DIR})
find_package(CGAL)
if(CGAL_FOUND)
    include_directories(${CGAL_INCLUDE_DIRS})#指定目录
    link_directories(${CGAL_LIBRARIES_DIR})
    message(STATUS ${CGAL_INCLUDE_DIRS})#显示信息
    message(STATUS ${CGAL_LIBRARIES_DIR})
    set(CGAL_LIBRARIES "CGAL;CGAL_Core;gmp;mpfr") # CGAL
    set(HAVE_CGAL True)
else()
    set(HAVE_CGAL False)
    message(STATUS "Configure package without CGAL!")
endif()

include_directories(${PROJECT_SOURCE_DIR}/include)
link_directories(${PROJECT_BINARY_DIR})

#Add subdiretory
add_subdirectory(src)
add_subdirectory(include)
add_subdirectory(test)

