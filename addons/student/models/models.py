# -*- coding: utf-8 -*-

from odoo import models, fields


class Student(models.Model):
    _name = "wb.student"
    _description = "this is student profile"
    name=fields.Char("Name")
    name1=fields.Char("Name1")
    name2=fields.Char("Name2")