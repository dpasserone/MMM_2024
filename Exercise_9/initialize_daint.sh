cp id_rsa cscs-key ~/.ssh/

cat <<EOT >> ~/.ssh/config
Host ela.cscs.ch
  User $1
  Port 22
  ServerAliveInterval 5
EOT

