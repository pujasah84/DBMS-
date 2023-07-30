from django.db import models


class Branch(models.Model):
    branch_id = models.BigAutoField(primary_key=True)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location


class Account(models.Model):
    acc = [("SINGLE","single"),
            ("JOINT",'joint')
    ]
    account_number=models.IntegerField(primary_key=True)
    type_of = models.CharField(choices=acc,default="SINGLE",max_length =10,null = True,blank=True)
    balance = models.FloatField(null = True,blank=True)


class Customer(models.Model):
    mobile_number = models.CharField(primary_key=True,max_length=10)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name 



class Employee(models.Model):
    name = models.CharField(max_length=50)
    degination = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Loan(models.Model):
    loan_id=models.BigAutoField(primary_key=True)
    loan_amount = models.FloatField()
    desc=models.CharField(max_length=50)  
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  

    def __str__(self):
        return str(self.loan_amount)

class Transaction(models.Model):
    tranType = [("DEBIT","debit"),
                ("CREDIT","credit")
    ]
    amount = models.FloatField()
    tran_type = models.CharField(choices=tranType,max_length=30)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    account=models.ForeignKey(Account,on_delete=models.CASCADE)
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)

    def __str__(self):
        return self.tran_type
    
        
    

