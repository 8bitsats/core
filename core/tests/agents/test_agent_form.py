
import pytest

from tests.agents.agent_fixtures import main_agent, stray

@pytest.mark.asyncio
async def test_execute_form_agent(main_agent, stray):
    assert True  # TODO: this is going to be a mess
