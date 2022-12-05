class Node:
    def __init__(self, dataval = None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
            
    def AtBeginning(self,newdata):
        NewNode = Node(newdata)

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval = NewNode

    def insert(self, val_before, newdata): # def insert function with self, val_before and newdata as parameters
        if val_before is None: # if there is nothing in val_before
            print('No Node to insert after')
            return
        else:
            NewData = Node(newdata) # Calls Node with the new data and assigns it to the variable NewData 
            NewData.nextval = val_before.nextval # set NewData to be the val_before next value 
            val_before.nextval = NewData # val_bere to be NewData 
                



        

list = SLinkedList()
list.headval = Node("Mon")

e2 = Node("Tue")
e3 = Node("Thur")
e4 = Node("Fri")
e5 = Node("Sat")
list.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5


list.AtEnd("Sun")
list.insert(list.headval.nextval,"Wed") # call the function insert with list head nex val and Wed because it should come after tue
list.listprint()
