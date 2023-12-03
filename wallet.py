# beginig code : test old wallet
from bit import PrivateKeyTestnet, wif_to_key, Key
from bit.network import NetworkAPI

real_wallet = PrivateKeyTestnet('cN2S8bNDjws14uhF1zMNxFih6NFgBSM1myKcC26PR73oJj2Mr1ni')
print('wallet address : ',real_wallet.address)
print('wallet balance :', real_wallet.get_balance())
