
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bots_commands import *



app = ApplicationBuilder().token("ххххххххххххххххххххххххххххххххххххххх").build()

app.add_handler(CommandHandler("hi", hi))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

print('server start')

app.run_polling()

