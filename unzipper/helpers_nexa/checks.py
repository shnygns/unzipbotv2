# ===================================================================== #
#                      Copyright (c) 2022 Itz-fork                      #
#                                                                       #
# This program is distributed in the hope that it will be useful,       #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                  #
# See the GNU General Public License for more details.                  #
#                                                                       #
# You should have received a copy of the GNU General Public License     #
# along with this program. If not, see <http://www.gnu.org/licenses/>   #
# ===================================================================== #


import logging
import asyncio
from pyrogram import enums
from unzipper import unzip_client
from config import Config


def get_bot_chat_id():
    try:
        bot_info = unzip_client.get_me()
        bot_user_id = bot_info.id
        message = unzip_client.send_message(chat_id=bot_user_id, text="Testing chat ID")
        bot_chat_id = message.chat.id
        logging.info(f"Bot's own chat ID: {bot_chat_id}")
        return bot_chat_id
    except Exception as e:
        logging.error(f"Error getting bot's own chat ID: {e}")
        return bot_user_id

def check_log_channel():
    try:
        if Config.LOGS_CHANNEL:
            bot_user_id = get_bot_chat_id()
            # c_info = unzip_client.get_chat(chat_id=Config.LOGS_CHANNEL)
            c_info = unzip_client.get_chat(chat_id=int(-1002429834992))
            if c_info.type != enums.ChatType.CHANNEL:
                logging.warn("Chat is not a channel!")
                exit()
            elif c_info.username is not None:
                logging.warn("Channel is not private!")
                exit()
            else:
                unzip_client.send_message(
                    chat_id=Config.LOGS_CHANNEL, text="`Unzipper-Bot has Successfully Started!` \n\n**Powered by @NexaBotsUpdates**")
        else:
            logging.warn("No Log Channel ID is Given! Imma leaving Now!")
            exit()
    except Exception as e:
        logging.warn("Error Happend while checking Log Channel! Make sure you're not dumb enough to provide a wrong Log Channel ID!")
        logging.warn(f"Error: \n{e}")