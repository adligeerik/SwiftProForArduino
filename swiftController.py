import serial
import threading
import logging
import socket


class Swift:

    def __init__(self):
        #self.ser = serial.Serial('/dev/ttyACM0')
        #elf.ser.baudrate = 115200
        self.speed = ' F10000000'
        self.xCoordinate = 0.0
        self.yCoordinate = 0.0
        self.zCoordinate = 0.0
        self.validPos = 0
        self.baseAngle = 0
        self.isExecuted = True
        self.echo = False
        self.verbose = 0 # 0 nothing , 1 all

        self.ip = "192.168.10.127"
        self.port = 8002
        self.buf = 1024
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip,self.port))

    def setEcho(self, echo):
        self.echo = echo

    def setVerbose(self, val):
        self.verbose = val

    def speed(self, newspeed):
        self.speed = newspeed

    def moveXYZRel(self, x, y, z, e, speed):
        if speed == '':
            speed = self.speed

        command = 'G2204 X'+ str(x)+ ' Y'+ str(y)+ ' Z'+ str(z) +' E'+ str(e) + speed +'\r\n'
        self.sendCommand(command)

    def moveZRel(self, dist):
        command = 'G2204 Z'+ str(dist) + self.speed +'\r\n'
        self.sendCommand(command)

    def moveXRel(self, dist):
        command = 'G2204 X'+ str(dist) + self.speed +'\r\n'
        self.sendCommand(command)

    def moveYRel(self, dist):
        command = 'G2204 Y'+ str(dist) + self.speed +'\r\n'
        self.sendCommand(command)

    def moveERel(self, dist):
        command = 'G2204 E'+ str(dist) + self.speed +'\r\n'
        self.sendCommand(command)

    def detach(self):
        command = 'M2019\r\n'
        self.sendCommand(command)

    def attach(self):
        command = 'M17\r\n'
        self.sendCommand(command)

    def moveToPos(self, X, Y, Z, E, speed = ""):
        if speed == '':
            speed = self.speed

        command = 'G0 X'+ str(X)+ ' Y'+ str(Y) +' Z' + str(Z)+' E' + str(E)+ speed+'\r\n'
        self.sendCommand(command)

    def moveXToPos(self, coordinate, speed = ""):
        if speed == '':
            speed = self.speed

        command = 'G0 X'+ str(coordinate) + speed+'\r\n'
        self.sendCommand(command)

    def moveYToPos(self, coordinate, speed = ""):
        if speed == '':
            speed = self.speed

        command = 'G0 Y'+ str(coordinate) + speed+'\r\n'
        self.sendCommand(command)

    def moveZToPos(self, coordinate, speed = ""):
        if speed == '':
            speed = self.speed

        command = 'G0 Z'+ str(coordinate) + speed+'\r\n'
        self.sendCommand(command)

    def moveEToPos(self, coordinate, speed = ""):
        if speed == '':
            speed = self.speed

        command = 'G0 E'+ str(coordinate) + speed+'\r\n'
        self.sendCommand(command)


    def moveSquare(self, dist):
        self.sendCommand('G2204 X'+ str(dist) + self.speed +'\r\n')
        self.sendCommand('G2204 Y'+ str(dist) + self.speed +'\r\n')
        self.sendCommand('G2204 X-'+ str(dist) + self.speed +'\r\n')
        self.sendCommand('G2204 Y-'+ str(dist) + self.speed +'\r\n')

    def stopPos(self):
        command = 'M2120 V'+str(0)+'\r\n'
        self.sendCommand(command)

    def startPos(self, interval):
        command = 'M2120 V'+str(interval)+'\r\n'
        self.sendCommand(command)
        #self.thread = threading.Thread(target = self.readFromPort, args=(self.ser,))
        self.thread = threading.Thread(target = self.readFromPort, args=(self.socket,))
        self.thread.daemon = True
        self.thread.start()
        self.enableComFin()

    def kill(self):
        command = 'M112'
        self.sendCommand(command)

    def readFromPort(self, socket):
        
        while 1:
            #line = ser.readline()
            line = socket.recv(self.buf)
            logging.info('Uarm response: '+ line)
            if self.verbose:
                print(line)

            if 'Unknown command' in line:
                self.isExecuted = True
                #TODO resend command
            
            elif 'E22' in line:
                logging.warning('Unreachable')
                if self.verbose:
                    print('warning unreachable')

            elif '@9' in line:
                #pass
                logging.warning('@9 recieved')
                self.isExecuted = True

            elif 'ok' in line or '@3' in line:
                splited = line.split(' ')
                if len(splited) > 1:
                    #print(line)
                    try:
                        if splited[1][0] == 'V':
                            self.baseAngle = float(splited[1][1:len(splited[1])])
                            #print(self.baseAngle)
                        if splited[1][0] == 'X':
                            self.xCoordinate = float(splited[1][1:len(splited[1])])
                        if splited[2][0] == 'Y':
                            self.yCoordinate = float(splited[2][1:len(splited[2])])
                        if splited[3][0] == 'Z':
                            self.zCoordinate = float(splited[3][1:len(splited[3])])
                        self.validPos = 1
                        self.isExecuted = True
                    except KeyboardInterrupt:
                        raise
                    except:
                        pass
                        #TODO better catch than pass


    def fetchPos(self,line):
        pass    
                    
    def comCheck(self):
        return self.isExecuted

    #def getSer(self):
    #    return self.ser

    def checkValidPos(self):
        return self.validPos

    def zeroing(self):
        command = 'M2401 B\r\n'
        self.sendCommand(command)

    def enableComFin(self):
        command = 'M2122 V1 \r\n'
        self.sendCommand(command)

    def disableComFin(self):
        command = 'M2122 V0 \r\n'
        self.sendCommand(command)

    def checkAngle(self):
        command = 'P2206 N0\r\n'
        self.sendCommand(command)

    def getPos(self):
        return self.xCoordinate, self.yCoordinate, self.zCoordinate

    def sendCommand(self,command):
        #self.ser.write(command + 'P2220\r\n')
        self.socket.send(command)
        logging.info('Command: '+command)
        if self.echo == True:
            print(command)

        #while not self.isExecuted:
        #    a = 0
        #self.isExecuted = False

    def servoAngle(self,angle):
        command = 'G2202 N3 V' + str(angle) + '\r\n'
        self.sendCommand(command)