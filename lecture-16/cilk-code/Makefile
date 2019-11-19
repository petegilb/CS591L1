.PHONY: help
help:
	@echo "Use: 'make w=<WORKERS> n=<fib index> run-fib' to run fibonacci, a good n here would be ~40"
	@echo "Use: 'make w=<WORKERS> n=<size of vectors> run-vadd' to run vector addition, a good n here would be 100M to 400M"

# Takes two command line arguments, w and n
# w=the number of workers
# n=index in fibonacci
run-fib: fib.o
	CILK_NWORKERS=${w} ./fib.o ${n}

# Takes two command line arguments, w and n
# w=the number of workers
# n=size of the vectors
run-vadd: vadd.o
	CILK_NWORKERS=${w} ./vadd.o ${n}

fib.o: fib.cpp
	clang++ -fcilkplus fib.cpp -o fib.o

vadd.o: vadd.cpp
	clang++ -fcilkplus vadd.cpp -o vadd.o

.PHONY: clean
clean:
	rm -rf *.o
