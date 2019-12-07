CC=g++
INC_PATH=-I /usr/include/python3.6
# LIB_PATH=-L/usr/lib/x86_64-linux-gnu/
# LIBS=-lapr-1 -laprutil-1
CFLAGS=-Wall -Wextra -g $(INC_PATH)
# CFLAGS=-Wall -Wextra -g -O2 -DNDEBUG $(INC_PATH)
#
SWIG_INTERFACES := $(wildcard cpp/*.i)
SWIG_SOURCES := $(patsubst %.i, %_wrap.cc, $(SWIG_INTERFACES))

SOURCES := $(filter-out $(SWIG_SOURCES),$(wildcard **/*.cc))
OBJECTS := $(patsubst %.cc, %.o, $(SOURCES) $(SWIG_SOURCES))

LIBRARIES := $(addsuffix .so, $(shell basename -s .i $(SWIG_INTERFACES)))
SHARED_LIB := $(addprefix python/_,$(LIBRARIES))


all: $(SHARED_LIB)

$(SHARED_LIB): $(OBJECTS)
	$(CC) $(CFLAGS) -shared $(LIB_PATH) $(LIBS) $(OBJECTS) -o $@

$(SWIG_SOURCES): %_wrap.cc:%.i
	swig -c++ -cppext cc -python -outdir python $<

$(OBJECTS): %.o: %.cc
	$(CC) $(CFLAGS) -fPIC -c $< -o $@

clean:
	rm -f $(OBJECTS) $(SHARED_LIB) $(SWIG_SOURCES)
