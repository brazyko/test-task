import datetime
from main import db_session, Users, Expenses, Category
global user


def main():
    table = int(input("\nList:\n"
                      "1) Login\n"
                      "2) Register\n"))
    if table not in range(1, 3):
        print("\nEnter number!!!")
        main()
    else:
        if table == 1:
            username = input('Enter username: ')
            if username:
                user = db_session.query(Users).filter_by(user_name=username).first()
                password = input('Enter password: ')
                if db_session.query(Users).filter_by(user_name=username, password=password).first():
                    print('You are logged in!')
                else:
                    print('wrong username or password')
                    main()
            else:
                print('empty input')
                main()
        if table == 2:
            username = input('Enter username: ')
            if db_session.query(Users).filter_by(user_name=username).first():
                print('Username is taken')
                main()
            else:
                password = input('Enter password: ')
                password2 = input('Confirm password:')
                if password2 == password:
                    user = Users(user_name=username, password=password)
                    db_session.add(user)
                    db_session.commit()
                    main()
                else:
                    print('Password error. Try again!')

    choice(user)


def choice(user):
    user_choice = int(input("\nList:\n"
                      "1) Add new category\n"
                      "2) Add new expenses\n"
                      "3) Show expenses by categories\n"
                      "4) Show expenses by time\n"
                      "5) Delete data\n"
                      "6) Exit\n"))
    if user_choice not in range(1, 6):
        print("\nEnter number!!!")
    else:
        if user_choice == 1:
            printer(add_category(user))
        elif user_choice == 2:
            add_expense(user)
        elif user_choice == 3:
            printer(show_categories_expenses(user))
        elif user_choice == 4:
            show_expenses_by_time(user)
        elif user_choice == 5:
            printer(clear_data())
        choice(user)
    if user_choice == 6:
        printer(quit_program())


def add_category(user):
    category_name = input("Enter category name: ")
    if db_session.query(Category).filter_by(category_name=category_name.lower()).first():
        print("\nCategory already exists!!!")
    else:
        category = Category(category_name=category_name.lower(), user_id=user.user_id)
        db_session.add(category)
        db_session.commit()
        print('Added category')


def add_expense(user):
    expense_sum = int(input("Enter sum of expense (integer): "))
    for category in db_session.query(Category).filter_by(user_id=user.user_id).all():
        print("%i) : %s" % (category.category_id, category.category_name))
    category_number = int(input("\nEnter category number: "))
    now = datetime.datetime.now()
    if db_session.query(Category).filter_by(category_id=category_number).first():
        new_expense = Expenses(expense_sum=expense_sum, user=user.user_id, category=category_number, date=now.strftime("%d/%m/%Y %H:%M:%S"))
        db_session.add(new_expense)
        db_session.commit()
        print('Added expense')
    else:
        print('First create category!')
        add_category(user)


def show_categories_expenses(user):
    for category in db_session.query(Category).filter_by(user_id=user.user_id).all():
        expenses_sum = 0
        for expense in category.expenses:
            expenses_sum += expense.expense_sum
        print("%i) : %s -  %s " % (category.category_id, category.category_name, expenses_sum))


def show_expenses_by_time(user):
    expenses = [expense for expense in db_session.query(Expenses).filter_by(user=user.user_id).all()]
    print('Choose statistic of expenses by:')
    ch_t = int(input("1) Day\n"
                     "2) Month\n"
                     "3) Year\n"))

    period_choise = {
        1: datetime.timedelta(days=1),
        2: datetime.timedelta(days=30),
        3: datetime.timedelta(days=365),
    }
    for expense in expenses:
        if datetime.datetime.strptime(expense.date, "%d/%m/%Y %H:%M:%S") >= datetime.datetime.now() - period_choise.get(ch_t):
            category = db_session.query(Category).filter_by(category_id=expense.category).first()
            print(" %s - %i - %s" % (category, expense.expense_sum, expense.date))


def clear_data():
    db_session.query(Expenses).delete()
    db_session.query(Category).delete()
    db_session.query(Users).delete()
    db_session.commit()
    return 'All data have been deleted'


def quit_program():
    return "See you later!"


def printer(func_to_print):
    print(func_to_print)


if __name__ == '__main__':
    main()
