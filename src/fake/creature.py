from model.creature import Creature

_creatures = [
    Creature(
        name="Bigfoot",
        country="US",
        area="Pacific Northwest",
        description="Hairy and elusive",
        aka="Sasquatch",
    ),
    Creature(
        name="Loch Ness Monster",
        country="UK",
        area="Loch Ness",
        description="Long-necked and scaly",
        aka="Nessie",
    ),
    Creature(
        name="yeti",
        country="Nepal",
        area="Himalayas",
        description="Tall, white, furry",
        aka="Abominable Snowman",
    ),
]


def get_all() -> list[Creature]:
    """Return all creatures"""
    return _creatures


def get_one(name: str) -> Creature | None:
    """Return one creature"""
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None


# The following are nonfunctional for now,
# so they just act like they work, without modifying
# the actual fake _creatures list:
def create(creature: Creature) -> Creature:
    """Add a creature"""
    return creature


def modify(creature: Creature) -> Creature:
    """Partially modify a creature"""
    return creature


def replace(creature: Creature) -> Creature:
    """Completely replace a creature"""
    return creature


def delete(name: str):
    """Delete a creature; return None if it existed"""
    return None
