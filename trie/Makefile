# C++ Compiler
CXX := g++

# Flags
CXXFLAGS += -std=c++11
CXXFLAGS += -pedantic -Wall -Wextra -Wcast-align -Wcast-qual -Wctor-dtor-privacy -Wdisabled-optimization -Wformat=2 -Winit-self -Wlogical-op -Wmissing-declarations -Wmissing-include-dirs -Wnoexcept -Wold-style-cast -Woverloaded-virtual -Wredundant-decls -Wshadow -Wsign-conversion -Wsign-promo -Wstrict-null-sentinel -Wstrict-overflow=5 -Wswitch-default -Wundef -Werror -Wno-unused

# Program name
EXE := trie.out

# Directories:
#   Sources
SRCDIR := src

#   Binary
BINDIR := bin
################################################################################

SRCS := $(wildcard $(SRCDIR)/*.cpp)

.PHONY: all clean distclean

build: $(BINDIR)/$(EXE)

$(BINDIR)/$(EXE):
	mkdir -p $(BINDIR)
	$(CXX) $(SRCS) $(CXXFLAGS) -o $@

clean:
	rm -f $(BINDIR)/$(EXE)

debug:
	valgrind $(BINDIR)/$(EXE)
