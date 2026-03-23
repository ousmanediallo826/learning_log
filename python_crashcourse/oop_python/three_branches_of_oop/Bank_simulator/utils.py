
import uuid
import datetime
generated_account = []
def get_generator_account_number():

    account = f"ACC-{uuid.uuid4().hex[:8].upper()}"
    if account not in generated_account:
        generated_account.append(account)
        print("Account generated")
        return account
    else:
        print("Duplicate account detected. regenerating...")
        return get_generator_account_number()


def timeStamp():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

number = get_generator_account_number()
print(number)
print(generated_account)
print(timeStamp())