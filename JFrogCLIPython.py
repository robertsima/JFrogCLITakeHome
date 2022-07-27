from secrets import choice
import requests, json
helpString = ("List of commands: \n" +  
            "- 'exit' ==> ends the session \n" +
            "- 'help' or '0' ==> prints a help string \n" +
            "- 'system ping' or '1' ==> get system ping from artifcatory \n" +
            "- 'system version' or '2' ==> get system version from artifactory \n" +
            "- 'create user' or '3' ==> create a user from artifactory given user inputs \n" +
            "- 'delete user' or '4' ==> deletes user from artifactory given user inputs \n" +
            "- 'get storage info' or '5' ==> # get system storage from artifactory \n" +
            "- 'create repository' or '6' ==> create a repository in the artifactory \n" +
            "- 'update repository' or '7' ==> updates a repository given user inputs \n" +
            "- 'list repositories' or '8' ==> get a list of local repositories in the artifactory \n")

headers = { #access header with bearer token.. JSON content type header
    'Authorization' : 'Bearer eyJ2ZXIiOiIyIiwidHlwIjoiSldUIiwiYWxnIjoiUlMyNTYiLCJraWQiOiJ5Z1l0M3lkTTE3VlhZMXpTTWFwZlJ4ek14Tml0ZndlUE5RZzVQbzNZY200In0.eyJleHQiOiJ7XCJyZXZvY2FibGVcIjpcInRydWVcIn0iLCJzdWIiOiJqZmFjQDAxZzhtd3M2OXgxN3ljMDhkZGthcWIxZWh6XC91c2Vyc1wvYWRtaW4iLCJzY3AiOiJhcHBsaWVkLXBlcm1pc3Npb25zXC9hZG1pbiIsImF1ZCI6IipAKiIsImlzcyI6ImpmZmVAMDAwIiwiZXhwIjoxNjkwMjUyMTgyLCJpYXQiOjE2NTg3MTYxODIsImp0aSI6ImJiNDA2M2FkLWNmYjYtNGRlMy04YThlLTQwYTRmOTU4MDVmNSJ9.TfJIs-XM50drAWEMd100ht7NguUMG8zo8U9DBwyNwBPOOtIyBQE570jXBIFcz_WXAS-SNOf-tBa9YrB07LQDLxuF2z2N_YzGJvMfdEfxoMK48m7-TdFFKuLgsdN4wykHpTzW49lfOyCPUTKzqOGF4C7C6xswmTi6R461gMyVL99JkFRag5_c_KsHUQVAXzW1MEpFqUk7LJIup5oIP9UZYG5pbquhesqshelBny2fDAT1lpXddA4657oZwYWAPyc1ykq-nKE-1RWqK2PnuwI8eAvGO0rNzSpMF0b3cn--D7bs4hNfHV7alexgZ4Jsri0MIkTmvx4SPwUzSXZ1M-WbOw',
    'Content-Type' : 'application/json'
    }
artifactoryUrl = "https://prodhomeassignment.jfrog.io/artifactory/"
accessUrl = "https://prodhomeassignment.jfrog.io/access/"
username = "admin"
password = "password"

## -------------------------------------------------------------------GET Methods-----------------------------------------------------------------------

def system_ping(): 
    # get system ping from artifcatory
    response = requests.request("GET", artifactoryUrl + 'api/system/ping', headers=headers)
    print("System ping response: ")

    print(response.json) # print api response

def list_repositories():
    # get a list of local repositories in the artifactory
    response = requests.request("GET", artifactoryUrl + 'api/repositories/?type=local', headers=headers)
    print("List of generic repositories: ")

    print(response.text) # print api response
       

def system_version():
    response = requests.request("GET", artifactoryUrl + 'api/system/version', headers=headers)
    print("System version response: ")
    # get system version from artifactory
    print(response.text)


def get_storage_info():
    # get system storage from artifactory
    response = requests.request("GET", artifactoryUrl + 'api/storageinfo', headers=headers)
    print("System storage information: ")
    print(response.text)
## -------------------------------------------------------------------PUT Methods-----------------------------------------------------------------------

def create_user():
# create a user from artifactory

    email = input("Enter an email for a new user... \n")
    jUser = input("Enter a username for a new user... \n")
    jPassword = input("Enter a password for  a new user... NOTE: Pasword must have one uppercase letter, one special character, and one letter. \n")

    print("You entered ... \n")
    print(email)
    print(jUser)
    print(jPassword)

    data = { 
        "name": jUser,
        "email":email,
        "password":jPassword,
        }

    #converts to json obj from python obj below
    json_data = json.dumps(data)
    print(json_data)

    request = requests.request("PUT", artifactoryUrl + 'api/security/users/' + jUser, headers=headers, json = data)

    print(request.status_code)
    print(request.text)
    print(request.json)

def create_repository():
# create a repository in the artifactory

    newRepoName = input("Enter a new repository name you would like to use... \n")
    print("You entered "+ newRepoName)


    #converts to json obj from python obj below
    data = {
        "rclass" : "local",
        }
    json_data = json.dumps(data)
    print(json_data)
    request = requests.request("PUT", artifactoryUrl + 'api/repositories/' + newRepoName, headers=headers, json = data)


    print(request.status_code)
    print(request.text) #prints api response
    print(request.json)

## -------------------------------------------------------------------DELETE Methods-----------------------------------------------------------------------

def delete_user():
# deletes user from artifactory
    jUser = input("Enter the name of the user you would like to delete... \n")
    print("You entered "+ jUser)

    response = requests.request("DELETE", artifactoryUrl + 'api/security/users/' + jUser, headers=headers)
    print("List of generic repositories: ")

    print(response.text)
    print(response.json)
    print(response.status_code)

## -------------------------------------------------------------------POST Methods-----------------------------------------------------------------------

def update_repository():
    repoName = input("Enter the name of a repository you would like to update... \n")
    print("You entered "+ repoName)
    repoclass = input("Enter the 'rclass'. HINT:'local'... \n")
    description = input("Enter a description to update the repository with. \n")
    notes = input("Enter some notes to update the repository with. \n")
    #converts to json obj from python obj below
    data = {
        "rclass" : repoclass,
        "description": description,
        "notes": notes
        }

    json_data = json.dumps(data)
    print(json_data)
    request = requests.request("POST", artifactoryUrl + 'api/repositories/' + repoName, headers=headers, json = data)

    print(request.status_code)
    print(request.text)
    print(request.json)

#---------------------------------------------------------------------MAIN method ------------------------------------------------------------------------

def main(): #main method executes the program... this is where the program runs
    checkUsername = input("Enter username \n")
    checkPassword = input("Enter password \n")

    if(checkUsername.__eq__(username) & checkPassword.__eq__(password)):
        print("Logged in! You can now begin inputting API commands... Type 'help' for a list of commands. \n")
        choice = ""
        while(choice != "exit"):
            choice = input()
            if (choice.__eq__("help")) or choice == '0':
                print(helpString)
                print("Input another command or enter 'exit'")

            elif choice.__eq__("system ping") or choice == '1':
                system_ping()
                print("Input another command or enter 'exit'")
            elif choice.__eq__("system version") or choice == '2':
                system_version()
                print("Input another command or enter 'exit'")
            elif choice.__eq__("create user") or choice == '3':
                create_user()
                print("Input another command or enter 'exit'")
            elif choice.__eq__("delete user") or choice == '4':
                delete_user()
                print("Input another command or enter 'exit'")
            elif choice.__eq__("get storage info") or choice == '5':
                get_storage_info()
                print("Input another command or enter 'exit'")
            elif choice.__eq__("create repository") or choice == '6':
                create_repository()
                print("Input another command or enter 'exit'")
            elif choice.__eq__("update repository") or choice == '7':
                update_repository()
                print("Input another command or enter 'exit'")
            elif choice.__eq__("list repositories") or choice == '8':
                list_repositories()
                print("Input another command or enter 'exit'")
            else: 
                print("Invalid input. Type 'help' for a list of commands or type 'exit' to end the CLI.")


    else: 
         print("Username or password combination incorrect. Try again. \n")
         main()

    print("Exiting... Goodbye!")

if __name__ == "__main__":
    main()
