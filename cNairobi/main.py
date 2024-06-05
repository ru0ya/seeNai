from flask import Flask, request


app = Flask(__name__)

# Temporary storage for user data
user_data = {}

@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route("/ussd", methods=['POST'])
def ussd():
    # Read the variables sent via POST from our API
    session_id = request.values.get("sessionId", None)
    serviceCode = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "")

    print("phone number", phone_number)
    print("text", text)

    if text == '':
        # This is the first request. Note how we start the response with CON
        response = "CON Welcome to the Kenya Tourist Guide \n"
        response += "1. Tourist Destinations \n"
        response += "2. Kenya Matatu Stages \n"
        response += "3. Nairobi Unique Foods \n"
    elif text == '1':
        # Business logic for Tourist Destinations
        response = "CON Tourist Destinations \n"
        response += "1. Maasai Mara \n"
        response += "2. Mount Kenya \n"
        response += "3. Diani Beach \n"
    elif text == '1*1':
        response = "END Maasai Mara is a large game reserve in Narok, Kenya, famous for its annual migration of wildebeest."
    elif text == '1*2':
        response = "END Mount Kenya is the highest mountain in Kenya and the second-highest in Africa, renowned for its scenic beauty."
    elif text == '1*3':
        response = "END Diani Beach is a major beach resort on the Indian Ocean coast of Kenya, known for its coral reefs and pristine white sands."
    elif text == '2':
        # Business logic for Kenya Matatu Stages
        response = "CON Kenya Matatu Stages \n"
        response += "1. Kencom \n"
        response += "2. GPO \n"
        response += "3. Ambassadeur \n"
    elif text == '2*1':
        response = "END Kencom stage is a major bus terminus in Nairobi, serving various routes across the city."
    elif text == '2*2':
        response = "END GPO stage is located near the General Post Office in Nairobi, serving multiple matatu routes."
    elif text == '2*3':
        response = "END Ambassadeur stage is a popular matatu terminus in Nairobi, known for its central location and accessibility."
    elif text == '3':
        # Business logic for Nairobi Unique Foods
        response = "CON Nairobi Unique Foods \n"
        response += "1. Nyama Choma \n"
        response += "2. Ugali \n"
        response += "3. Mutura \n"
    elif text == '3*1':
        response = "END Nyama Choma is a popular Kenyan dish of roasted meat, often enjoyed with friends and family."
    elif text == '3*2':
        response = "END Ugali is a staple food in Kenya, made from maize flour and water, usually served with vegetables or meat."
    elif text == '3*3':
        response = "END Mutura is a Kenyan sausage made from meat, blood, and spices, commonly enjoyed as a street food."
    else:
        # Default fallback response
        response = "END Invalid input, please try again"

    # Print the response to the console for debugging
    print(response)

    # Return the response to the API
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
