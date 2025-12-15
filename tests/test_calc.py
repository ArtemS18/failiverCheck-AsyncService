import pytest
from app.service import calculate_avalilable
from app.schema import ComponentsToSystemCalcList, ComponentsToSystemCalc, Component

@pytest.mark.asyncio
async def test_ok_calculation():
    mtbf = 100
    mttr = 100
    available = float(mtbf) / float(mtbf + mttr)
    result =  float (1 - (float(1-available) ** float(1)))

    items = ComponentsToSystemCalcList(
        id=1, 
        components=[
            ComponentsToSystemCalc(
                replication_count=1, 
                component_data=Component(
                    id=0, 
                    title="test", 
                    type="test", 
                    mtbf=mtbf, 
                    mttr=mttr, 
                    available=available
                    )
                )
            ]
        )
    test_result = await calculate_avalilable(items)
    assert test_result == result

@pytest.mark.asyncio
async def test_ok_without_available_calculation():
    mtbf = 100
    mttr = 100
    available = float(mtbf) / float(mtbf + mttr)
    result =  float (1 - (float(1-available) ** float(1)))

    items = ComponentsToSystemCalcList(
        id=1, 
        components=[
            ComponentsToSystemCalc(
                replication_count=1, 
                component_data=Component(
                    id=0, 
                    title="test", 
                    type="test", 
                    mtbf=mtbf, 
                    mttr=mttr, 
                    available=0
                    )
                )
            ]
        )
    test_result = await calculate_avalilable(items)
    assert test_result == result
