from fastapi import FastAPI
import uvicorn
from app.service.blockchain import Blockchain
from app.model.transaction import Transaction
app = FastAPI()
blockchain = Blockchain()

@app.get("/getChain")
async def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return {"length": len(chain_data),
            "chain": chain_data}


@app.post("/addChain")
async def add_chain(transaction : Transaction):
    blockchain.add_new_transaction(transaction.description)
    blockchain.mine()
    return transaction

@app.get("/")
def read_root():
    return {"Estado": "OK"}

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)