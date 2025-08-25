# import re

# ''' This class is used to take input from the user and scan resumes for keywords. '''
class taking_input:
    # ''' This method initializes the class and takes keywords input from the user. '''
    def __init__(self):
        enter = input("\nEnter keywords to search for:\n").lower()
        self.keywords = enter.strip().split(',') # Split keywords by comma and convert to lowercase
        # return keywords

    # ''' This method takes resume details from the user and stores them in a list. '''
    def data(self):
        resumes = []
        for i in range(1,3):
            raw_data = input("\nEnter the resume details to scan:\n").lower().strip()
            resumes.append(raw_data) # Store resumes in a list (resumes)
        self.resumes = resumes # Store resumes in the instance variable
        return resumes
        
    # ''' This method checks each resume for the presence of keywords and prints the results. '''
    def checking_keywords(self):
        try:
            # ''' Check each resume for keywords and print the results. '''
            for i, resume in enumerate(self.resumes, 1):
                found = [kw for kw in self.keywords if kw in resume] # List comprehension to find keywords in the resume
                if found:
                    print(f"\nKeyword found in resume {i}: {', '.join(found)}")
                # else:
                #     print(f"\nNo keywords found in resume {i}.")
            # ''' If no keywords are found in any resume, print a message. '''
        except Exception as e:
            print(f"An error occurred: {e}")

# ''' Calling the class and its methods to execute the resume scanning process. '''
scan = taking_input()
scan.data()
scan.checking_keywords()