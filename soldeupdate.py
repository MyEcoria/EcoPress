import pyetherbalance 
# Sign up for https://infura.io/, and get the url to an ethereum node
infura_url = 'https://ropsten.infura.io/v3/c9c9b80644a14798be4d0f7bee4997d6'
ethereum_address = '0x880cA9F202d09A10FA80Fe0407d04f1a20c9957E'
# Create an pyetherbalance object , pass the infura_url
ethbalance = pyetherbalance.PyEtherBalance(infura_url)
# get ether balance
balance_eth = ethbalance.get_eth_balance(ethereum_address)


counter = str(balance_eth)
specialChars = "'"
specialChars1 = "{"
specialChars2 = "}"
for specialChar in specialChars:
    txt = counter.replace(specialChars, '"')
    txt1 = txt.replace(specialChars1, '[{')
    txt2 = txt1.replace(specialChars2, '}]')    
print(txt2)
fichier = open("ethsolde.json", "w")
fichier.write(txt2)
fichier.close()
