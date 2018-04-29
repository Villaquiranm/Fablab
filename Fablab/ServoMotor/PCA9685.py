# -*- coding: UTF-8 -*-
import smbus
import time

pca9685_adr=0x40
pca9685_mode1adr=0x00
pca9685_mode2adr=0x01
pca9685_subadr1=0x02
pca9685_subadr2=0x03
pca9685_subadr3=0x04
pca9685_allcalladr=0x05
pca9685_led0_on_l=0x06
pca9685_led0_on_h=0x07
pca9685_led0_off_l=0x08
pca9685_led0_off_h=0x09
pca9685_all_led_on_l=0xfa
pca9685_all_led_on_h=0xfb
pca9685_all_led_off_l=0xfc
pca9685_all_led_off_h=0xfd
pca9685_pre_scale=0xfe
pca9685_testmode=0xff
pca9685_mode=0x00

class PCA9685(object):
    def __init__(self, address=pca9685_adr):
        self._address =address
        self._bus = smbus.SMBus(1)
    def init(self):
        self._bus.write_byte_data(self._address,pca9685_mode1adr,0x0)
    def all_init(self):
        self.write_16(pca9685_all_led_on_l,0)
        self.write_16(pca9685_all_led_off_l,300)
    def hex1(self,x1):
        if x1<0xff:
            x_l=x1
            x_h=0x00
        else :
            x_h=x1/256
            x_l=x1-x_h*256
        return x_l,x_h
    def write_16(self,led,u_16):
        (u_16_l,u_16_h)=self.hex1(u_16)
        self._bus.write_byte_data(self._address,led,u_16_l)
        self._bus.write_byte_data(self._address,led+1,u_16_h)
    def set_all_pwm(self,ledon,ledoff):
        self.write_16(pca9685_all_led_on_l,ledon)
        self.write_16(pca9685_all_led_off_l,ledoff)
    def set_pwm(self,n,ledon,ledoff):
        print (ledon,ledoff)
        self.write_16(pca9685_led0_on_l+4*n,ledon)
        self.write_16(pca9685_led0_on_l+4*n,ledoff)
    def set_pwm_frequency(self,hz):
        hz=float(hz)
        data=(25000000/(4096*hz))-1
        data=int(data)
        oldmode1=self._bus.read_byte_data(self._address,pca9685_mode1adr)
        newmode1 = (oldmode1&0x7F) | 0x10
        self._bus.write_byte_data(self._address,pca9685_mode1adr,newmode1)
        self._bus.write_byte_data(self._address,pca9685_pre_scale,data)
        self._bus.write_byte_data(self._address,pca9685_mode1adr,oldmode1)
        time.sleep(0.005)
        self._bus.write_byte_data(self._address,pca9685_mode1adr,oldmode1|0xa1)
        self.init()
    def get_pwm_frequency(self):
        data=self._bus.read_byte_data(self._address,pca9685_pre_scale)
        hz=25000000/(4096*(data+1))
        return hz
    def set_all_angle(self,angle):
        if angle>180:angle=180
        if angle<0:angle=0
        self.set_pwm_frequency(50)
        time1=float(angle+45)/90
        ledoff=int((time1/20)*4096)
        self.write_16(pca9685_all_led_on_l,0)
        self.write_16(pca9685_all_led_off_l,ledoff)
    def set_angle(self,n,angle):
        if angle>180:angle=180
        if angle<0:angle=0
        time1=float(angle+45)/90
        ledoff=int((time1/20)*4096)
        self.write_16(pca9685_led0_on_l+4*n,0)
        self.write_16(pca9685_led0_off_l+4*n,ledoff)
