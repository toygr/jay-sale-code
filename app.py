from pymongo import MongoClient
from pymongo.server_api import ServerApi
from tabulate import tabulate
from dotenv import load_dotenv
import os
import random
import argparse

load_dotenv()
parser = argparse.ArgumentParser(description="Your script description")
parser.add_argument("--name", help="Investor name")
parser.add_argument("--info", default="Nope", help="Additional info for investor")
parser.add_argument(
    "-c", "--create", action="store_true", help="Additional info for investor"
)

# Parse the arguments
args = parser.parse_args()

conn = os.getenv("MONGODB_URL")
client = MongoClient(conn, server_api=ServerApi("1"))

db = client["jay-sol"]
collection = db["users"]
schema = {"code": int, "name": str, "info": str}

documents = collection.find({})
if args.create:
    if not args.name:
        print("Name not provided")
        exit()
    codes = [v["code"] for v in documents if v.get("code")]
    while True:
        code = random.randrange(1000000, 10000000)
        if not code in codes:
            break
    document = {"code": code, "name": args.name, "info": args.info}
    result = collection.insert_one(document)
    if result.inserted_id:
        print(
            f"Created new investor info!\ncode: {code}, Name: {args.name}, Info: {args.info}"
        )

documents = [
    {"code": f"{v.get("code")}", "name": v.get("name"), "info": v.get("info")}
    for v in documents
    if v.get("code")
]

# Process and print the documents
document = {"code": "Code", "name": "Name", "info": "Info"}
documents.insert(0, document)
print(tabulate(documents, headers="firstrow", tablefmt="grid"))

client.close()
