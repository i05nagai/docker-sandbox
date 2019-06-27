
## Setup

```
dpkg-reconfigure slapd

If you enable this option, no initial configuration or database will be created for you.
Omit OpenLDAP server configuration? [yes/no] no

The DNS domain name is used to construct the base DN of the LDAP directory. For example, 'foo.example.org' will create the directory with 'dc=foo, dc=example, dc=org' as
base DN.
DNS domain name: example.com

Please enter the name of the organization to use in the base DN of your LDAP directory.
Organization name: organizationname

Please enter the password for the admin entry in your LDAP directory.
Administrator password:

HDB and BDB use similar storage formats, but HDB adds support for subtree renames. Both support the same configuration options.
The MDB backend is recommended. MDB uses a new storage format and requires less configuration than BDB or HDB.
In any case, you should review the resulting database configuration for your needs. See /usr/share/doc/slapd/README.Debian.gz for more details.
  1. BDB  2. HDB  3. MDB
Database backend to use: MDB
```

```
slapd
```

```
Please select the geographic area in which you live. Subsequent configuration questions will narrow this down by presenting a list of cities, representing the time zones
in which they are located.

  1. Africa  2. America  3. Antarctica  4. Australia  5. Arctic  6. Asia  7. Atlantic  8. Europe  9. Indian  10. Pacific  11. SystemV  12. US  13. Etc
Geographic area: 8

Please select the city or region corresponding to your time zone.

  1. Amsterdam  7. Berlin      13. Chisinau    19. Isle_of_Man  25. Lisbon      31. Mariehamn  37. Paris      43. San_Marino  49. Stockholm  55. Vaduz      61. Zagreb
  2. Andorra    8. Bratislava  14. Copenhagen  20. Istanbul     26. Ljubljana   32. Minsk      38. Podgorica  44. Sarajevo    50. Tallinn    56. Vatican    62. Zaporozhye
  3. Astrakhan  9. Brussels    15. Dublin      21. Jersey       27. London      33. Monaco     39. Prague     45. Saratov     51. Tirane     57. Vienna     63. Zurich
  4. Athens     10. Bucharest  16. Gibraltar   22. Kaliningrad  28. Luxembourg  34. Moscow     40. Riga       46. Simferopol  52. Tiraspol   58. Vilnius
  5. Belfast    11. Budapest   17. Guernsey    23. Kiev         29. Madrid      35. Nicosia    41. Rome       47. Skopje      53. Ulyanovsk  59. Volgograd
  6. Belgrade   12. Busingen   18. Helsinki    24. Kirov        30. Malta       36. Oslo       42. Samara     48. Sofia       54. Uzhgorod   60. Warsaw
Time zone: 7
```

By default,

- root DN
    - this user's DN is cn=admin,dc=example,dc=com


## Configurtion
* `/etc/ldap/slapd.d/`

## Reference
- [OpenLDAP Server](https://help.ubuntu.com/lts/serverguide/openldap-server.html.en)
- [How To Install and Configure OpenLDAP and phpLDAPadmin on Ubuntu 16\.04 \| DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-openldap-and-phpldapadmin-on-ubuntu-16-04)
- [OpenLDAP, Main Page](https://www.openldap.org/)
