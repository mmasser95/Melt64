#-------------------------------------------------------------------------------
# Name:        Melt64
#
# Author:      mmasser95
#
# Created:     07/10/2014
#                                                                           
# Licence:     GPLv3
#-------------------------------------------------------------------------------
import random, os
import string
class CreateKey:

    def __init__(self, name):
        self.d = {}
        self.e = {}
        self.allChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz1234567890"
        if os.path.exists('D:\\' + name + '.txt') == True:
            self.Importar(name)
            
        if os.path.exists('D:\\' + name + '.txt') == False:
            self.Exportar(name)
            

        
        
    def Crear(self):

        a=0
        while a < 63:
            self.d[self.allChar[a]] = self.allChar[random.randint(0,62)] + self.allChar[random.randint(0,62)] + self.allChar[random.randint(0,62)]
            x = self.d[self.allChar[a]]
            self.e[x] = self.allChar[a]
            a = a +1
        
    def Encriptar(self, sms):
        a = 0
        crypt = ''
        sms = str(sms)
        #print 'Original Message: ' + sms
        while a < len(sms):
            crypt = crypt + self.d[sms[a]]
            a = a+1
        #print 'Encripted Message: ' + crypt
        return crypt
        
    def Desencriptar(self, miss):
        a = 0
        crypt = ''
        #print 'Original Message: ' + miss
        while a < len(miss):
            crypt = crypt + self.e[miss[a:a+3]]
            a = a + 3
        #print 'Desencripted Message: ' + crypt
        return crypt

    def Exportar(self, name):
        self.Crear()
        a = 0
        self.fole = open("D:\\" + name + ".txt", "wb")
        while a < 63:
            x = self.d[self.allChar[a]]
            self.fole.write(x)
            a = a + 1
        self.fole.close
            
            
    def Importar(self,name):
        self.flole = open('D:\\' + name + '.txt', 'r')
        x = self.flole.read()
        a = 0
        b = 0
        while a < len(x):
            self.d[self.allChar[b]] = x[a:a+3]
            self.e[x[a:a+3]] = self.allChar[b]
            b = b +1
            a = a +3
