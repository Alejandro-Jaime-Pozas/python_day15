
# PROGRAM START
#==========================================================================================================================
# APPROACH: CREATE PROGRAM AS IF JUST KNOW ABOUT OOP AND NOTHING ABOUT SAVING SPACE/TIME 
# will need following fns: 
#     monthly income 
#     monthly expenses 
#     cash flow 
#     initial investment
#     cash on cash ROI 
#     fn to check valid input??\n - add this later optional 

# so i will create just one class which houses all 5 fns. 
# this class will have init ... nothing, everything is returned with its fn call, just assign variables w fn calls?


class ROICalculator:

    def __init__(self, client, ):
        self.client = client.title()
        self.exp_dict = {} # empty dict, add values as you ask for inputs
        self.inc_dict = {} # empty dict, add values as you ask for inputs
        self.init_investments_dict = {} # empty dict for investments

    def income(self, ):
        while True:
            try:
                self.inc_dict["income"] = int(input("\nWhat is the monthly rental income on your property: "))
                break
            except:
                print('Sorry, only numbers allowed. ')

    # i can assign inputs \nto each variable, then add variable to a dict...but that wastes space, better add value to dict directly.
    def expenses(self, ):
        while True:
            try:
                self.exp_dict["taxes"] = int(input("\nWhat are your monthly tax expenses: "))
                self.exp_dict["insurance"] = int(input("\nWhat is your monthly insurance expense: "))
                self.exp_dict["hoa"] = int(input("\nWhat is your monthly HOA expense if you pay it: "))
                self.exp_dict["lawn_snow"] = int(input("\nWhat is your monthly lawn/snow expense if any: "))
                self.exp_dict["vacancy"] = int(input("\nWhat is your monthly vacancy expense: "))
                self.exp_dict["repairs"] = int(input("\nWhat is your monthly repair expense: "))
                self.exp_dict["capex"] = int(input("\nWhat is your monthly calculated capex expense: "))
                self.exp_dict["prop_mgmt"] = int(input("\nWhat is your monthly property management expense: "))
                self.exp_dict["mortgage"] = int(input("\nWhat is your monthly mortgage expense: "))
                break
            except:
                print('Sorry, only numbers allowed. ')

    def _cash_flow(self, ):
        return (sum(self.inc_dict.values()) - sum(self.exp_dict.values())) * 12

    def init_investment(self, ):
        while True:
            try:
                self.init_investments_dict["down_pmt"] = int(input("\nWhat is your down payment for the property: "))
                self.init_investments_dict["closing_costs"] = int(input("\nWhat are your closing costs for the property: "))
                self.init_investments_dict["rehab_costs"] = int(input("\nWhat are your rehab costs for the property: "))
                break
            except:
                print('Sorry, only numbers allowed. ')

    def alternatives(self, ):
        if self.roi_pct * 100 < 0:
            return "\nWell it's probably a good idea to steer clear of this one..."
        elif self.roi_pct * 100 < 5:
            return "\nNot bad, but you're barely beating inflation here..."
        elif self.roi_pct * 100 < 10:
            return "\nThat's a good number, anything between 5-10% is solid."
        else:
            return "\nThis is a pretty good investment, I think I'll take it myself."
    
    def roi(self, ):
        net_income = self._cash_flow()
        self.roi_pct = net_income / sum(self.init_investments_dict.values())
        print(f"\n{client}, Your ROI per year is: {(self.roi_pct * 100):.2f}%.")
        print(self.alternatives())
        return self.roi_pct

    def output(self, ):

        print('\nHere is a breakdown of your ROI calculation:\n')
        print('\n' + '='*60 + '\n')
        print(f"\t{'+ TOTAL INCOME' : <25}" + f"{'=': ^10}" + f'${sum(self.inc_dict.values()) * 12 : >5}')
        print(f"\t{'- TOTAL EXPENSES' : <25}" + f"{'=': ^10}" + f'${sum(self.exp_dict.values()) * 12 : >5}')
        print(f"\t{'= TOTAL CASH FLOW' : <25}" + f"{'=': ^10}" + f'${self._cash_flow() : >5}')
        print('-'*60)
        print(f"\t{'INITIAL INVESTMENT' : <25}" + f"{'=': ^10}" + f'${sum(self.init_investments_dict.values()) : >5}')
        print('-'*60)
        print(f"\tAnnual Cash Flow / Initial Investment = {(self.roi_pct * 100):.2f}%\n")
        print('='*60 + '\n')





# MAIN PROGRAM

client = 'Brian'

calc = ROICalculator(client)

print(f"Hey {calc.client}, let's get started with your ROI calculator so you can decide if you're getting a good deal.\n")

calc.income()

calc.expenses()

calc.init_investment()

calc.roi()

calc.output()

print('\n\nThanks for your business!')







# Here we assume that we have a client coming to us asking for an automated Rental Property Calculator. 
# Our client's name is Brandon from a company called "Bigger Pockets". Below, you will find a video of 
# what Brandon usually does to calculate his Rental Property ROI.

# Using Visual Studio Code/Jupyter Notebook, and Object Oriented Programming create a program that will 
# calculate the Return on Investment(ROI) for a rental property. (use learned algorithm concepts to save time O(1)/O(log n)/O(n)

# This project will be completed individually, though you can feel free to share ideas with your fellow students.

# Once completed, commit the project to github and submit the link to this assignment.

# ======================================================================================================

# WE'LL SAY THAT YOU ARE IN THE POSITION OF A PROPERTY OWNER WHO IS RENTING AN APT COMPLEX OR A HOUSE

# what I need to calculate ROI:

#     Init Property Price ex $200,000         - need input? \nnot really if they give me the down payment not needed

# ====================================================================================================================================
    
#     MONTHLY INCOME 
#     Rental Income       ex $2,000           - need input 
#     Laundry             ex $0               - need input (\njust leave blank for now, if time, let user input t\nhis)
#     Storage             ex $0               - need input (\njust leave blank for now, if time, let user input t\nhis)
#     Misc                ex $0               - need input (\njust leave blank for now, if time, let user input t\nhis)
#     TOTAL INCOME        ex $2,000           CALCULATE 
# ====================================================================================================================================

#     EXPENSES
#     Tax                 ex $150             - need input?
#     Insurance           ex $100             - need input 
#     Utilities           ex $0               - need input (\njust leave blank for now, if time, let user input t\nhis)
#         Electric 
#         Water 
#         Sewer 
#         Garbage 
#         Gas 
#     HOA                 ex $0               - need input 
#     Lawn/Snow           ex $0               - need input 
#     Vacancy             ex $100             - need input 
#     Repairs             ex $100             - need input 
#     CapEx               ex $100             - need input 
#     Property Mgmt       ex $200             - need input 
#     Mortgage            ex $860             - need input (\ncan calculate also using current rates)
#     TOTAL EXPENSES      ex $1,610           CALCULATE 
# ====================================================================================================================================

#     CASH FLOW 
#     + Income            ex $2000            CALCULATE 
#     - Expenses          ex $1610            CALCULATE
#     TOTAL CASH FLOW     ex $390             CALCULATE
# ====================================================================================================================================

#     INITIAL INVESTMENT 
#     Down payment        ex $40,000          - need input 
#     Closing costs       ex $3,000           - need input 
#     Rehab budget        ex $7,000           - need input 
#     Misc other          ex $0               - need input l\neave blank for now 
#     TOTAL INVESTMENT    ex $50,000          CALCULATE 
# ====================================================================================================================================

#     Annual cash flow / total investment 
#     = 4,680 / 50,000 = 9.36%                CALCULATE dont need the purchase price for this, unless mortgage/down payment is calculated (not user input)

#         cash on cash ROI = 9.36% / yr