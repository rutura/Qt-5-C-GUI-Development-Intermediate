cmake_minimum_required(VERSION 3.5)

project(1-11Classes-part3 LANGUAGES CXX)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(1-11Classes-part3 main.cpp box.h rectangle.h square.h rectangle.cpp)
