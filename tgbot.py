from pathlib import Path
from dotenv import dotenv_values
import re
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from web3 import Web3
from eth_account import Account
from web3.middleware import geth_poa_middleware
import pprint

def is_valid_evm_address(address):
    pattern = re.compile(r'^0x[0-9a-fA-F]{40}$')
    return bool(pattern.match(address))


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('faucet bot start！')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('use "/faucet address" to get bevm-canary-test BTC faucet。')
    

def faucet_command(update: Update, context: CallbackContext)-> None:
    print(update.message.chat_id)
    address = update.message.text[8:]
    if is_valid_evm_address(address) == True:
        transfer(address)
        update.message.reply_text("success")
    else:
        update.message.reply_text('please reset your input like "/faucet 0x477994165A4989E77dC775155c917a4A77017419"')

def faucet_command_group(update: Update, context: CallbackContext)-> None:
    print(update.message.chat_id)
    address = update.message.text[8:]
    if is_valid_evm_address(address) == True:
        transfer(address)
        update.message.reply_text("success")
    else:
        update.message.reply_text('please reset your input like "/faucet 0x477994165A4989E77dC775155c917a4A77017419"')
def transfer(to_address):
    mnemonic = ""
    env_file = Path(__file__).parent.joinpath(".env")
    if mnemonic == "" and env_file.exists():
        env = dotenv_values()
        if "MNEMONIC" in env:
            mnemonic = env["MNEMONIC"]
    assert mnemonic != "", "Please set MNEMONIC"
    Account.enable_unaudited_hdwallet_features()
    w3 = Web3(Web3.HTTPProvider('https://canary-testnet.bevm.io/'))

    account = Account.from_mnemonic(mnemonic)
    from_address = account.address
    amount_wei = w3.toWei("0.1","Ether")
    nonce = w3.eth.getTransactionCount(from_address)

    transaction = {
        'from': from_address,
        'to': to_address,
        'value': amount_wei,
        'gas': 21000,  # gas限制
        'gasPrice': w3.toWei("1","gwei"),  # gas价格，可以根据网络情况调整
        'nonce': nonce,
    }

    signed_transaction = w3.eth.account.sign_transaction(transaction, account.privateKey)
    transaction_hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)
    # print(transaction_hash)

def main() -> None:
    updater = Updater("6447070061:AAGpX1rOxUvUjomWkV4CEL7Qrz33WTt3ZHY")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & Filters.command, faucet_command))
    dp.add_handler(MessageHandler(Filters.text & Filters.group, faucet_command_group))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

