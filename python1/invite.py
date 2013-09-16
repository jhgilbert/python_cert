#!/usr/local/bin/python3
invites = {}
options = ['add', 'list', 'approve', 'delete', 'quit']
prompt = 'Pick an option from the list: {0} '.format(', '.join(options))
status_1 = 'unapproved'
status_2 = 'approved'
while True:
    inp = input(prompt)
    if inp not in options:
        print('Please pick a valid option')
        continue
    if inp == 'add':
        name = input('Enter name:')
        if not name:
            continue
        invites[name] = status_1
    elif inp == 'list':
        for name, status in invites.items():
            print("{0}, {1}".format(name, status))
    elif inp == 'approve':
        for name in invites:
            if invites[name] == status_1:
                break
        else:
            print('There must be {0} status invites. Please pick another option'.format(status_1))
            continue
        while True:
            print('Please enter a valid name from the list below: ')
            unapproved = []
            for name in invites:
                if invites[name] == status_1:
                    unapproved.append(name)
            print(", ".join(unapproved))
            name = input('Enter name: ')
            if not name:
                break # user changed mine about approving
            if name in unapproved:
                invites[name] = status_2
                print('{0} {1}'.format(name, status_2))
                break
    elif inp == 'delete':
        if not invites:
            print('There must be invites before you delete any of them')
            continue
        while True:
            print('Please enter a valid name from the list below')
            for name, status in invites.items():
                print("{0} ({1})".format(name, status))
            name = input('Enter name:')
            if not name:
                break # user changed mind about deleting
            if name in invites:
                del invites[name]
                print("{0} deleted".format(name))
                break
    elif inp == 'quit':
        print('Quitting invites')
        print('The final invitation list follows')
        for name, status in invites.items():
            print("{0} ({1})".format(name, status))
        break
