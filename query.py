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
    block_timestate = network.get_runtime_block(block_hash)['block']['extrinsics'][0]['params'][0]['value']

    return parachain_name, version, token, peers_count, block_hash, block_number, block_timestate

if  __name__ == '__main__':
    network = si.SubstrateInterface(url="wss://vladivostok-rpc.robonomics.network")
    #version = si.SubstrateInterface(url="wss://vladivostok-rpc.robonomics.network").rpc_request(
    #    method='chain_getBlock',
   #     params=[],
   #     result_handler=None
   #)
    block_hash = network.get_chain_finalised_head()
    print(block_hash)
    block_number = network.get_runtime_block(block_hash)['block']['extrinsics'][0]['params'][0]['value']
    print(block_number)
    timestamp = 1598264150.041
    value = datetime.datetime.fromtimestamp(timestamp)
    print(value.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])

    #{'block': {'extrinsics': [{'valueRaw': '040200', 'extrinsic_length': 10, 'version_info': '04', 'call_code': '0200',
    #                           'call_function': 'set', 'call_module': 'timestamp',
     #                          'params': [{'name': 'now', 'type': 'Compact<Moment>',