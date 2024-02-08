## Role - rol-capg-compareprepost

Role used to compare prechecks and postcheck csv files.

## Requirements

Requires 2 csv files named: post_checks.csv and pre_checks.csv.

## Role Variables

    Variables in vars/main.yml:
      script_path: "roles/rol-capg-compareprepost/files/compare_csv.py"
      output_path: "roles/rol-capg-compareprepost/files/output.csv"
    
    Provide the paths for `pre_checks.csv` and `post_checks.csv` using `--extra-vars`.

## Usage

Run the playbook using the command:
ansible-playbook playbook.yml --extra-vars "pre_checks_path=/path/to/pre_checks.csv post_checks_path=/path/to/post_checks.csv"

## Dependencies

none.

## Example Playbook

    - hosts: localhost
      gather_facts: false
      roles:
        - rol-capg-compareprepost

## License

CAPGEMINI CIS

## Author Information

PU Automation.


