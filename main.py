from blockchain import Blockchain


def main():
    blockchain = Blockchain()
    blockchain.new_transaction('nich', 'hicn', '1 BTC')
    blockchain.new_transaction('hicn', 'nich', '2 BTC')
    blockchain.new_transaction('nich', 'hicn', '1 BTC')
    blockchain.new_block(1)
    print(blockchain.chain)

if __name__ == '__main__':
    main()