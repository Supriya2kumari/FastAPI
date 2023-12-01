from fastapi import FastAPI
import motor.motor_asyncio
  
app = FastAPI()

client = motor.motor_asyncio.AsyncIOMotorClient()
db = client.test_database
collection = db.test_collection

async def do_insert():
    document = {"_id" : id}
    result = await collection.insert_one(document)
    return result.inserted_id

async def do_find_one():
    result = await collection.find_one({"i":{"$lt":1}})
    return result

async def do_update():
    result = await collection.replace_one({"_id":id},{"key":"value"})
    return result.modifeid_count

async def do_delete_one():
    result = await collection.delete_one({"_id":id})
    return result.deleted_count