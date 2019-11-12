run: test.o
	CILK_NWORKERS=${w} ./test.o ${n}

test.o: test.cpp
	clang++ -fcilkplus test.cpp -o test.o

.PHONY: help
help:
	@echo "Use: 'make w=<WORKERS> n=<fib index> run' to run"

.PHONY: clean
clean:
	rm -rf test.o

