# Helpdesk System

A modular Helpdesk System designed to delegate helpdesk tickets based on their source.

---

## Modules Overview

| Module Name     | Description                                            |
|-----------------|--------------------------------------------------------|
| `helpdesk_app`  | Core helpdesk module handling incoming tickets.        |
| `todo_app`      | To-do app for handling internal tickets.               |
| `helpdesk_todo` | Routes internal tickets to the ToDo app.               |
| `helpdesk_crm`  | Routes portal tickets to the CRM app.                  |
| `crm_ext`       | Extension module for CRM ticket handling.              |
| `sale_ext`      | Optional: Extends CRM integration with sales pipeline. |


## Prerequisite

- [Odoo 18](https://www.odoo.com/documentation/18.0/administration/on_premise/source.html)


## Usage

1. Clone the repository.
2. Run Odoo with the modules:
```bash
odoo-bin --addons-path <odoo's addons path>, <repo's path>
```


## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Get in Touch
[<img src="https://img.shields.io/badge/email-white?&style=for-the-badge&logo=gmail" alt="Email"/>](mailto:bhabishworgrg@gmail.com)
[<img src="https://img.shields.io/badge/linkedin-blue?&style=for-the-badge" alt="LinkedIn"/>](https://www.linkedin.com/in/bhabishwor-gurung/)
