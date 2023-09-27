#test automate filling of work doc
from docx.shared import Cm

from docxtpl import DocxTemplate, InlineImage

from docx.shared import Cm, Inches, Mm, Emu

import random

import datetime

import matplotlib.pyplot as plt

#Import template document

template = DocxTemplate('test.docx')

#Generate list of random values
def getinput():
    Policy= input('policy for deviation')
    Policy_Owner=input('Polcy Owner')
    Business_Unit=input('Buisness Unit')
    Risk_Owner=input('Risk Owner')
    num_of_devi=int(input('Number of clause to be deviated'))
    table=[]
    for num_of_devi!=0 :
        Clause=input('Clause to be Deviated')
        Description=input('Description of the Deviation')
        Control=input('Compensating Control')
        row={'Clause':Clause,'Description':Description,'Control':Control}
        table.append(row)
        num_of_devi-1
    Risk_Just=input('Risk Justification')
    Con_accep=input('consideration for accetance')
    dateofrisknoti=input('date of risk notification')
    accptperiod=input('Accpetance Period')
    Nextreview=input('next review date')
    addrem=input('addtional remarks')

#Declare template variables

context = {

'Policy': Policy,

'Policy Owner': Policy_Owner,

'Business Unit': Business_Unit,

'Risk Owner': Risk_Owner,

'table_contents': table,

'Risk Justification': Risk_Just


}

#Render automated report

template.render(context)

template.save('test.docx')
