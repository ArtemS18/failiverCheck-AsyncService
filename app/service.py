import asyncio
from httpx import AsyncClient, Response
from app.schema import Component, ComponentsToSystemCalcList, ResultRequest
from app import config
from logging import getLogger


log = getLogger(__name__)

async def calculate_avalilable(items: ComponentsToSystemCalcList) -> float:
    system_available: float = 1
    for el in items.components:
        component: Component = el.component_data
        available = component.available
        if available == 0:
            if component.mtbf == 0 or component.mtbf + component.mttr == 0:
                raise 
            available = float(component.mtbf) / float(component.mtbf + component.mttr)
        component_available = float (1 - (float(1-available) ** float(el.replication_count)))
        system_available *= component_available
    return system_available

async def send_results(items: ComponentsToSystemCalcList, time_sleep: int = 10):
    system_available = await calculate_avalilable(items)
    log.info("Calculate : %s", system_available)
    await asyncio.sleep(time_sleep)

    async with AsyncClient() as client:
        resp: Response = await client.put(
            config.WEBHOOK_URL, 
            json=ResultRequest(
                available_calc=system_available, 
                token=config.TOKEN, 
                sustem_calc_id=items.id
            ).model_dump()
        )
        log.info("Respone : %s", resp.json())
