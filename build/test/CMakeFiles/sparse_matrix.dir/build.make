# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/fww/repository/fww_study

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/fww/repository/fww_study/build

# Include any dependencies generated for this target.
include test/CMakeFiles/sparse_matrix.dir/depend.make

# Include the progress variables for this target.
include test/CMakeFiles/sparse_matrix.dir/progress.make

# Include the compile flags for this target's objects.
include test/CMakeFiles/sparse_matrix.dir/flags.make

test/CMakeFiles/sparse_matrix.dir/sparse_matrix.cpp.o: test/CMakeFiles/sparse_matrix.dir/flags.make
test/CMakeFiles/sparse_matrix.dir/sparse_matrix.cpp.o: ../test/sparse_matrix.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/fww/repository/fww_study/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object test/CMakeFiles/sparse_matrix.dir/sparse_matrix.cpp.o"
	cd /home/fww/repository/fww_study/build/test && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/sparse_matrix.dir/sparse_matrix.cpp.o -c /home/fww/repository/fww_study/test/sparse_matrix.cpp

test/CMakeFiles/sparse_matrix.dir/sparse_matrix.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/sparse_matrix.dir/sparse_matrix.cpp.i"
	cd /home/fww/repository/fww_study/build/test && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/fww/repository/fww_study/test/sparse_matrix.cpp > CMakeFiles/sparse_matrix.dir/sparse_matrix.cpp.i

test/CMakeFiles/sparse_matrix.dir/sparse_matrix.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/sparse_matrix.dir/sparse_matrix.cpp.s"
	cd /home/fww/repository/fww_study/build/test && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/fww/repository/fww_study/test/sparse_matrix.cpp -o CMakeFiles/sparse_matrix.dir/sparse_matrix.cpp.s

test/CMakeFiles/sparse_matrix.dir/sparse_matrix.cpp.o.requires:

.PHONY : test/CMakeFiles/sparse_matrix.dir/sparse_matrix.cpp.o.requires

test/CMakeFiles/sparse_matrix.dir/sparse_matrix.cpp.o.provides: test/CMakeFiles/sparse_matrix.dir/sparse_matrix.cpp.o.requires
	$(MAKE) -f test/CMakeFiles/sparse_matrix.dir/build.make test/CMakeFiles/sparse_matrix.dir/sparse_matrix.cpp.o.provides.build
.PHONY : test/CMakeFiles/sparse_matrix.dir/sparse_matrix.cpp.o.provides

test/CMakeFiles/sparse_matrix.dir/sparse_matrix.cpp.o.provides.build: test/CMakeFiles/sparse_matrix.dir/sparse_matrix.cpp.o


# Object files for target sparse_matrix
sparse_matrix_OBJECTS = \
"CMakeFiles/sparse_matrix.dir/sparse_matrix.cpp.o"

# External object files for target sparse_matrix
sparse_matrix_EXTERNAL_OBJECTS =

test/sparse_matrix: test/CMakeFiles/sparse_matrix.dir/sparse_matrix.cpp.o
test/sparse_matrix: test/CMakeFiles/sparse_matrix.dir/build.make
test/sparse_matrix: test/CMakeFiles/sparse_matrix.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/fww/repository/fww_study/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable sparse_matrix"
	cd /home/fww/repository/fww_study/build/test && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/sparse_matrix.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
test/CMakeFiles/sparse_matrix.dir/build: test/sparse_matrix

.PHONY : test/CMakeFiles/sparse_matrix.dir/build

test/CMakeFiles/sparse_matrix.dir/requires: test/CMakeFiles/sparse_matrix.dir/sparse_matrix.cpp.o.requires

.PHONY : test/CMakeFiles/sparse_matrix.dir/requires

test/CMakeFiles/sparse_matrix.dir/clean:
	cd /home/fww/repository/fww_study/build/test && $(CMAKE_COMMAND) -P CMakeFiles/sparse_matrix.dir/cmake_clean.cmake
.PHONY : test/CMakeFiles/sparse_matrix.dir/clean

test/CMakeFiles/sparse_matrix.dir/depend:
	cd /home/fww/repository/fww_study/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/fww/repository/fww_study /home/fww/repository/fww_study/test /home/fww/repository/fww_study/build /home/fww/repository/fww_study/build/test /home/fww/repository/fww_study/build/test/CMakeFiles/sparse_matrix.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : test/CMakeFiles/sparse_matrix.dir/depend

