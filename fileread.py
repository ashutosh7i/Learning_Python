#reading from a file
readFile = open('test.txt','r').read();
#r means read
print(readFile);
#prints that file

#using readlines method
readLines=open('test.txt','r').readlines();
print(readLines);