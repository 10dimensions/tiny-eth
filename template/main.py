'''
A core concept in blockchains is the ability to store and access a historical record of account balances. Design a structure allows setting and retrieving the latest value at a certain block height.

  `set(account, balance)`
  `get(account, height)`
  `increment_height()`
'''
'''
// **Example flow:**

// - `initialize` → height=0
// - `set(A, 1)`
// - `increment_height()`
// - `set(B, 2)`
// - `increment_height()`
// - `set(A, 3)`
// - `increment_height()`
// - `get(A, 0)` → returns 1
// - `get(B, 0)` → returns 0
// - `get(B, 1)` → returns 2
// - `get(A, 1)` → returns 1
// - `get(B, 2)` -> returns 2
// - `get(A, 2)` → returns  3
'''


class Block:

  def __init__(self):
    self.state = {}

  #Update account states
  def update_state(self, address, balance):
    self.state[address] = balance


class Blockchain:

  def __init__(self):
    self.blocks = []

  #Get block height
  def get_block_height(self):
    return len(self.blocks)

  #Add new block to chain
  def add_to_chain(self, block):
    self.blocks.append(block)

  #Forge new block and archive the data
  def forge_new_block(self, address, balance):
    height = self.get_block_height()
    block_data = self.blocks[height - 1] if height > 0 else Block()

    archival_block_data = Block()
    for key in block_data.state:
      archival_block_data.state[key] = block_data.state[key]

    archival_block_data.update_state(address, balance)

    self.add_to_chain(archival_block_data)

  #Get block at height
  def get_block_data(self, height):
    return self.blocks[height - 1]

  #Get balance at given block height
  def get_historic_balance(self, address, height):
    block_data = self.get_block_data(height)
    if address in block_data.state:
      return block_data.state[address]
    else:
      return "Address not registered"

  #Get current balance
  def get_balance(self, address):
    latest_block = len(self.blocks) - 1
    if latest_block == 0:
      return 0

    block_data = self.get_block_data(latest_block)
    return block_data.state[address]


#Genesis
Mainnet = Blockchain()

if __name__ == "__main__":
  print("Genesis | Block Height: ", Mainnet.get_block_height())

  #Make txns
  Mainnet.forge_new_block("A", 1)
  Mainnet.forge_new_block("B", 2)
  Mainnet.forge_new_block("A", 3)

  #Read txns
  print(Mainnet.get_historic_balance("A", 1))
  print(Mainnet.get_historic_balance("B", 1))
  print(Mainnet.get_historic_balance("A", 2))
  print(Mainnet.get_historic_balance("B", 2))
  print(Mainnet.get_historic_balance("A", 3))
  print(Mainnet.get_historic_balance("B", 3))
