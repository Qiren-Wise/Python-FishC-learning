class Ticket():
    def __init__(self,weekend=0,child=0):
        self.price = 100
        if weekend:
            self.inc = 1.2
        else:
            self.inc = 1
        if child:
            self.discount = 0.5
        else:
            self.discount = 1

    def sum(self,num):
        return self.price * self.inc * self.discount * num

adult = Ticket()
child = Ticket(child=1)
adultCount = int(input("成人的个数为："))
childCount = int(input("儿童的个数为："))
print('价格为：%.2f' % (adult.sum(adultCount)+child.sum(childCount)))

    