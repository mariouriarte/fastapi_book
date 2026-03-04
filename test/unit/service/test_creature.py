import os
import pytest
from model.creature import Creature
from service import creature as code
import data.init as init
# os.environ["CRYPTID_SQLITE_DB"] = ":memory:"

@pytest.fixture(autouse=True)
def set_up_db():
    """Set up an in-memory database for each test."""
    os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
    init.get_db(reset=True) # Ensure a fresh in-memory connection
    yield
    # No explicit teardown needed for :memory: as it's discarded after the session

@pytest.fixture
def sample() -> Creature:
    return Creature(name="FUEReti", country="CN", area="Himalayas",
        description="Harmless Himalayan",
        aka="Abominable Snowman")

def test_obv():
    assert 1 == 1

def test_create(sample: Creature):
    resp = code.create(sample)
    assert resp == sample
#
# def test_get_exists():
#     resp = code.get_one("Yeti")
#     assert resp == sample
#
# def test_get_missing():
#     resp = code.get_one("boxturtle")
#     assert resp is None
