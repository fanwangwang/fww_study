## CMakeLists.txt笔记

* 项目最外层 cmake 编写

```
cmake_minimum_required(VERSION 2.8)　　         %必须有的
include_directories(${PROJECT_SOURCE_DIR}/src)　%设置include头文件查找路径
link_directories (${PROJECT_BINARY_DIR}/lib)　　%设置库文件搜索路径
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)
add_subdirectory(src)
add_subdirectory(lib)
```
* 项目内层 cmake 编写
  * 例如在 test 目录里边有 sparse_matrix.cpp 文件,则编辑 CMakeLists.txt 文档
```
add_executable(sparse_matrix sparse_matrix.cpp)
```
如果还有其他的 .cpp 文件，则往CMakeLists.txt 文档里添加即可.
  * 在 src 目录下编辑 CMakeLists.txt 文档

```
file(GLOB_RECURSE HEADER ./*.h)
install(FILES ${HEADER} DESTINATION src)
```

