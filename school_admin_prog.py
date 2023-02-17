def add_student():
    a=open('demo.csv','a')
    name=input('enter name:')
    age=input('enter age:')
    contact_number=input('enter contact details:')
    email_id=input('enter email id:')
    a.write(name+' ')
    a.write(age+' ')
    a.write(contact_number+' ')
    a.write(email_id+' ')
    a.write('\n')
    print('students detailes added')

def view_students():
    a= open('demo.csv','r') 
    print('name','age','con_number','email_id')
    for k in a:
        b=k.strip().split(',')
        for i in range(len(b)):
            print(b[i])
        
def search_student():
    search_name = input("Enter student name to search: ")
    a=open('demo.csv','r')
    for i in a:
        n=i.strip().split(',')
        if n[0]==search_name:
           print(n[0],n[1],n[2],n[3])
while True:
    print('1. Add student')
    print('2. View students')
    print('3. Search student')
    print('4. Exit')

    choice = input('Enter your choice (1-4): ')
    print()

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        print('------------')
        break
    else:
        print('Invalid choice')