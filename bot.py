import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensagem = (
        "🤖 ALDO SINAIS EURUSD\n\n"
        "Ativo: EUR/USD\n"
        "Gráfico: M1\n"
        "Confirmação: M5\n\n"
        "Comandos disponíveis:\n"
        "/analise - Ver orientação do bot\n"
        "/regras - Ver critérios de análise\n\n"
        "⚠️ Ainda não estou conectado a cotações ao vivo. "
        "Não envio sinais reais nem garanto resultados."
    )
    await update.message.reply_text(mensagem)

async def analise(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🟡 AGUARDAR\n\n"
        "Ainda preciso conectar uma fonte de cotações "
        "para analisar EUR/USD em tempo real."
    )

async def regras(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 CRITÉRIOS PLANEJADOS\n\n"
        "🟢 CALL: tendência de alta confirmada em M1 e M5.\n"
        "🔴 PUT: tendência de baixa confirmada em M1 e M5.\n"
        "🟡 AGUARDAR: sinais conflitantes ou mercado lateral.\n\n"
        "Esses critérios ainda precisam ser testados. "
        "Não garantem acerto ou lucro."
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("analise", analise))
    app.add_handler(CommandHandler("regras", regras))
    app.run_polling()

if __name__ == "__main__":
    main()
