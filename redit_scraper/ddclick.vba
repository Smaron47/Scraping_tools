Dim Driver As Selenium.ChromeDriver
Set Driver = New Selenium.ChromeDriver
AddOptions Driver
Driver.Timeouts.ImplicitWait = 20
Dim StartCell As Range
Dim TrackingNumbers As Variant
Dim OrderIDArray As Variant
Dim divElement As Object
Dim childElements As Object
Dim childElement As Object


Driver.Get OrderURL
Sleep 3000
Entiretext1 = Driver.FindElementByTag("body").Text

'End If

'If InStr(1, entiretext, "Tracking Number:") Then
WaitUntilElementPresentUsingCSS Driver, OTHER_PARCEL_CSS
Dim Element As WebElement
Set Element = Driver.FindElementByCss(OTHER_PARCEL_CSS, 10)
Element.Click
Set Element = Driver.FindElementByClass(" css-vnprg8-menu")

Set divElement = Driver.FindElementByXPath("//div[@direction='column']")
divElement.Click

Sleep 2000
Set childElements = Driver.FindElementsByXPath(".//*[starts-with(@id, 'react-select-2-option-')]")
Sheet1.Range("F3:G100").ClearContents

m = 0
For Each childElement In childElements
    Set childElement = Driver.FindElementsByXPath(".//*[starts-with(@id, 'react-select-2-option-')]")(m)
    childElement.Click
    ' Additional actions after clicking, if needed

    ' Wait for some time after clicking
    Sleep 2000

    ' Your previous Chrome automation code here to get tracking numbers

    ' Write the tracking number to the worksheet
    ' Assuming you have a variable TrackingNumber obtained from the previous code
    startCell.Offset(m+1, 1).Value = childElement.Text

    ' Click on the div element again
    divElement.Click

    ' Wait for some time after clicking
    Sleep 2000

    m = m + 1
Next childElement






TrackingNumbers = Split(Element.Text, Chr(10))



Dim TrackingNumber2 As Variant
Dim StartRow As Long

For k = 0 To UBound(TrackingNumbers)
StartCell.Offset(k, 0).Value = OrderIDArray(i) 'Cells(StartRow, 6).Value = Url
StartCell.Offset(k, 1).Value = Left(TrackingNumbers(k), InStr(1, TrackingNumbers(k), " ")) '2 'Sheet1.Cells(StartRow, 7).Value = TrackingNumber
StartRow = 2
Next k

***** Add code for selecting the other item(s) in the list and  ****

Entiretext1 = Driver.FindElementByTag("body").Text
