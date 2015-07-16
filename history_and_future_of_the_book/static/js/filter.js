$(document).ready(function() {
    var myConnect = "Provider=Microsoft.Jet.OLEDB.4.0; Data Source=d:\\sdi.mdb"; 
 
    var ConnectObj = new ActiveXObject("ADODB.Connection");
    var RS = new ActiveXObject("ADODB.Recordset");
    var sql="SELECT * FROM history_and_future_of_the_book_table WHERE file_position='A07686+dwdID1';";
 
    ConnectObj.Open (myConnect);
    RS.Open(sql,ConnectObj,adOpenForwardOnly,adLockReadOnly,adCmdText);
 
    var fieldCount = RS.Fields.Count;
    alert("Field Count" + fieldCount);    
    RS.Close();
    ConnectObj.Close();
});