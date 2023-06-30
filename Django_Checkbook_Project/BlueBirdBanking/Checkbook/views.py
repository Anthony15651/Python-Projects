from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction

# Create your views here.

# This function will render the Home page
def home(request):
    # Retrieves the Transaction Form
    form = TransactionForm(data=request.POST or None)
    # Checks if the request method is POST
    if request.method == 'POST':
        # If the form is submitted, retrieve which account the user wants to view
        pk = request.POST['account']
        # Call balance function to render that account's Balance Sheet
        return balance(request, pk)
    # Saves content to the template as a dictionary
    content = {'form': form}
    return render(request, 'checkbook/index.html', content)

# This function will render the Create Account page
def create_account(request):
    # Retrieves the Account Form
    form = AccountForm(data=request.POST or None)
    # Checks if request method is POST
    if request.method == 'POST':
        # Checks to see if form is valid
        if form.is_valid():
            # If valid, save form and return to home page
            form.save()
            return redirect('index')
    # Saves content to the template as a dictionary
    content = {'form': form}
    return render(request, 'checkbook/CreateNewAccount.html', content)

# This function will render the Balance page
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)                 # Retrieve requested account using its pk
    transactions = Transaction.Transactions.filter(account=pk)  # Retrieve all of that account's transactions
    current_total = account.initial_deposit                     # Creates account total variable
    table_contents = {}                                         # Creates a dictionary for the information
    for t in transactions:                                      # Loop through transactions and determine dpst / wthdrwl
        if t.type == 'Deposit':                                 #
            current_total += t.amount                           # If deposit, add amount to balance
            table_contents.update({t: current_total})           # Add transaction and total to dictionary
        else:                                                   #
            current_total -= t.amount                           # If withdrawal, subtract amount from balance
            table_contents.update({t: current_total})           # Add transaction and total to dictionary
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)

# This function will render the Transaction page
def transaction(request):
    # Retrieve the Transaction Form
    form = TransactionForm(data=request.POST or None)
    # Checks if request method is POST
    if request.method == 'POST':
        # Checks to see if form is valid
        if form.is_valid():
            # Retrieve which account the transaction was for
            pk = request.POST['account']
            # If valid, save form and render balance of the accounts Balance Sheet
            form.save()
            return balance(request, pk)
    # Saves content to the template as a dictionary
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content)
