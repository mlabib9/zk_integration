# -*- coding: utf-8 -*-
# Copyright (c) 2021, Peter Maged and contributors
# For license information, please see license.txt


import frappe 



def update_employee_name_fro_checkin():
    frappe.db.sql("""
                  update `tabEmployee Checkin` log 
                  set log.employee_name = 
                  (select emp.employee_name from tabEmployee emp where emp.name = log.employee limit 1) ;
                  """)


