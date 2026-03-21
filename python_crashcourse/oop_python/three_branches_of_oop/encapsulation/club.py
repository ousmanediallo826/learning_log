class Club():
    def __init__(self, clubName, maxMembers):
        self.clubName = clubName
        self.maxMembers = maxMembers
        self.membersList = []

    def addMember(self, name):
        if len(self.membersList) < self.maxMembers:
            self.membersList.append(name)
            print('OK. ' + name + 'has been added to the ' + self.clubName + ' club.')
        else:
            print('Sorry, but we cannot add ' + name + ' to the ' + self.clubName + ' club.')
            print(f'This club already has  {self.maxMembers} members.')
    def report(self):
        print()
        print(f'Here are the {len(self.membersList)} members of {self.clubName} club.')
        for name in self.membersList:
            print('   ' + name)
            print()