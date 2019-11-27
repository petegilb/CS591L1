.PHONY: help
help:
	@echo "Use: 'make n=<n> run1' to run the first intro with parameter <n>"
	@echo "Use: 'make n=<n> run2' to run the second intro (vector addition) on vectors of size n"

run: helloworld.o
	./helloworld.o

run1: cintro1.o
	./cintro1.o ${n}

run2: cintro2.o
	./cintro2.o ${n}

helloworld.o: helloworld.cpp
	clang++ helloworld.cpp -o helloworld.o

cintro1.o: cintro1.cpp
	clang++ cintro1.cpp -o cintro1.o

cintro2.o: cintro2.cpp
	clang++ cintro2.cpp -o cintro2.o

.PHONY: clean
clean:
	rm -rf *.o
