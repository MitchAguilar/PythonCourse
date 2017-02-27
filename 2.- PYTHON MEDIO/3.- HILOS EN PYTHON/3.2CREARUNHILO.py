import threading
import time

class MiHilo(threading.Thread):
    def run(self):
        print("{} inició".format(self.getName()));
        time.sleep(1)
        print("{} Terminó".format(self.getName()))
if __name__=="__main__":
    for x in range(4):
        hilo=MiHilo(name="Thread-{}".format(x+1))
        hilo.start()
        time.sleep(.99)

#cuidado con la sintaxis tarado y revisa el codigo porque se puede reventar menso
             
