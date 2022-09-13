from discord_webhook import DiscordWebhook, DiscordEmbed
import inspect
import os, sys


def log(mensaje, tipo: str) -> int:
    try:
        proxies = {
            "http": "192.168.0.252:8080",
            "https": "192.168.0.252:8080",
        }
        procname = inspect.stack()[1][3]
        # Webhook of my channel. Click on edit channel --> Webhooks --> Creates webhook
        mUrl = "https://discord.com/api/webhooks/852593467003371581/UO6pjrI1w3CZ7QC1EGdDS7xzdaZukJS9t6qO4Grckon9BsLq4ZuRPWfKkvJE3fZ06pxy"
        webhook = DiscordWebhook(
            # proxies=proxies,
            url=mUrl,
            content=f"""```{mensaje.to_markdown(index=False)}```""",
        )
        response = webhook.execute()
    except Exception as e:
        print(f"\nFallo el discord log: {str(e)}")
        pass
    return 0


# def log_discord(proceso, mensajes):
#     try:
#         if "ERROR" in proceso:
#             color = "FF0000"  # rojo
#         else:
#             color = "00FF00"  # verde

#         computer = os.environ["COMPUTERNAME"]
#         proxies = {
#             "http": "iwsva-25m:8080",
#             "https": "iwsva-25m:8080",
#         }
#         mUrl = "https://discord.com/api/webhooks/852593467003371581/UO6pjrI1w3CZ7QC1EGdDS7xzdaZukJS9t6qO4Grckon9BsLq4ZuRPWfKkvJE3fZ06pxy"
#         # if "vdm" in computer.lower():
#         #     webhook = DiscordWebhook(url=mUrl, proxies=proxies)
#         # else:
#         #     webhook = DiscordWebhook(url=mUrl)
#         webhook = DiscordWebhook(url=mUrl)
#         embed = DiscordEmbed(title=proceso, color=color)
#         for k, v in mensajes.items():
#             if "Errores" in k or "Caidos" in k or "Codigo" in k:
#                 embed.add_embed_field(name=k, value=v, inline=True)
#             else:
#                 embed.add_embed_field(name=k, value=v, inline=False)
#         webhook.add_embed(embed)
#         response = webhook.execute()
#     except Exception as e:
#         print(f"\nFallo el discord log: {str(e)}")
#         pass
#     return 0
