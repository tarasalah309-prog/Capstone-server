import requests

count = 1
while True:
    purpose = input("What's your purpose from the email? ")
    recipient = input("Who is the Recipient of the email? ")
    length = input("How do you want the the email length?(ex: short-medium-detailed) ")
    while True:
        tone = input("Choose a number to indicate your tone(1/friendly - 2/formal - 3/urgent - 4/other): ")
        if tone == "1":
            tone = "friendly"
            break
        elif tone == "2":
            tone = "formal"
            break
        elif tone == "3":
            tone = "urgent"
            break
        elif tone == "4":
            tone = input("How do you want the tone exactly? ")
            break
        else:
            print("invalid option.")


    request1 = "Write a clear email using the following details."
    request2 = f"Purpose: {purpose}"
    request3 = f"Recipient: {recipient}"
    request4 = f"Length: {length}"
    request5 = f"Tone: {tone}"
    request6 = "Return only the email with no extra explanation"
                        
    invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"
    stream = False

    headers = {
        "Authorization": "Bearer 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",
        "Accept": "text/event-stream" if stream else "application/json",
    }

    payload = {
    "messages": [
        {
        "role": "user",
        "content": f"{request1}\n{request2}\n{request3}\n{request4}\n{request5}\n{request6}"
        }
    ],
    "model": "mistralai/mistral-large-3-675b-instruct-2512",
    "frequency_penalty": 0,
    "max_tokens": 2048,
    "presence_penalty": 0,
    "stream": stream,
    "temperature": 0.15,
    "top_p": 1
    }

    response = requests.post(invoke_url, headers=headers, json=payload, stream=stream)
    if stream:
        for line in response.iter_lines():
            if line:
                print(line.decode("utf-8"))
    else:
        print(response.json())

    with open(f"email {count}.txt", "w") as file:
        file.write(response.json())

    count += 1
    repeat = input("Do you want to generate another email? (y/n)")
    if repeat != "y":
        break