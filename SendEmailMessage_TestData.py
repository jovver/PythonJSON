import json
import copy

# Initializes the number of emailData objects to create
numOfObjects = 500


# Opens the template file
with open("SendEmailRequest.json", "r") as file:
    data = json.load(file)
    file.close()


# Acquires the emailData object to copy
emailDataList = data["emailData"].copy()
copiedEmailData = copy.deepcopy(emailDataList[0])

# Iterates over the number initialized
for i in range(numOfObjects):
    copiedSendData = copy.deepcopy(copiedEmailData["sendData"])
    copiedSendData.update({"accountPendingEventId": "123-" + str(i+1)})
    copiedEmailData.update({"sendData": copiedSendData})
    emailDataList.append(copy.deepcopy(copiedEmailData))

# Updates the dictionary object with the new list
data.update({"emailData": emailDataList})


# Writes the result to a different json file
with open("SendEmailRequest_Final.json", "w") as file:
    json.dump(data, file)
    file.close()