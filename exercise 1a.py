# Message 1
message1 = "https://database.com/user/augustom,AugUSto Martin, 23, Approved,,"
message1_required = message1.removeprefix("https://database.com/user/").removesuffix(",,")
username1, full_name1, age1, status1 = message1_required.split(',')
full_name1 = full_name1.strip().replace(" ", "").lower()
status1 = status1.strip().lower()
formatted_message1 = f"message: {username1},{full_name1},{age1},{status1}"

# Message 2
message2 = "https://database.com/user/juliasch,JuLIA SchmidT, 67, rejected,,"
message2_required = message2.removeprefix("https://database.com/user/").removesuffix(",,")
username2, full_name2, age2, status2 = message2_required.split(',')
full_name2 = full_name2.strip().replace(" ", "").lower()
status2 = status2.strip().lower()
formatted_message2 = f"message: {username2},{full_name2},{age2},{status2}"

# Message 3
message3 = "https://database.com/user/kmarx,Karl Marx, 42, rejected,,"
message3_required = message3.removeprefix("https://database.com/user/").removesuffix(",,")
username3, full_name3, age3, status3 = message3_required.split(',')
full_name3 = full_name3.strip().replace(" ", "").lower()
status3 = status3.strip().lower()
formatted_message3 = f"message: {username3},{full_name3},{age3},{status3}"

# Print all formatted messages
print(formatted_message1)
print(formatted_message2)
print(formatted_message3)