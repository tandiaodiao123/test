#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/2 11:51
# @Author  : datan
# @Site    : 
# @File    : run.py


from R_W_excel import read_data
from R_W_excel import write_data


def run_case():
    #注册
    register_case = read_data('all_case.xlsx', 'register')
    write_data(register_case,'all_case.xlsx','register',7,8)
    #登录
    login_case = read_data('all_case.xlsx', 'login')
    write_data(login_case,'all_case.xlsx','login',7,8)
    # 充值
    recharge_case=read_data('all_case.xlsx','recharge')
    write_data(recharge_case,'all_case.xlsx','recharge',7,8)
    #提现
    withdraw_case=read_data('all_case.xlsx', 'withdraw')
    write_data(withdraw_case,'all_case.xlsx','withdraw',7,8)
    print('我在执行')
run_case()

