#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.


import wx
from cairis.core.armid import *
import cairis.core.DomainProperty 
from DomainPropertyDialog import DomainPropertyDialog
from DialogClassParameters import DialogClassParameters
from cairis.core.ARM import *
from DimensionBaseDialog import DimensionBaseDialog

class DomainPropertiesDialog(DimensionBaseDialog):
  def __init__(self,parent):
    DimensionBaseDialog.__init__(self,parent,DOMAINPROPERTIES_ID,'Domain Properties',(930,300),'domainproperty.png')
    idList = [DOMAINPROPERTIES_DOMAINPROPERTYLIST_ID,DOMAINPROPERTIES_BUTTONADD_ID,DOMAINPROPERTIES_BUTTONDELETE_ID]
    columnList = ['Name','Type']
    self.buildControls(idList,columnList,self.dbProxy.getDomainProperties,'domainproperty')
    listCtrl = self.FindWindowById(DOMAINPROPERTIES_DOMAINPROPERTYLIST_ID)
    listCtrl.SetColumnWidth(0,300)
    listCtrl.SetColumnWidth(1,200)


  def addObjectRow(self,listCtrl,listRow,dp):
    listCtrl.InsertStringItem(listRow,dp.name())
    listCtrl.SetStringItem(listRow,1,dp.type())


  def onAdd(self,evt):
    try:
      addParameters = DialogClassParameters(DOMAINPROPERTY_ID,'Add Domain Property',DomainPropertyDialog,DOMAINPROPERTY_BUTTONCOMMIT_ID,self.dbProxy.addDomainProperty,True)
      self.addObject(addParameters)
    except ARMException,errorText:
      dlg = wx.MessageDialog(self,str(errorText),'Add Domain Property',wx.OK | wx.ICON_ERROR)
      dlg.ShowModal()
      dlg.Destroy()
      return

  def onUpdate(self,evt):
    selectedObjt = self.objts[self.selectedLabel]
    try:
      updateParameters = DialogClassParameters(DOMAINPROPERTY_ID,'Edit Domain Property',DomainPropertyDialog,DOMAINPROPERTY_BUTTONCOMMIT_ID,self.dbProxy.updateDomainProperty,False)
      self.updateObject(selectedObjt,updateParameters)
    except ARMException,errorText:
      dlg = wx.MessageDialog(self,str(errorText),'Edit Domain Property',wx.OK | wx.ICON_ERROR)
      dlg.ShowModal()
      dlg.Destroy

  def onDelete(self,evt):
    try:
      self.deleteObject('No Domain Property','Delete Domain Property',self.dbProxy.deleteDomainProperty)
    except ARMException,errorText:
      dlg = wx.MessageDialog(self,str(errorText),'Delete Domain Property',wx.OK | wx.ICON_ERROR)
      dlg.ShowModal()
      dlg.Destroy
