import tcod as libtcod
from game_messages import Message


def heal(*args, **kwargs):
    entity = args[0]
    amount = kwargs.get('amount')

    results = []

    if entity.fighter.hp == entity.fighter.max_hp:
        results.append({'consumed': True, 'message': Message('Potion has no affect. You are already at full health',
                         libtcod.yellow)})
    else:
        entity.fighter.heal(amount)
        results.append({'consumed': True, 'message': Message('You consume potion. Health increased', libtcod.green)})

    return results