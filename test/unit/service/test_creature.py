import os
os.environ["CRYPTID_UNIT_TEST"] = "true"
from fastapi import HTTPException
import pytest

from model.creature import Creature
from errors import Missing, Duplicate

# os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
# from data import creature as data
from web import creature

@pytest.fixture
def sample() -> Creature:
    return Creature(name="dragon",
        aka="firedrake",
        country="*",
        area="*",
        description="Wings! Fire!")

@pytest.fixture
def fakes() -> list[Creature]:
    return creature.get_all()

def test_create(sample):
    assert creature.create(sample) == sample

def test_create_duplicate(fakes):
    with pytest.raises(HTTPException) as exc:
        _ = creature.create(fakes[0])
        assert exc.value.status_code == 404

def test_get_one(fakes):
    assert creature.get_one(fakes[0].name) == fakes[0]

def test_get_one_missing():
    with pytest.raises(HTTPException) as exc:
        _ = creature.get_one("bobcat")
        assert exc.value.status_code == 404
