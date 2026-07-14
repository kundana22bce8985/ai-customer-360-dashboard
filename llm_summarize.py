import json
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API Key
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-3-flash-preview")



def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)


crm = load_json("crm.json")
support = load_json("support.json")
slack = load_json("slack.json")
emails = load_json("emails.json")
usage = load_json("usage.json")

def get_customer_data(customer_name):

    customer = {}

    for item in crm:
        if item["customer"] == customer_name:
            customer["crm"] = item

    for item in support:
        if item["customer"] == customer_name:
            customer["support"] = item

    for item in slack:
        if item["customer"] == customer_name:
            customer["slack"] = item

    for item in emails:
        if item["customer"] == customer_name:
            customer["emails"] = item

    for item in usage:
        if item["customer"] == customer_name:
            customer["usage"] = item

    return customer

def generate_summary(customer_name):

    data = get_customer_data(customer_name)

    prompt = f"""
    You are a Customer Success AI.

    Analyze the customer information below.

    {data}

    Return your answer in this format:

    Customer Summary

    Risks

    Opportunities

    Next Best Action
    """

    response = model.generate_content(prompt)

    return response.text
