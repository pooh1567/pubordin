
from hashlib import sha256
import random



class BlockChin:
    blockNo=0
    nonce=0
    transaction=None
    previous_hash=None
    hash=None
    timestamp=str(datetime.datetime.now())
    
    blockchainList=[]

    def __init__(self):
        self.blockNo=1
        self.nonce=random.randint(0,100)
        self.previous_hash="000000000000000"
        self.timestamp=str(datetime.datetime.now())
    # def hashblock(self):
    #     newNonce=random.randint(1,1000000000000)
    #     hashtext=str(self.blockNo)+str(newNonce)+str(self.transaction)+str(self.previous_hash)+self.timestamp
    #     blockhash=sha256(hashtext.encode()).hexdigest()

        # self.hash=blockhash
        # self.nonce=newNonce

    def addToBlockkchain(self):
        block={
            'blockNo':self.blockNo,
            'nonce':self.nonce,
            'previous_hash':self.previous_hash,
            'transaction':self.transaction,
            'timestamp':self.timestamp,
            'hash':self.hash
        }
        self.blockchainList.append(block)

    def create_newblock(self,data):
        self.blockNo=len(self.blockchainList)+1
        self.nonce=random.randint(0,100)
        self.previous_hash=self.blockchainList[-1]['hash']
        self.timestamp=str(datetime.datetime.now())
        self.transaction=data
        self.hash=None

        self.hashblock()
        self.addToBlockkchain()

    def hashblock(self):
    
        nonce_limit=100000000000
        zeroes=4
        for rand_nonce in range(nonce_limit):
            basetext=str(self.blockNo)+ str(self.transaction)+ str(self.previous_hash)+self.timestamp+str(rand_nonce)
            hashblock=sha256(basetext.encode()).hexdigest() 
            if hashblock.startswith('0'*zeroes):
                print(f" found hash with nonce {rand_nonce}")
            self.nonce=rand_nonce 
            self.hash=hashblock
            return hashblock        
        raise BaseException("Couldn't find correct hash after trying (nonce limit) times")

        def addTOBlockchin(self):
            block={
                'blockNo':self.blockNO,
                'nonce':self.nonce,
                'previous_hash':self.previous_hash,
                'transaction':self.transaction,
                'hash':self.hash,
                'timestamp':self.timestamp,
                }
# print('Build BlockChain')
block=BlockChin()
# print (block.blockNo)
# print (block.nonce)
# print (block.transaction)
# print (block.previous_hash)
# print (block.hash)
# print (block.timestamp)
# print (block.blockchainList)
# print('------------Hash Block-------------')
block.hashblock()
# print (block.blockNo)
# print (block.nonce)
# print (block.transaction)
# print (block.previous_hash)
# print (block.hash)
# print (block.timestamp)
# print (block.blockchainList)
# print('------------Add Block To BlcokList-------------')
block.addToBlockkchain()
# print (block.blockNo)
# print (block.nonce)
# print (block.transaction)
# print (block.previous_hash)
# print (block.hash)
# print (block.timestamp)
# print (block.blockchainList)
# print('------------Show Data Block In BlcokList-------------')
# print("Block ID : ",block.blockchainList[0]['blockNo'])
# print("Nonce : ",block.blockchainList[0]['nonce'])
# print("Transaction : ",block.blockchainList[0]['transaction'])
# print("Previous Hash : ",block.blockchainList[0]['previous_hash'])
# print("Hash : ",block.blockchainList[0]['hash'])
# print("TimeStamp : ",block.blockchainList[0]['timestamp'])

# สร้าง block ใหม่

newtransaction="I'm ATOMIC"
block.create_newblock("I")
block.create_newblock("LOVE")
block.create_newblock("YOU")
block.create_newblock("TO")
block.create_newblock("BE")

for block in block.blockchainList:
    
   
    print('show data')
    print("Block ID",block['blockNo'])
    print("Nonce",block['nonce'])
    print("Transaction",block['transaction'])
    print("Preveishash",block['previous_hash'])
    print("hash",block['hash'])
    print("TimeStamp",block['timestamp'])
  
#  i=0
# while i<len(block.blockchainList):
#     print("หมายเลข block:",block.blockchainList[i]['blockNo'])
#     print("ค่าblock:",block.blockchainList[i]['nonce'])
#     print("ข้อมูล block:",block.blockchainList[i]['transaction'])
#     print("Previous hash :",block.blockchainList[i]['previous_hash'])
#     print("hash ของ block:",block.blockchainList[i]['hash'])
#     print("เวลาที่สร้าง block:",block.blockchainList[i]['timestamp'])
    
#     i=i+1
    
    print("")    
    #
    #
    
