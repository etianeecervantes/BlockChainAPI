from fastapi import FastAPI, status, HTTPException, Depends
from app.blockchain import Blockchain
from model.transaction import Transaction

app = FastAPI()
blockchain = Blockchain()

@app.get("/getChain", status_code=status.HTTP_200_OK)
async def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return {"length": len(chain_data),
            "chain": chain_data}


@app.post("/addChain", status_code=status.HTTP_201_CREATED)
async def add_chain(transaction : Transaction):
    blockchain.add_new_transaction(transaction.description)
    blockchain.mine()
    return transaction