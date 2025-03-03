from prisma import Prisma
import logging

prisma = Prisma()

async def connect_db():
    await prisma.connect()
    print("🟢 Conectado a la base de datos")

async def disconnect_db():
    await prisma.disconnect()
    print("🔴 Desconectado de la base de datos")