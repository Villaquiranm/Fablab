# -*- coding: UTF-8 -*-
from PCA9685 import PCA9685 # 导入PCA9685库
import time
pwm=PCA9685(0x40)
pwm.set_pwm_frequency(50) # 设置频率
pwm.init() # 初始化pca9685
pwm.all_init() # 初始化所有通道
#pwm.set_all_pwm(0,4000) # 设置所有通道。两个参数，前面一个是低电平转高电平的时间，后面一个是高电平转低电平的时间，这两个数值都应该小于4096
pwm.set_pwm(0,0,4000) # 第一个参数为通道。两个参数，前面一个是低电平转高电平的时间，后面一个是高电平转低电平的时间，这两个数值都应该小于4096
#pwm.set_all_angle(180) # 所有通道的舵机都设置为180度
pwm.set_angle(0, 180) # 设置0通道为180度
pwm.get_pwm_frequency() # 读取频率
