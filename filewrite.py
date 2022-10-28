#opening a file, writing to it , saving it and closing
#creating/opening a file, giving it name and using that to perform methods on that name
#opening with w for write mode
OpenFile = open('test.txt','w');
#writing data to file
OpenFile.write("Hello world, python wrote this");
#closing file
OpenFile.close();