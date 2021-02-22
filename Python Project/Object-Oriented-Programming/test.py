class distance:
    def __init__(self, x=None,y=None):
        self.ft=x
        self.inch=y
    def __add__(self):
        # temp=distance()
        # temp.ft=self.ft
        # temp.inch=self.inch
        if self.inch>=12:
            self.ft+=1
            self.inch-=12
            #return self
    def __str__(self):
        return 'ft:'+str(self.ft)+' in: '+str(self.inch)

d1=distance(3,10)
print(d1)
