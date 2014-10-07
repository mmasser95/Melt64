import Melt64

def main():
    KeyName = str(raw_input('Insert the KeyName: '))
    MessageO = str(raw_input('Insert the Message: '))
    Key = Melt64.CreateKey(KeyName)
    MessageE = Key.Encriptar(MessageO)
    MessageD = Key.Desencriptar(MessageE)
    print 'The original message is: ' + MessageO
    print 'The encripted message is : ' + MessageE
    print 'The desencripted message is: ' + MessageD

if __name__ == '__main__':
    main()
