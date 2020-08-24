import substrateinterface as si
import datetime

sub = {'substrate_dao': si.SubstrateInterface(url="wss://substrate.ipci.io"),
       'substrate_robonomics': si.SubstrateInterface(url="wss://vladivostok-rpc.robonomics.network")}


def get_network_status(substrate):
    network = sub.get(substrate)
    parachain_name = network.rpc_request(
        method='system_chain',
        params=[],
        result_handler=None
    ).get('result')

    version = network.rpc_request(
        method='system_version',
        params=[],
        result_handler=None
    ).get('result')

    token = network.rpc_request(
        method='system_properties',
        params=[],
        result_handler=None
    ).get('result')['tokenSymbol']

    peers_count = network.rpc_request(
        method='system_health',
        params=[],
        result_handler=None
    ).get('result')['peers']

    block_hash = network.get_chain_head()
    block_number = network.get_block_number(block_hash)
    try:
        block_timestate = network.get_runtime_block(block_hash)['block']['extrinsics'][0]['params'][0]['value']
    except Exception:
        block_timestate = 'none'
    return parachain_name, version, token, peers_count, block_hash, block_number, block_timestate
