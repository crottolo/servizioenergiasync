Option Compare Database

Function RecordToJSON(rs As DAO.Recordset) As String
    Dim fld As DAO.Field
    Dim jsonObj As Object
    Dim valuePart As Variant
    
    ' Crea un nuovo oggetto Dictionary per contenere i dati
    Set jsonObj = CreateObject("Scripting.Dictionary")

    For Each fld In rs.Fields
        If IsNull(fld.Value) Then
            valuePart = Null
        Else
            valuePart = fld.Value
        End If
        
        ' Aggiungi il valore al Dictionary con il nome del campo come chiave
        jsonObj.Add fld.name, valuePart
    Next fld

    ' Usa VBA-JSON per convertire il Dictionary in una stringa JSON
    RecordToJSON = JsonConverter.ConvertToJson(jsonObj)
    
    ' Pulizia
    Set jsonObj = Nothing
End Function

Public Sub httpclient(jsonPayload As String, endpoint As String)

    Dim xmlhttp As New MSXML2.XMLHTTP60, myurl As String
    Dim responseText As String
    Dim token As String
    
    myurl = "http://178.32.226.230:8000" & endpoint
    token = "ServizioEnergia1!" ' Sostituisci con il tuo token reale

    xmlhttp.Open "POST", myurl, False
    xmlhttp.setRequestHeader "Content-Type", "application/json"
    xmlhttp.setRequestHeader "Authorization", "Bearer " & token
    xmlhttp.send jsonPayload
    
    responseText = xmlhttp.responseText
    
    ' Controllo manuale della risposta
    If InStr(1, responseText, """success"":true") > 0 Then
        'MsgBox "Success!"
        
    Else
        MsgBox "Failed!"
    End If
End Sub





Private Sub Form_AfterUpdate()
    Dim rs As DAO.Recordset
    Dim jsonData As String

    Set rs = Me.RecordsetClone
    rs.Bookmark = Me.Bookmark

    jsonData = RecordToJSON(rs)

    Call httpclient(jsonData, "/clienti")
End Sub

Private Sub invia_post_Click()
    Dim rs As DAO.Recordset
    Dim jsonData As String

    Set rs = Me.RecordsetClone
    rs.Bookmark = Me.Bookmark

    jsonData = RecordToJSON(rs)

    Call httpclient(jsonData, "/clienti")
End Sub

