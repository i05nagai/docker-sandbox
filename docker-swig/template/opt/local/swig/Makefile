CC := g++
INC_PATH := -I /usr/include/python3.6 -I ./cpp/
# LIB_PATH=-L ./python
# LIBS=-lapr-1 -laprutil-1
CFLAGS := -Wall -Wextra -g $(INC_PATH) -std=c++11
# CFLAGS=-Wall -Wextra -g -O2 -DNDEBUG $(INC_PATH)
SWIG_INTERFACES := $(wildcard cpp/*.i)
SWIG_SOURCES := $(patsubst %.i, %_wrap.cc, $(SWIG_INTERFACES))

EXAMPLE_SWIG_INTERFACES := $(wildcard cpp/*.i)
EXAMPLE_SWIG_SOURCES := $(patsubst %.i, %_wrap.cc, $(EXAMPLE_SWIG_INTERFACES))
EXAMPLE_SOURCES := $(filter-out $(EXAMPLE_SWIG_SOURCES),$(wildcard cpp/*.cc))
EXAMPLE_OBJECTS := $(patsubst %.cc, %.o, $(EXAMPLE_SOURCES) $(EXAMPLE_SWIG_SOURCES))
EXAMPLE_LIB := python/_example.so

CORE_SWIG_INTERFACES := $(wildcard cpp/core/*.i)
CORE_SWIG_SOURCES := $(patsubst %.i, %_wrap.cc, $(CORE_SWIG_INTERFACES))
CORE_SOURCES := $(filter-out $(CORE_SWIG_SOURCES),$(shell find cpp/core -name *.cc))
CORE_OBJECTS := $(patsubst %.cc, %.o, $(CORE_SOURCES) $(CORE_SWIG_SOURCES))
CORE_LIB := python/_core.so

NS1_SWIG_INTERFACES := $(wildcard cpp/ns1/*.i)
NS1_SWIG_SOURCES := $(patsubst %.i, %_wrap.cc, $(NS1_SWIG_INTERFACES))
NS1_SOURCES := $(filter-out $(NS1_SWIG_SOURCES),$(shell find cpp/ns1 -name *.cc))
NS1_OBJECTS := $(patsubst %.cc, %.o, $(NS1_SOURCES) $(NS1_SWIG_SOURCES))
NS1_LIB := python/_ns1.so

OBJECTS := $(NS1_OBJECTS) $(EXAMPLE_OBJECTS) $(CORE_OBJECTS)
SWIG_SOURCES := $(EXAMPLE_SWIG_SOURCES) $(NS1_SWIG_SOURCES) $(CORE_SWIG_SOURCES)
SHARED_LIB := $(NS1_LIB) $(EXAMPLE_LIB) $(CORE_LIB)

.PHONY: all

all: $(SHARED_LIB)

$(CORE_LIB): $(CORE_OBJECTS)
	$(CC) $(CFLAGS) -shared $(LIB_PATH) $(LIBS) $^ -o $@

$(NS1_LIB): $(NS1_OBJECTS) $(CORE_OBJECTS)
	$(CC) $(CFLAGS) -shared $(LIB_PATH) $(LIBS) $^ -o $@

$(EXAMPLE_LIB): $(EXAMPLE_OBJECTS)
	$(CC) $(CFLAGS) -shared $(LIB_PATH) $(LIBS) $^ -o $@

$(SWIG_SOURCES): %_wrap.cc:%.i
	swig -c++ -cppext cc -python -outdir python $<

%.o: %.cc
	$(CC) $(CFLAGS) -fPIC -c $< -o $@

clean:
	rm -f $(OBJECTS) $(SHARED_LIB) $(SWIG_SOURCES)
