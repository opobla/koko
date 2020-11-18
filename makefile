all: maths 

maths.o: maths.c
	gcc maths.c -c -o maths.o

kokocode.o: kokocode.c
	gcc kokocode.c -c -o kokocode.o

lolocode.o: lolocode.c
	gcc lolocode.c -c -o lolocode.o

pepecode.o: pepecode.c
	gcc pepecode.c -c -o pepecode.o

maths: maths.o kokocode.o lolocode.o pepecode.o
	gcc maths.o kokocode.o lolocode.o pepecode.o -o maths

clean:
	rm -f *.o
	rm -f maths
	rm -f distribution.tgz

dist:
	tar zcvf distribution.tgz *