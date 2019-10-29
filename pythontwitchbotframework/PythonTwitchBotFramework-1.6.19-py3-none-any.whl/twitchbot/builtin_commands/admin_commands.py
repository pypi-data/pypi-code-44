from twitchbot import Command, CommandContext, Message, get_bot

ADMIN_COMMAND_PERMISSION = 'admin'


@Command('shutdown', context=CommandContext.BOTH, permission=ADMIN_COMMAND_PERMISSION,
         help='make the bot shutdown')
async def cmd_shutdown(msg: Message, *args):
    await msg.reply('bot shutting down...')
    get_bot().shutdown()
