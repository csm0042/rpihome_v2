#!/usr/bin/python3
""" wemo_cclt1.py: 
""" 

# Import Required Libraries (Standard, Third Party, Local) ************************************************************
import datetime
import logging
import multiprocessing
from rpihome.devices.device_wemo import DeviceWemo


# Authorship Info *****************************************************************************************************
__author__ = "Christopher Maue"
__copyright__ = "Copyright 2016, The RPi-Home Project"
__credits__ = ["Christopher Maue"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Christopher Maue"
__email__ = "csmaue@gmail.com"
__status__ = "Development"


# Device class ********************************************************************************************************
class Wemo_cclt1(DeviceWemo):
    def __init__(self, name, msg_out_queue):
        super().__init__(name, msg_out_queue)


    def check_rules(self, **kwargs):
        """This method contains the rule-set that controls internal security lights """
        # Update value stored in dt_now to current datetime
        self.dt = datetime.datetime.now()
        # Process input variables if present  
        self.homeArray = []   
        self.home = False          
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "datetime":
                    self.dt = value
                if key == "homeArray":
                    self.homeArray = value 
                if key == "home":
                    self.home = value 
                if key == "utcOffset":
                    self.utcOffset = value
                if key == "sunriseOffset":
                    self.sunriseOffset = value
                if key == "sunsetOffset":
                    self.sunsetOffset = value   
                if key == "timeout":
                    self.timeout = value                    
        # Determine if anyone is home
        for h in self.homeArray:
            if h is True:
                self.home = True        
        # Calculate sunrise / sunset times
        self.sunrise = datetime.datetime.combine(datetime.datetime.today(), self.s.sunrise(self.dt, self.utcOffset))
        self.sunset = datetime.datetime.combine(datetime.datetime.today(), self.s.sunset(self.dt, self.utcOffset))                        
        # Decision tree to determine if screen should be awake or not
        if self.home is True:
            # If after 5am but before sunrise + the offset minutes
            if self.dt <= self.sunrise + self.sunriseOffset:
                self.state = True
            # If after sunset + the offset minutes but before 10pm  
            elif self.dt >= self.sunset + self.sunsetOffset:              
                self.state = True
            else:
                self.state = False
        else:
            self.state = False
        # Return result
        return self.state          