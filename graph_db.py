from neo4j.v1 import GraphDatabase
from config import username, password

driver = GraphDatabase.driver("bolt://localhost:7687", auth=(username, password))
