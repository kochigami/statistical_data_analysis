###
CXX := g++
SRC := $(wildcard *.cpp)
TARGET := $(SRC:.cpp=)
OBJ := $(SRC:.cpp=.o) 

CXXFLAGS :=`pkg-config --cflags opencv` 
LDFLAGS := `pkg-config --libs opencv`

## $(SRC:.cpp=.o) = test.cpp - .cpp + .o

###
all:$(TARGET)

fill_in_color:fill_in_color.o
	$(CXX) -o $@ $< $(LDFLAGS)
test2:test2.o
	$(CXX) -o $@ $< $(LDFLAGS)
gaussian:gaussian.o
	$(CXX) -o $@ $< $(LDFLAGS)
face_detection:face_detection.o
	$(CXX) -o $@ $< $(LDFLAGS)

.cpp.o:
	$(CXX) -o $@ -c $< $(CXXFLAGS)

## $@ is current target file
## $< is current dependent file (file no moto)
## .cpp.o: if .o file is required, it is created from .cpp file (suffix rule)
## g++ -o test.o -c test.cpp `pkg-config --cflags opencv`
## $(TARGET): $(OBJ) (= test.o) -> g++ -o test test.o `pkg-config --libs opencv
## $(TARGET): $(OBJ)
##	$(CXX) -o $(TARGET) $(OBJ) $(LDFLAGS) 
### main: main.cpp
###     g++ -o main main.cpp `pkg-config --cflag opencv` `pkg-config --libs opencv`
###

###
.PHONY: clean #clean isn't an existing file. clean is defined as a task target
clean:
	$(RM) *.o $(TARGET)
