# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Student(models.Model):
    _name = "wb.student"
    _description = "this is student profile"
    name=fields.Char("Name")
    name1=fields.Char("Name1")
    name2=fields.Char("Name2")
    file_to_sign = fields.Binary(string=’File to sign’ )

    def action_do_something(self):
        for record in self:
            record.name = "Something"
        print("hello")
        return True
