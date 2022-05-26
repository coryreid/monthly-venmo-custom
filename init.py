import email
from venmo_api import Client
from dotenv import load_dotenv
from datetime import datetime

from utils import get_env, env_vars, get_month, Venmo, Gmail

def main(now):
  """
  The main function which initiates the script.
  """

  load_dotenv()  # take environment variables from .env.
  actualVars = []
  for var in env_vars:
    actualVars.append(get_env(var))

  access_token, gmail_app_password, email_sender, email_recipient, e_friend_id = actualVars

  month = get_month(now)
  venmo = Venmo(access_token)
  gmail = Gmail(email_sender)

  friends =[
    {
      "name": "Evie",
      "id": e_friend_id,
    }
  ]

  successfulRequests = []
  expectedRequests = len(friends)

  for friend in friends:
    name = friend["name"]
    id = friend["id"]
    description = "Test request for the month of " + month + "— Sent by Cory's Assistant Efron 🤵🏻‍♂️"
    amount = 3.00
    subject = f"Venmo request for {name}"
    message = f"""Good news old sport!

I have successfully requested money from {name}.

— Efron 🤵🏻‍♂️
    """
    success = venmo.request_money(id, amount, description, gmail.send_message(email_recipient, email_sender, gmail_app_password, subject, message))
    if success:
      successfulRequests.append(success)

  if len(successfulRequests) == expectedRequests:
    print("✅ Ran script successfully and sent " + str(expectedRequests) + " Venmo requests.")
  else:
    print("❌ Something went wrong. Only sent " + str(len(successfulRequests)) + "/" + str(expectedRequests) + " venmo requests.")

now = datetime.now()
main(now)
