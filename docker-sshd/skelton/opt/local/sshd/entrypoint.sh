#!/bin/sh

set -x

HOME_BASEDIR=${HOME_BASEDIR:-"/home"}
HOME_USERS=${HOME_USERS:-""}
HOME_SUDOERS="${HOME_SUDOERS:-""}"

# required environment:
#   HOME_BASEDIR
# Usage:
# addusers <first uid> <default shell> [<github:[shell]>...]
addusers() {
  local first_uid=$1
  shift
  local default_shell=$1
  shift
  for u in "$@"; do
    local user=$(echo $u | cut -d: -f 1)
    local user_shell=$(echo $u | cut -d: -f 2)

    local adduser_args=""
    local uid=""
    local gid=""

    # if home directory for this user exists
    if test -d "$HOME_BASEDIR/$user"; then
      uid=$(/bin/ls -nld $HOME_BASEDIR/$user | cut -d' ' -f3)
      gid=$(/bin/ls -nld $HOME_BASEDIR/$user | cut -d' ' -f4)

      addgroup --gid $gid $user
      adduser_args="--uid $uid --gid $gid"
    fi

    local home=$HOME_BASEDIR/$user

    adduser $user --firstuid $first_uid --shell ${user_shell:-$default_shell} --home $home $adduser_args < /dev/null

    if test "x$uid" = "x"; then
      uid=$(/bin/ls -nld $home | cut -d' ' -f3)
      gid=$(/bin/ls -nld $home | cut -d' ' -f4)
    fi

    # Adds ssh keys
    install -m 700 -o $uid -g $gid -d $home/.ssh/
    curl -o $home/.ssh/authorized_keys https://github.com/$user.keys
    chown $uid:$gid $home/.ssh/authorized_keys
    chmod 600 $home/.ssh/authorized_keys
  done
}
# add sudoers
for user in $HOME_SUDOERS; do
  cat >> /etc/sudoers.d/sshd <<EOF
$user ALL=(ALL:ALL) NOPASSWD:ALL
EOF
done

addusers 1000 /bin/bash $HOME_USERS


if test "x$1" = "x"; then
  exec /bin/bash
else
  exec "$@"
fi
