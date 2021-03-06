from time import gmtime, strftime
import gzip

class Logger:
    def __init__(self,filen):
        if filen[-3:] != ".gz":
            filen += ".gz"
        self.filename = filen
        self.fl = None
    
    def a(self):
        self.fl = gzip.open(self.filename,"at")

    def whac(self,string):
        self.fl = gzip.open(self.filename,"at")
        self.fl.write("\n# "+string+"\n")
        self.c()

    def w(self,string):
        stt = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
        self.fl.write(stt+" || "+string+"\n")

    def wac(self,string):
        self.fl = gzip.open(self.filename,"at")
        self.w(string)
        self.c()

    def c(self):
        #stt = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
        #self.fl.write(stt+" || closing log\n")
        self.fl.close()
