from unittest import TestCase
import datetime
import multiprocessing
from rpihome.rules import home_user3


class TestHomeUser3(TestCase):
    def setUp(self):
        self.testQueue = multiprocessing.Queue(-1)         
        self.user = home_user3.HomeUser3(self.testQueue)
        self.ip = "10.5.30.112"
        self.mac = "70:ec:e4:81:44:0f"

    def test_user3_mode_0(self):
        """ User mode==0 is force-away """
        self.user.by_mode(mode=0, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(4,0)))
        self.assertEqual(self.user.yes, False)
        self.user.by_mode(mode=0, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(6,0)))
        self.assertEqual(self.user.yes, False)    
        self.user.by_mode(mode=0, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(8,0)))
        self.assertEqual(self.user.yes, False)  
        self.user.by_mode(mode=0, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(10,0)))
        self.assertEqual(self.user.yes, False)
        self.user.by_mode(mode=0, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(12,0)))
        self.assertEqual(self.user.yes, False)    
        self.user.by_mode(mode=0, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(14,0)))
        self.assertEqual(self.user.yes, False)
        self.user.by_mode(mode=0, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(16,0)))
        self.assertEqual(self.user.yes, False)    
        self.user.by_mode(mode=0, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(18,0)))
        self.assertEqual(self.user.yes, False)  
        self.user.by_mode(mode=0, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(20,0)))
        self.assertEqual(self.user.yes, False)
        self.user.by_mode(mode=0, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(22,0)))
        self.assertEqual(self.user.yes, False)                  

    def test_user3_mode_1(self):
        """ User mode==1 is force-home """
        self.user.by_mode(mode=1, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(4,0)))
        self.assertEqual(self.user.yes, True)
        self.user.by_mode(mode=1, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(6,0)))
        self.assertEqual(self.user.yes, True)    
        self.user.by_mode(mode=1, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(8,0)))
        self.assertEqual(self.user.yes, True)  
        self.user.by_mode(mode=1, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(10,0)))
        self.assertEqual(self.user.yes, True)
        self.user.by_mode(mode=1, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(12,0)))
        self.assertEqual(self.user.yes, True)    
        self.user.by_mode(mode=1, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(14,0)))
        self.assertEqual(self.user.yes, True)
        self.user.by_mode(mode=1, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(16,0)))
        self.assertEqual(self.user.yes, True)    
        self.user.by_mode(mode=1, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(18,0)))
        self.assertEqual(self.user.yes, True)  
        self.user.by_mode(mode=1, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(20,0)))
        self.assertEqual(self.user.yes, True)
        self.user.by_mode(mode=1, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(22,0)))
        self.assertEqual(self.user.yes, True)  

    def test_user3_mode_2(self):
        """ User mode==2 is home/away based upon a typical schedule """
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(4,0)))
        self.assertEqual(self.user.yes, True)
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(6,0)))
        self.assertEqual(self.user.yes, True)    
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(8,0)))
        self.assertEqual(self.user.yes, False)  
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(10,0)))
        self.assertEqual(self.user.yes, False)
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(12,0)))
        self.assertEqual(self.user.yes, False)    
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(14,0)))
        self.assertEqual(self.user.yes, False)
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(16,0)))
        self.assertEqual(self.user.yes, False)    
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(18,0)))
        self.assertEqual(self.user.yes, False)  
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(20,0)))
        self.assertEqual(self.user.yes, False)
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(22,0)))
        self.assertEqual(self.user.yes, False) 
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,1), datetime.time(4,0)))
        self.assertEqual(self.user.yes, False)
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,1), datetime.time(6,0)))
        self.assertEqual(self.user.yes, False)    
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,1), datetime.time(8,0)))
        self.assertEqual(self.user.yes, False)  
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,1), datetime.time(10,0)))
        self.assertEqual(self.user.yes, False)
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,1), datetime.time(12,0)))
        self.assertEqual(self.user.yes, False)    
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,1), datetime.time(14,0)))
        self.assertEqual(self.user.yes, False)
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,1), datetime.time(16,0)))
        self.assertEqual(self.user.yes, False)    
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,1), datetime.time(18,0)))
        self.assertEqual(self.user.yes, False)  
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,1), datetime.time(20,0)))
        self.assertEqual(self.user.yes, False)
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,1), datetime.time(22,0)))
        self.assertEqual(self.user.yes, False)  
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,2), datetime.time(4,0)))
        self.assertEqual(self.user.yes, False)
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,2), datetime.time(6,0)))
        self.assertEqual(self.user.yes, False)    
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,2), datetime.time(8,0)))
        self.assertEqual(self.user.yes, False)  
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,2), datetime.time(10,0)))
        self.assertEqual(self.user.yes, False)
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,2), datetime.time(12,0)))
        self.assertEqual(self.user.yes, False)    
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,2), datetime.time(14,0)))
        self.assertEqual(self.user.yes, False)
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,2), datetime.time(16,0)))
        self.assertEqual(self.user.yes, False)    
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,2), datetime.time(18,0)))
        self.assertEqual(self.user.yes, True)  
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,2), datetime.time(20,0)))
        self.assertEqual(self.user.yes, True)
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,2), datetime.time(22,0)))
        self.assertEqual(self.user.yes, True) 
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,3), datetime.time(4,0)))
        self.assertEqual(self.user.yes, True)
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,3), datetime.time(6,0)))
        self.assertEqual(self.user.yes, True)    
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,3), datetime.time(8,0)))
        self.assertEqual(self.user.yes, False)  
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,3), datetime.time(10,0)))
        self.assertEqual(self.user.yes, False)
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,3), datetime.time(12,0)))
        self.assertEqual(self.user.yes, False)    
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,3), datetime.time(14,0)))
        self.assertEqual(self.user.yes, False)
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,3), datetime.time(16,0)))
        self.assertEqual(self.user.yes, False)    
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,3), datetime.time(18,0)))
        self.assertEqual(self.user.yes, True)  
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,3), datetime.time(20,0)))
        self.assertEqual(self.user.yes, True)
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,3), datetime.time(22,0)))
        self.assertEqual(self.user.yes, True) 
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,4), datetime.time(4,0)))
        self.assertEqual(self.user.yes, True)
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,4), datetime.time(6,0)))
        self.assertEqual(self.user.yes, True)    
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,4), datetime.time(8,0)))
        self.assertEqual(self.user.yes, False)  
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,4), datetime.time(10,0)))
        self.assertEqual(self.user.yes, False)
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,4), datetime.time(12,0)))
        self.assertEqual(self.user.yes, False)    
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,4), datetime.time(14,0)))
        self.assertEqual(self.user.yes, False)
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,4), datetime.time(16,0)))
        self.assertEqual(self.user.yes, False)    
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,4), datetime.time(18,0)))
        self.assertEqual(self.user.yes, False)  
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,4), datetime.time(20,0)))
        self.assertEqual(self.user.yes, False)
        self.user.by_mode(mode=2, ip=self.ip, datetime=datetime.datetime.combine(datetime.date(2016,11,4), datetime.time(22,0)))
        self.assertEqual(self.user.yes, False)                                 

    def test_user3_mode_3(self):
        """ User mode==3 is home/away via arp and ping """
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(4,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30)       
        self.user.by_mode(mode=3, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, True)
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(6,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30)         
        self.user.by_mode(mode=3, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, True)   
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(8,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30)          
        self.user.by_mode(mode=3, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, True)  
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(10,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30) 
        self.user.by_mode(mode=3, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, True)
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(12,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30) 
        self.user.by_mode(mode=3, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, True)  
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(14,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30) 
        self.user.by_mode(mode=3, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, True)
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(16,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30) 
        self.user.by_mode(mode=3, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, True)
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(18,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30) 
        self.user.by_mode(mode=3, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, True)  
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(20,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30) 
        self.user.by_mode(mode=3, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, True)
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(22,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30) 
        self.user.by_mode(mode=3, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, True) 

    def test_user3_mode_4(self):
        """ User mode==4 is by ping only, but with an away delay """
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(4,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30)       
        self.user.by_mode(mode=4, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, True)
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(6,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30)         
        self.user.by_mode(mode=4, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, True)   
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(8,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30)          
        self.user.by_mode(mode=4, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, True)  
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(10,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30) 
        self.user.by_mode(mode=4, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, True)
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(12,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30) 
        self.user.by_mode(mode=4, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, True)  
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(14,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30) 
        self.user.by_mode(mode=4, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, True)
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(16,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30) 
        self.user.by_mode(mode=4, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, True)
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(18,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30) 
        self.user.by_mode(mode=4, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, True)  
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(20,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30) 
        self.user.by_mode(mode=4, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, True)
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(22,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30) 
        self.user.by_mode(mode=4, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, True)


    def test_user3_mode_5(self):
        """ User mode==5 determines home/away based upon a typical schedule, but includes pings for newly-home detection """
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(4,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30)       
        self.user.by_mode(mode=5, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, True)
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(6,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30)         
        self.user.by_mode(mode=5, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, True)   
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(8,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30)          
        self.user.by_mode(mode=5, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, False)  
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(10,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30) 
        self.user.by_mode(mode=5, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, False)
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(12,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30) 
        self.user.by_mode(mode=5, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, False)  
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(14,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30) 
        self.user.by_mode(mode=5, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, False)
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(16,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30) 
        self.user.by_mode(mode=5, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, False)
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(18,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30) 
        self.user.by_mode(mode=5, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, False)  
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(20,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30) 
        self.user.by_mode(mode=5, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, False)
        self.datetime = datetime.datetime.combine(datetime.date(2016,10,31), datetime.time(22,0))        
        self.user.last_arp = self.datetime + datetime.timedelta(minutes=-30)
        self.user.last_ping = self.datetime + datetime.timedelta(minutes=-30) 
        self.user.by_mode(mode=5, ip=self.ip, mac=self.mac, datetime=self.datetime)
        self.assertEqual(self.user.yes, False)                 
