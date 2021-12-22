from hashlib import sha256
import time


class block:
    def __init__(self,timeStamp,data,previousHash=''):
        self.timeStamp = timeStamp
        self.data = data
        self.previousHash = previousHash
        self.kuvvet = 0
        self.hash = self.hesapla()

    def hesapla(self):
        while True:
            self.kuvvet = self.kuvvet+1
            ozet = sha256((str(self.timeStamp)+str(self.data)+str(self.previousHash)+str(self.kuvvet)).encode()).hexdigest()
            if ozet[0:2] == "00":
                break
        return ozet

class blockchain:
    def __init__(self):
        self.chain=[self.GenesisOlustur()]

    def GenesisOlustur(self):
        return block(time.ctime(),"deliltoplama1"," ")

    def blockEkle(self,data):
        node = block(time.ctime(),data,self.chain[-1].hash)
        self.chain.append(node)

    def kontrol(self):
        for i in range(len(self.chain)):
            if i!=0:
                ilk = self.chain[i-1].hash
                suan=self.chain[i].previousHash
                if ilk!=suan:
                    return "ZINCIR KOPMUS"
                if sha256((str(self.chain[i].timeStamp)+str(self.chain[i].data)+str(self.chain[i].previousHash)+str(self.chain[i].kuvvet)).encode()).hexdigest() != self.chain[i].hash:
                    return "ZINCIR KOPMUS"
        return "ZINCIR SAGLAM"


    def listeleme(self):
        print("Blockchain")
        for i in range(len(self.chain)):
            print("--------------------")
            print("Block  =>  ",i,"\nHash = " ,str(self.chain[i].hash), "\n ZAMAN İMGECİ = " ,str(self.chain[i].timeStamp),"\nData = " ,str(self.chain[i].data),"\nKuvvet = " ,str(self.chain[i].kuvvet),"\nPreviousHash = " ,str(self.chain[i].previousHash))
            print("--------------------")

deliltoplama1 = blockchain()

while True:
    print("Lütfen seçiminizi yapınız \n Block eklemek için 1 \nBlockchaini görmek için 2 \nZinciri kontrol etmek için 3 \nSistemden çıkmak için 4")
    data = input()
    if data == "1":
        print("GÖNDERİLEN DELİLLERİ BULUNDUKLARI SIRAYA GÖRE GİRİNİZ = \n")
        delil = input()
        deliltoplama1.blockEkle(delil)
    elif data == "2":
        deliltoplama1.listeleme()
    elif data == "3":
        print(str(deliltoplama1.kontrol()))
    elif data=="4":
        break

