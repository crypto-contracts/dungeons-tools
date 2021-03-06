from flask import request

from flask import (
    Blueprint
)

from . import services
import json

bp = Blueprint('airdrop', __name__, url_prefix='/airdrop')

@bp.route('/monster_holder', methods=["GET"])
def monster_holder():
    base = request.args.get('base', 200)
    endblock = request.args.get('endblock', 0)

    items = services.get_monster_holders(int(endblock))
    
    return json.dumps([{
        'index': i+1, 'address': e.holder_address, 'count': e.count, 
        'amount': services.cal_monster_holder_rewards(e.count, int(base))} for i, e in enumerate(items)])

@bp.route('/dungeons_interaction', methods=["GET"])
def dungeons_interaction():
    base = request.args.get('base', 50)
    endblock = request.args.get('endblock', 0)

    items = services.get_dungeons_interactions(endblock)
    
    return json.dumps([{
        'index': i+1, 'address': e.called_from, 'count': e.count, 
        'amount': services.cal_dungeons_interaction_rewards(e.count, int(base))} for i, e in enumerate(items)])


@bp.route('/rarity_holder', methods=["GET"])
def rarity_holder():
    base = request.args.get('base', 4)

    items = services.get_rarity_holders()
    
    return json.dumps([{
        'index': i+1, 'address': e.holder_address, 'max_level': e.max_level, 
        'amount': services.cal_rarity_holder_rewards(e.max_level, int(base))} for i, e in enumerate(items)])