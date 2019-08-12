[![Build Status](https://travis-ci.org/bihealth/ansible-role-apache.svg?branch=master)](https://travis-ci.org/bihealth/ansible-role-apache)

# Apache

Basic setup as Apache (currently for DAVrods only).

## Requirements

You have to configure the SSL certificate at least for the `apache_cert_name` (defaults to `inventory_hostname`).

## Role Variables

See `defaults/main.yml` for all role variables and their documentation.

## Dependencies

- `bihealth.ssl_certs`

## Example Playbook

```yaml
- hosts: servers
  vars:
    ssl_ssl_certs:
      - name: example.com
    apache_cert_name: example.com
  roles:
    - role: bihealth.ansible-role-apache
```

## License

MIT

## Author Information

- Manuel Holtgrewe

Created with love at [Core Unit Bioinformatics (CUBI), Berlin Institute of Health (BIH)](https://www.cubi.bihealth.org).
