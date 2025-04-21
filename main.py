def processed_message(message):
    message = message.strip().removeprefix('https://database.com/user/')
    username,name,age,status,*_ = message.split(",")
    name = name.replace(" ","").lower()
    status = status.lower()
    age = age.strip()
    status = status.strip()
    print(f"message: {username},{name},{age},{status}")

message1= "https://database.com/user/augustom,AugUSto Martin, 23, Approved,,";
message2= "https://database.com/user/juliasch,JuLIA SchmidT, 67, rejected,,";
message3= "https://database.com/user/kmarx,Karl Marx, 42, rejected,,";

processed_message(message1)
processed_message(message2)
processed_message(message3)
