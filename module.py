from test import employee
class result(employee):
    def emmperdetails(self):
        self.dupdetailsper()
    def empprodetails(self):
        self.dupdetailspro()
    def empaccdetails(self):
        self.dupdetailsacc()

obj=result()
obj.emmperdetails()
obj.empprodetails()
obj.empaccdetails()
class employee:
    def __perdetails(self):
        ename=input("ENTER EMPLOYEE NAME:")
        eage=int(input("ENTER EMPLOYEE AGE:"))
        efathername=input("ENTER EMPLOYEE FATHERNAME:")
        elocation=input("ENTER EMPLOYEE LOCATION:")
        emobilenumber=int(input("ENTER MOBILE NUMBER:"))
        print("EMPLOYEE NAME:",ename)
        print("EMPLOYEE AGE:",eage)
        print("EMPLOYEE FATHERNAME:",efathername)
        print("EMPLOYEE LOACTION:",elocation)
        print("EMPLOYEE PHONENUMBER:",emobilenumber)
    def dupdetailsper(self):
        self.__perdetails()
    def __prodetails(self):
        ename = input("ENTER EMPLOYEE NAME:")
        education=input("ENTER EMPLOYEE EDUCATION:")
        subject=input("ENTER GRADUATION GROUP:")
        tcource=input("ENTER TECHNICAL COURCE:")
        tlanguages=input("ENTER TECHNICAL LANGUAGES:")
        print("EMPLOYEE NAME:", ename)
        print("EMPLOYEE EDUCATION:",education)
        print("EMPLOYEE GRADUATIN:",subject)
        print("EMPLOYEE TECHNICAL COURCE:",tcource)
        print("EMPLOYEE TECHINACAL LANGUAGES:",tlanguages)
    def dupdetailspro(self):
        self.__prodetails()
    def __accdetails(self):
        ename=input("ENTER EMPLOYEE NAME:")
        ebankname=input("ENTER BANK NAME:")
        eaccountnum=int(input("ENTER ACCOUNT NUMBER OF BANK:"))
        eifsecode=input("ENTER IFSE CODE OF BANK:")
        print("EMPLOYEE NAME:", ename)
        print("EMPLOYEE BANKNAME:",ebankname)
        print("EMPLOYEE ACCOUNTNUMBER:",eaccountnum)
        print("EMPLOYEE IFSECODE:",eifsecode)
    def dupdetailsacc(self):
        self.__accdetails()



