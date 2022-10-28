#opening a file, writing to it , saving it and closing
#creating/opening a file, giving it name and using that to perform methods on that name
#opening with w for write mode
OpenFile = open('test.txt','a');
#writing data to file
OpenFile.write("\nHello world, append wrote this");
#closing file
OpenFile.close();   

#everything is same, we just have to change w with a, to append