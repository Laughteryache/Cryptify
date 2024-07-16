from fastapi import APIRouter
from src.utils.cmc_api import cmc_client


router = APIRouter(tags=['Crypto'],
                   prefix="/crypto")


@router.get("")
async def cryptocurrencies():
    return await cmc_client.get_listings()


@router.get("/crypto/{currency_id}")
async def get_cryptocurrency(currency_id: int):
    return await cmc_client.get_currency(currency_id=currency_id)